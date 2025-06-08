import psutil
import time
import threading
from typing import Dict, Any, List, Callable
import subprocess

class SystemMonitor:

    def __init__(self):
        self.monitoring_active = False
        self.monitor_thread = None
        self.callbacks = []
        self.update_interval = 1.0

        self.cpu_history = []
        self.memory_history = []
        self.gpu_history = []
        self.max_history_length = 60

        self.current_stats = {
            'cpu_percent': 0,
            'memory_percent': 0,
            'memory_used_gb': 0,
            'memory_total_gb': 0,
            'gpu_percent': 0,
            'gpu_memory_used': 0,
            'gpu_memory_total': 0,
            'disk_percent': 0,
            'network_sent': 0,
            'network_recv': 0,
            'processes': []
        }

    def start_monitoring(self):

        if not self.monitoring_active:
            self.monitoring_active = True
            self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
            self.monitor_thread.start()

    def stop_monitoring(self):

        self.monitoring_active = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=2)

    def add_callback(self, callback: Callable[[Dict[str, Any]], None]):

        self.callbacks.append(callback)

    def remove_callback(self, callback: Callable[[Dict[str, Any]], None]):

        if callback in self.callbacks:
            self.callbacks.remove(callback)

    def _monitor_loop(self):

        last_network = psutil.net_io_counters()

        while self.monitoring_active:
            try:

                cpu_percent = psutil.cpu_percent(interval=None)

                memory = psutil.virtual_memory()
                memory_percent = memory.percent
                memory_used_gb = memory.used / (1024**3)
                memory_total_gb = memory.total / (1024**3)

                disk = psutil.disk_usage('/')
                disk_percent = disk.percent

                current_network = psutil.net_io_counters()
                network_sent = current_network.bytes_sent - last_network.bytes_sent
                network_recv = current_network.bytes_recv - last_network.bytes_recv
                last_network = current_network

                gpu_percent, gpu_memory_used, gpu_memory_total = self._get_gpu_usage()

                processes = self._get_top_processes()

                self.current_stats.update({
                    'cpu_percent': cpu_percent,
                    'memory_percent': memory_percent,
                    'memory_used_gb': memory_used_gb,
                    'memory_total_gb': memory_total_gb,
                    'gpu_percent': gpu_percent,
                    'gpu_memory_used': gpu_memory_used,
                    'gpu_memory_total': gpu_memory_total,
                    'disk_percent': disk_percent,
                    'network_sent': network_sent,
                    'network_recv': network_recv,
                    'processes': processes
                })

                self._update_history()

                for callback in self.callbacks:
                    try:
                        callback(self.current_stats.copy())
                    except Exception as e:
                        print(f"Error in monitoring callback: {e}")

                time.sleep(self.update_interval)

            except Exception as e:
                print(f"Error in monitoring loop: {e}")
                time.sleep(self.update_interval)

    def _get_gpu_usage(self) -> tuple:

        try:

            nvidia_usage = self._get_nvidia_usage()
            if nvidia_usage[0] is not None:
                return nvidia_usage

            amd_usage = self._get_amd_usage()
            if amd_usage[0] is not None:
                return amd_usage

            intel_usage = self._get_intel_usage()
            if intel_usage[0] is not None:
                return intel_usage

        except Exception as e:
            print(f"Error getting GPU usage: {e}")

        return 0, 0, 0

    def _get_nvidia_usage(self) -> tuple:

        try:
            result = subprocess.run([
                "nvidia-smi", "--query-gpu=utilization.gpu,memory.used,memory.total",
                "--format=csv,noheader,nounits"
            ], capture_output=True, text=True, check=True, timeout=5)

            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                if lines and lines[0]:
                    parts = lines[0].split(',')
                    if len(parts) >= 3:
                        gpu_percent = float(parts[0].strip())
                        memory_used = float(parts[1].strip())
                        memory_total = float(parts[2].strip())
                        return gpu_percent, memory_used, memory_total
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
            pass

        return None, None, None

    def _get_amd_usage(self) -> tuple:

        try:

            result = subprocess.run([
                "wmic", "path", "win32_VideoController", "get",
                "AdapterRAM,DriverVersion,Name,VideoProcessor", "/format:csv"
            ], capture_output=True, text=True, check=False, timeout=5)

            return 0, 0, 0
        except Exception:
            pass

        return None, None, None

    def _get_intel_usage(self) -> tuple:

        try:

            return 0, 0, 0
        except Exception:
            pass

        return None, None, None

    def _get_top_processes(self, limit: int = 10) -> List[Dict[str, Any]]:

        processes = []

        try:
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'memory_info']):
                try:
                    proc_info = proc.info
                    if proc_info['cpu_percent'] > 0 or proc_info['memory_percent'] > 0.1:
                        memory_mb = 0
                        if proc_info['memory_info']:
                            memory_mb = proc_info['memory_info'].rss / (1024 * 1024)

                        processes.append({
                            'pid': proc_info['pid'],
                            'name': proc_info['name'],
                            'cpu_percent': proc_info['cpu_percent'],
                            'memory_percent': proc_info['memory_percent'],
                            'memory_mb': memory_mb
                        })
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
        except Exception as e:
            print(f"Error getting processes: {e}")

        processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
        return processes[:limit]

    def _update_history(self):

        current_time = time.time()

        self.cpu_history.append({
            'time': current_time,
            'value': self.current_stats['cpu_percent']
        })

        self.memory_history.append({
            'time': current_time,
            'value': self.current_stats['memory_percent']
        })

        self.gpu_history.append({
            'time': current_time,
            'value': self.current_stats['gpu_percent']
        })

        if len(self.cpu_history) > self.max_history_length:
            self.cpu_history.pop(0)
        if len(self.memory_history) > self.max_history_length:
            self.memory_history.pop(0)
        if len(self.gpu_history) > self.max_history_length:
            self.gpu_history.pop(0)

    def get_current_stats(self) -> Dict[str, Any]:

        return self.current_stats.copy()

    def get_cpu_history(self) -> List[Dict[str, Any]]:

        return self.cpu_history.copy()

    def get_memory_history(self) -> List[Dict[str, Any]]:

        return self.memory_history.copy()

    def get_gpu_history(self) -> List[Dict[str, Any]]:

        return self.gpu_history.copy()

    def get_system_info(self) -> Dict[str, Any]:
        """Get comprehensive system information"""
        system_info = {
            'cpu': {},
            'memory': {},
            'gpu': {},
            'disk': {},
            'network': {},
            'os': {}
        }

        try:

            cpu_freq = psutil.cpu_freq()
            system_info['cpu'] = {
                'name': self._get_cpu_name(),
                'cores': psutil.cpu_count(logical=False),
                'threads': psutil.cpu_count(logical=True),
                'frequency_current': cpu_freq.current if cpu_freq else 0,
                'frequency_max': cpu_freq.max if cpu_freq else 0,
                'usage_per_core': psutil.cpu_percent(percpu=True)
            }


            memory = psutil.virtual_memory()
            swap = psutil.swap_memory()
            system_info['memory'] = {
                'total_gb': memory.total / (1024**3),
                'available_gb': memory.available / (1024**3),
                'used_gb': memory.used / (1024**3),
                'percent': memory.percent,
                'swap_total_gb': swap.total / (1024**3),
                'swap_used_gb': swap.used / (1024**3),
                'swap_percent': swap.percent
            }


            system_info['gpu'] = self._get_detailed_gpu_info()


            disk_usage = psutil.disk_usage('/')
            disk_io = psutil.disk_io_counters()
            system_info['disk'] = {
                'total_gb': disk_usage.total / (1024**3),
                'used_gb': disk_usage.used / (1024**3),
                'free_gb': disk_usage.free / (1024**3),
                'percent': (disk_usage.used / disk_usage.total) * 100,
                'read_bytes': disk_io.read_bytes if disk_io else 0,
                'write_bytes': disk_io.write_bytes if disk_io else 0
            }


            network_io = psutil.net_io_counters()
            system_info['network'] = {
                'bytes_sent': network_io.bytes_sent,
                'bytes_recv': network_io.bytes_recv,
                'packets_sent': network_io.packets_sent,
                'packets_recv': network_io.packets_recv
            }


            import platform
            system_info['os'] = {
                'system': platform.system(),
                'release': platform.release(),
                'version': platform.version(),
                'machine': platform.machine(),
                'processor': platform.processor()
            }

        except Exception as e:
            print(f"Error getting system info: {e}")

        return system_info

    def _get_cpu_name(self) -> str:
        """Get CPU name"""
        try:
            result = subprocess.run([
                "wmic", "cpu", "get", "name", "/format:value"
            ], capture_output=True, text=True, check=False)

            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if line.startswith('Name='):
                        return line.split('=', 1)[1].strip()
        except Exception:
            pass

        return "Unknown CPU"

    def _get_detailed_gpu_info(self) -> Dict[str, Any]:
        """Get detailed GPU information"""
        gpu_info = {
            'name': 'Unknown',
            'driver_version': 'Unknown',
            'memory_total': 0,
            'memory_used': 0,
            'usage_percent': 0,
            'temperature': 0
        }

        try:

            nvidia_info = self._get_nvidia_detailed_info()
            if nvidia_info['name'] != 'Unknown':
                return nvidia_info


            result = subprocess.run([
                "wmic", "path", "win32_VideoController", "get",
                "Name,DriverVersion", "/format:csv"
            ], capture_output=True, text=True, check=False)

            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                for line in lines[1:]:
                    if line.strip() and ',' in line:
                        parts = line.split(',')
                        if len(parts) >= 4:
                            gpu_info['name'] = parts[2] if parts[2] else 'Unknown'
                            gpu_info['driver_version'] = parts[1] if parts[1] else 'Unknown'
                            if parts[0] and parts[0].isdigit():
                                gpu_info['memory_total'] = int(parts[0]) / (1024**2)
                            break
        except Exception as e:
            print(f"Error getting GPU info: {e}")

        return gpu_info

    def _get_nvidia_detailed_info(self) -> Dict[str, Any]:
        """Get detailed NVIDIA GPU info"""
        gpu_info = {
            'name': 'Unknown',
            'driver_version': 'Unknown',
            'memory_total': 0,
            'memory_used': 0,
            'usage_percent': 0,
            'temperature': 0
        }

        try:
            result = subprocess.run([
                "nvidia-smi", "--query-gpu=name,driver_version,memory.total,memory.used,utilization.gpu,temperature.gpu",
                "--format=csv,noheader,nounits"
            ], capture_output=True, text=True, check=True, timeout=5)

            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                if lines and lines[0]:
                    parts = [p.strip() for p in lines[0].split(',')]
                    if len(parts) >= 6:
                        gpu_info['name'] = parts[0]
                        gpu_info['driver_version'] = parts[1]
                        gpu_info['memory_total'] = float(parts[2])
                        gpu_info['memory_used'] = float(parts[3])
                        gpu_info['usage_percent'] = float(parts[4])
                        gpu_info['temperature'] = float(parts[5])
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
            pass

        return gpu_info

    def get_fps_info(self) -> Dict[str, Any]:
        """Get FPS information (placeholder for future implementation)"""
        return {
            'current_fps': 0,
            'average_fps': 0,
            'min_fps': 0,
            'max_fps': 0,
            'frame_time': 0
        }

    def set_update_interval(self, interval: float):

        self.update_interval = max(0.1, interval)
