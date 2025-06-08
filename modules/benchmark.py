import threading
import time
import psutil
import subprocess
import os
import json
import hashlib
import math
import random
import numpy as np
import multiprocessing
import zlib
from datetime import datetime
import winreg

try:
    import OpenGL.GL as gl
    import OpenGL.GLUT as glut
    import OpenGL.GLU as glu
    OPENGL_AVAILABLE = True
except ImportError:
    OPENGL_AVAILABLE = False

try:
    import pygame
    from pygame.locals import DOUBLEBUF, OPENGL
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

def cpu_math_task(n):

    total = 0
    for i in range(1, n):
        total += math.sqrt(i) * math.sin(i) * math.cos(i)
    return total

def cpu_compression_task(data_size):

    data = os.urandom(data_size)
    compressed = zlib.compress(data, level=6)
    decompressed = zlib.decompress(compressed)
    return len(compressed)

class PCBenchmark:
    def __init__(self):
        self.results = {}
        self.is_running = False
        self.progress_callback = None
        self.status_callback = None

        self.reference_scores = {
            'cpu_single_math': 8.0,
            'cpu_single_hash': 4.0,
            'cpu_multi_math': 2.0,
            'cpu_multi_compression': 3.0,
            'memory_bandwidth': 12000,
            'memory_latency': 0.1,
            'disk_seq_write': 800,
            'disk_seq_read': 900,
            'disk_random_4k': 80000,
            'gpu_rendering': 8.0
        }

    def set_callbacks(self, progress_callback, status_callback):

        self.progress_callback = progress_callback
        self.status_callback = status_callback

    def update_progress(self, value):

        if self.progress_callback:
            self.progress_callback(value)

    def update_status(self, message):

        if self.status_callback:
            self.status_callback(message)

    def run_full_benchmark(self):

        if self.is_running:
            return

        self.is_running = True
        self.results = {}

        try:
            self.update_status("Initializing comprehensive benchmark...")
            self.update_progress(0)
            time.sleep(1)

            self.update_status("Testing CPU performance...")
            cpu_score = self.benchmark_cpu_comprehensive()
            self.results['cpu'] = cpu_score
            self.update_progress(40)

            self.update_status("Testing memory performance...")
            memory_score = self.benchmark_memory_comprehensive()
            self.results['memory'] = memory_score
            self.update_progress(60)

            self.update_status("Testing disk performance...")
            disk_score = self.benchmark_disk_comprehensive()
            self.results['disk'] = disk_score
            self.update_progress(90)

            self.update_status("Testing GPU performance...")
            gpu_score = self.benchmark_gpu_comprehensive()
            self.results['gpu'] = gpu_score
            self.update_progress(95)

            self.update_status("Calculating overall score...")
            overall_score = self.calculate_overall_score()
            self.results['overall'] = overall_score
            self.update_progress(100)

            self.save_results()
            self.update_status("Comprehensive benchmark completed!")

        except Exception as e:
            self.update_status(f"Benchmark failed: {str(e)}")
        finally:
            self.is_running = False

        return self.results

    def calculate_score(self, actual_time, reference_time):

        if actual_time <= 0:
            return 100

        performance_ratio = reference_time / actual_time

        if performance_ratio >= 3.0:

            score = 95 + min(5, (performance_ratio - 3.0) * 2)
        elif performance_ratio >= 2.0:

            score = 80 + (performance_ratio - 2.0) * 15
        elif performance_ratio >= 1.0:

            score = 50 + (performance_ratio - 1.0) * 30
        else:

            score = performance_ratio * 50

        return min(100, max(0, round(score, 1)))

    def calculate_bandwidth_score(self, actual_bandwidth, reference_bandwidth):

        if actual_bandwidth <= 0:
            return 0

        performance_ratio = actual_bandwidth / reference_bandwidth

        if performance_ratio >= 3.0:

            score = 95 + min(5, (performance_ratio - 3.0) * 2)
        elif performance_ratio >= 2.0:

            score = 80 + (performance_ratio - 2.0) * 15
        elif performance_ratio >= 1.0:

            score = 50 + (performance_ratio - 1.0) * 30
        else:

            score = performance_ratio * 50

        return min(100, max(0, round(score, 1)))

    def benchmark_cpu_comprehensive(self):

        scores = {}

        cpu_info = self.get_cpu_info()
        scores['info'] = cpu_info

        self.update_status("Testing CPU single-core math performance...")
        single_math_time = self.cpu_single_math_test()
        single_math_score = self.calculate_score(single_math_time, self.reference_scores['cpu_single_math'])
        scores['single_math'] = {
            'time': round(single_math_time, 3),
            'score': single_math_score
        }

        if not self.is_running:
            return scores

        self.update_status("Testing CPU single-core hashing performance...")
        single_hash_time = self.cpu_single_hash_test()
        single_hash_score = self.calculate_score(single_hash_time, self.reference_scores['cpu_single_hash'])
        scores['single_hash'] = {
            'time': round(single_hash_time, 3),
            'score': single_hash_score
        }

        if not self.is_running:
            return scores

        self.update_status("Testing CPU multi-core math performance...")
        multi_math_time = self.cpu_multi_math_test()
        multi_math_score = self.calculate_score(multi_math_time, self.reference_scores['cpu_multi_math'])
        scores['multi_math'] = {
            'time': round(multi_math_time, 3),
            'score': multi_math_score
        }

        if not self.is_running:
            return scores

        self.update_status("Testing CPU multi-core compression performance...")
        multi_comp_time = self.cpu_multi_compression_test()
        multi_comp_score = self.calculate_score(multi_comp_time, self.reference_scores['cpu_multi_compression'])
        scores['multi_compression'] = {
            'time': round(multi_comp_time, 3),
            'score': multi_comp_score
        }

        single_core_avg = (single_math_score + single_hash_score) / 2
        multi_core_avg = (multi_math_score + multi_comp_score) / 2
        cpu_score = round((single_core_avg * 0.3) + (multi_core_avg * 0.7), 1)
        scores['score'] = cpu_score

        return scores

    def cpu_single_math_test(self):

        start_time = time.time()

        total = 0
        for i in range(1, 500000):
            if not self.is_running:
                break
            total += math.sqrt(i) * math.sin(i) * math.cos(i)

        return time.time() - start_time

    def cpu_single_hash_test(self):

        start_time = time.time()

        data = b"benchmark_data_" * 1000
        for i in range(50000):
            if not self.is_running:
                break
            hashlib.sha256(data + str(i).encode()).hexdigest()

        return time.time() - start_time

    def cpu_multi_math_test(self):

        cores = multiprocessing.cpu_count()
        chunk_size = 200000 // cores

        start_time = time.time()
        try:
            with multiprocessing.Pool(cores) as pool:
                if self.is_running:
                    pool.map(cpu_math_task, [chunk_size] * cores)
        except Exception as e:

            self.update_status("Multiprocessing failed, using threading...")
            return self.cpu_multi_math_test_threading()

        return time.time() - start_time

    def cpu_multi_math_test_threading(self):

        def math_task_thread():
            total = 0
            for i in range(1, 200000):
                if not self.is_running:
                    break
                total += math.sqrt(i) * math.sin(i) * math.cos(i)
            return total

        cores = psutil.cpu_count()
        start_time = time.time()

        threads = []
        for _ in range(cores):
            thread = threading.Thread(target=math_task_thread)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return time.time() - start_time

    def cpu_multi_compression_test(self):

        cores = multiprocessing.cpu_count()
        data_size = 2 * 1024 * 1024

        start_time = time.time()
        try:
            with multiprocessing.Pool(cores) as pool:
                if self.is_running:
                    pool.map(cpu_compression_task, [data_size] * cores)
        except Exception as e:

            self.update_status("Multiprocessing failed, using threading...")
            return self.cpu_multi_compression_test_threading()

        return time.time() - start_time

    def cpu_multi_compression_test_threading(self):

        def compression_task_thread():
            data = os.urandom(2 * 1024 * 1024)
            compressed = zlib.compress(data, level=6)
            decompressed = zlib.decompress(compressed)
            return len(compressed)

        cores = psutil.cpu_count()
        start_time = time.time()

        threads = []
        for _ in range(cores):
            thread = threading.Thread(target=compression_task_thread)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return time.time() - start_time

    def benchmark_memory_comprehensive(self):

        scores = {}

        memory_info = psutil.virtual_memory()
        scores['total_gb'] = round(memory_info.total / (1024**3), 2)
        scores['available_gb'] = round(memory_info.available / (1024**3), 2)

        memory_type = self.get_memory_info()
        scores['memory_type'] = memory_type

        self.update_status("Testing memory bandwidth...")
        bandwidth_score, bandwidth_mbps = self.memory_bandwidth_test()
        scores['bandwidth'] = {
            'mbps': round(bandwidth_mbps, 2),
            'score': bandwidth_score
        }

        if not self.is_running:
            return scores

        self.update_status("Testing memory latency...")
        latency_score, latency_time = self.memory_latency_test()
        scores['latency'] = {
            'time': round(latency_time, 3),
            'score': latency_score
        }

        memory_score = round((bandwidth_score * 0.7) + (latency_score * 0.3), 1)
        scores['score'] = memory_score

        return scores

    def memory_bandwidth_test(self):

        size = 25000000

        start_time = time.time()

        arr1 = np.ones(size, dtype=np.float32)

        arr2 = np.zeros(size, dtype=np.float32)
        arr2[:] = arr1[:]
        arr2 += 1.0
        result = np.sum(arr2)

        total_time = time.time() - start_time

        bytes_processed = size * 4 * 4
        bandwidth_mbps = (bytes_processed / (1024 * 1024)) / total_time

        bandwidth_score = self.calculate_bandwidth_score(bandwidth_mbps, self.reference_scores['memory_bandwidth'])

        return bandwidth_score, bandwidth_mbps

    def memory_latency_test(self):

        size = 5000000
        arr = np.arange(size, dtype=np.int32)
        np.random.shuffle(arr)

        start_time = time.time()

        total = 0
        for i in range(50000):
            if not self.is_running:
                break
            idx = arr[i % len(arr)]
            total += arr[idx % len(arr)]

        latency_time = time.time() - start_time

        latency_score = self.calculate_score(latency_time, self.reference_scores['memory_latency'])

        return latency_score, latency_time

    def benchmark_disk_comprehensive(self):

        scores = {}

        system_drive = os.environ.get('SystemDrive', 'C:')
        test_file = os.path.join(system_drive, 'benchmark_test.tmp')

        try:

            disk_usage = psutil.disk_usage(system_drive)
            scores['total_gb'] = round(disk_usage.total / (1024**3), 2)
            scores['free_gb'] = round(disk_usage.free / (1024**3), 2)
            scores['disk_type'] = self.get_disk_type(system_drive)

            self.update_status("Testing disk sequential write...")
            write_score, write_speed = self.disk_sequential_write_test(test_file)
            scores['sequential_write'] = {
                'mbps': round(write_speed, 2),
                'score': write_score
            }

            if not self.is_running:
                return scores

            self.update_status("Testing disk sequential read...")
            read_score, read_speed = self.disk_sequential_read_test(test_file)
            scores['sequential_read'] = {
                'mbps': round(read_speed, 2),
                'score': read_score
            }

            if not self.is_running:
                return scores

            self.update_status("Testing disk random 4K performance...")
            random_score, random_iops = self.disk_random_4k_test(test_file)
            scores['random_4k'] = {
                'iops': round(random_iops, 2),
                'score': random_score
            }

            disk_score = round((write_score * 0.3) + (read_score * 0.3) + (random_score * 0.4), 1)
            scores['score'] = disk_score

        except Exception as e:
            scores['error'] = str(e)
            scores['score'] = 0
        finally:

            try:
                if os.path.exists(test_file):
                    os.remove(test_file)
            except:
                pass

        return scores

    def disk_sequential_write_test(self, test_file):

        data = os.urandom(1024 * 1024)
        total_mb = 100

        start_time = time.time()
        with open(test_file, 'wb') as f:
            for i in range(total_mb):
                if not self.is_running:
                    break
                f.write(data)
                f.flush()

                if i % 10 == 0:
                    self.update_status(f"Writing... {i}/{total_mb} MB")

        write_time = time.time() - start_time
        write_speed = total_mb / write_time if write_time > 0 else 0

        write_score = self.calculate_bandwidth_score(write_speed, self.reference_scores['disk_sequential_write'])

        return write_score, write_speed

    def disk_sequential_read_test(self, test_file):

        if not os.path.exists(test_file):
            return 0, 0

        file_size = os.path.getsize(test_file)
        total_mb = file_size / (1024 * 1024)

        start_time = time.time()
        with open(test_file, 'rb') as f:
            bytes_read = 0
            while True:
                if not self.is_running:
                    break
                chunk = f.read(1024 * 1024)
                if not chunk:
                    break
                bytes_read += len(chunk)

                if bytes_read % (10 * 1024 * 1024) == 0:
                    mb_read = bytes_read / (1024 * 1024)
                    self.update_status(f"Reading... {mb_read:.0f}/{total_mb:.0f} MB")

        read_time = time.time() - start_time
        read_speed = total_mb / read_time if read_time > 0 else 0

        read_score = self.calculate_bandwidth_score(read_speed, self.reference_scores['disk_sequential_read'])

        return read_score, read_speed

    def disk_random_4k_test(self, test_file):

        if not os.path.exists(test_file):
            return 0, 0

        file_size = os.path.getsize(test_file)
        operations = 5000

        start_time = time.time()
        with open(test_file, 'r+b') as f:
            for i in range(operations):
                if not self.is_running:
                    break

                pos = random.randint(0, max(0, file_size - 4096))
                pos = (pos // 4096) * 4096

                f.seek(pos)
                f.read(4096)

                if i % 500 == 0:
                    self.update_status(f"Random 4K... {i}/{operations} ops")

        random_time = time.time() - start_time
        random_iops = operations / random_time if random_time > 0 else 0

        random_score = self.calculate_bandwidth_score(random_iops, self.reference_scores['disk_random_4k'])

        return random_score, random_iops

    def benchmark_gpu_comprehensive(self):

        scores = {}

        try:

            gpu_info = self.get_gpu_info()
            scores['info'] = gpu_info

            self.update_status("Testing GPU graphics rendering...")
            graphics_score = self.gpu_graphics_rendering_test()

            if graphics_score > 0:
                scores['graphics_rendering'] = {
                    'score': graphics_score,
                    'method': 'OpenGL 3D Rendering'
                }
                scores['score'] = graphics_score
            else:

                self.update_status("Attempting external GPU benchmark...")
                external_score = self.try_external_gpu_benchmark()

                if external_score > 0:
                    scores['external_benchmark'] = {
                        'score': external_score,
                        'method': 'External GPU Tool'
                    }
                    scores['score'] = external_score
                else:

                    self.update_status("Using compute benchmark fallback...")
                    compute_score, compute_time = self.gpu_compute_test_realistic()
                    scores['compute'] = {
                        'time': round(compute_time, 3),
                        'score': compute_score,
                        'method': 'Matrix Operations (CPU-based fallback)'
                    }
                    scores['score'] = compute_score

            try:
                result = subprocess.run(['nvidia-smi', '--query-gpu=memory.total,memory.used',
                                        '--format=csv,noheader,nounits'],
                                      capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    lines = result.stdout.strip().split('\n')
                    if lines:
                        memory_info = lines[0].split(', ')
                        scores['memory_total_mb'] = int(memory_info[0])
                        scores['memory_used_mb'] = int(memory_info[1])
            except:
                pass

        except Exception as e:
            scores['error'] = str(e)
            scores['score'] = 0

        return scores

    def gpu_graphics_rendering_test(self):

        if not OPENGL_AVAILABLE or not PYGAME_AVAILABLE:
            self.update_status("OpenGL/Pygame not available for GPU testing...")
            return 0

        try:

            pygame.init()
            display = (800, 600)
            pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

            glu.gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
            gl.glTranslatef(0.0, 0.0, -5)

            gl.glEnable(gl.GL_DEPTH_TEST)
            gl.glEnable(gl.GL_LIGHTING)
            gl.glEnable(gl.GL_LIGHT0)

            frame_count = 0
            start_time = time.time()
            test_duration = 3.0

            self.update_status("Rendering 3D graphics...")

            while time.time() - start_time < test_duration and self.is_running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        break

                gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

                gl.glRotatef(1, 3, 1, 1)

                for i in range(15):
                    gl.glPushMatrix()
                    gl.glTranslatef(i * 0.3, 0, 0)
                    self.draw_cube()
                    gl.glPopMatrix()

                self.draw_moderate_scene()

                pygame.display.flip()
                frame_count += 1

            total_time = time.time() - start_time
            fps = frame_count / total_time if total_time > 0 else 0

            pygame.quit()

            if fps >= 120:
                score = 90 + min(10, (fps - 120) / 60 * 10)
            elif fps >= 60:
                score = 70 + (fps - 60) / 60 * 20
            elif fps >= 30:
                score = 40 + (fps - 30) / 30 * 30
            elif fps >= 15:
                score = 20 + (fps - 15) / 15 * 20
            else:
                score = fps / 15 * 20

            return min(100, max(0, round(score, 1)))

        except Exception as e:
            self.update_status(f"Graphics rendering failed: {str(e)}")
            return 0

    def draw_cube(self):

        try:
            vertices = [
                [1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1],
                [1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1]
            ]

            edges = [
                [0,1], [1,2], [2,3], [3,0],
                [4,5], [5,6], [6,7], [7,4],
                [0,4], [1,5], [2,6], [3,7]
            ]

            faces = [
                [0,1,2,3], [3,2,6,7], [7,6,5,4],
                [4,5,1,0], [1,5,6,2], [4,0,3,7]
            ]

            gl.glBegin(gl.GL_QUADS)
            for face in faces:
                for vertex in face:
                    gl.glVertex3fv(vertices[vertex])
            gl.glEnd()

        except:
            pass

    def draw_moderate_scene(self):

        try:

            for i in range(8):
                gl.glPushMatrix()
                gl.glTranslatef(math.sin(i) * 1.5, math.cos(i) * 1.5, 0)

                gl.glBegin(gl.GL_TRIANGLES)
                for j in range(0, 360, 20):
                    for k in range(0, 180, 20):

                        x1 = math.sin(math.radians(k)) * math.cos(math.radians(j)) * 0.3
                        y1 = math.sin(math.radians(k)) * math.sin(math.radians(j)) * 0.3
                        z1 = math.cos(math.radians(k)) * 0.3

                        x2 = math.sin(math.radians(k+20)) * math.cos(math.radians(j)) * 0.3
                        y2 = math.sin(math.radians(k+20)) * math.sin(math.radians(j)) * 0.3
                        z2 = math.cos(math.radians(k+20)) * 0.3

                        x3 = math.sin(math.radians(k)) * math.cos(math.radians(j+20)) * 0.3
                        y3 = math.sin(math.radians(k)) * math.sin(math.radians(j+20)) * 0.3
                        z3 = math.cos(math.radians(k)) * 0.3

                        gl.glVertex3f(x1, y1, z1)
                        gl.glVertex3f(x2, y2, z2)
                        gl.glVertex3f(x3, y3, z3)

                gl.glEnd()
                gl.glPopMatrix()

        except:
            pass

    def try_external_gpu_benchmark(self):

        external_tools = [

            ("C:\\Program Files\\FurMark\\FurMark.exe", ["/nogui", "/benchmark"]),
            ("C:\\Program Files (x86)\\FurMark\\FurMark.exe", ["/nogui", "/benchmark"]),

            ("C:\\Program Files\\Unigine\\Heaven Benchmark 4.0\\bin\\Heaven.exe", ["-benchmark"]),

            ("C:\\Program Files\\3DMark\\3DMarkCmd.exe", ["--definition=firestrike_graphics_test"]),
        ]

        for tool_path, args in external_tools:
            if os.path.exists(tool_path):
                try:
                    self.update_status(f"Running external GPU benchmark...")
                    result = subprocess.run([tool_path] + args,
                                          capture_output=True, text=True, timeout=60)

                    if result.returncode == 0:
                        return 75

                except Exception as e:
                    continue

        return 0

    def gpu_compute_test_realistic(self):

        sizes = [600, 900]
        total_time = 0

        for size in sizes:
            if not self.is_running:
                break

            self.update_status(f"Compute fallback test... {size}x{size} matrix")

            start_time = time.time()

            a = np.random.rand(size, size).astype(np.float32)
            b = np.random.rand(size, size).astype(np.float32)

            c = np.dot(a, b)

            operation_time = time.time() - start_time
            total_time += operation_time

        base_score = self.calculate_score(total_time, self.reference_scores['gpu_compute'])

        realistic_score = min(70, base_score * 0.8)

        return round(realistic_score, 1), total_time

    def get_cpu_info(self):

        info = {}
        try:
            info['cores'] = psutil.cpu_count(logical=False)
            info['threads'] = psutil.cpu_count(logical=True)
            info['frequency_mhz'] = psutil.cpu_freq().current if psutil.cpu_freq() else 0

            try:
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                    r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
                cpu_name = winreg.QueryValueEx(key, "ProcessorNameString")[0]
                winreg.CloseKey(key)
                info['name'] = cpu_name.strip()
            except:
                info['name'] = "Unknown CPU"

        except Exception as e:
            info['error'] = str(e)

        return info

    def get_gpu_info(self):

        info = {}
        try:

            result = subprocess.run(['nvidia-smi', '--query-gpu=name,driver_version,memory.total',
                                    '--format=csv,noheader,nounits'],
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                if lines:
                    gpu_data = lines[0].split(', ')
                    info['name'] = gpu_data[0]
                    info['driver'] = gpu_data[1]
                    info['memory_mb'] = gpu_data[2].replace(' MiB', '')
                    info['vendor'] = 'NVIDIA'
                    return info
        except:
            pass

        try:
            import wmi
            c = wmi.WMI()
            for gpu in c.Win32_VideoController():
                if gpu.Name and 'Microsoft' not in gpu.Name:
                    info['name'] = gpu.Name
                    info['memory_mb'] = gpu.AdapterRAM // (1024*1024) if gpu.AdapterRAM else 0
                    if 'NVIDIA' in gpu.Name.upper():
                        info['vendor'] = 'NVIDIA'
                    elif 'AMD' in gpu.Name.upper() or 'RADEON' in gpu.Name.upper():
                        info['vendor'] = 'AMD'
                    elif 'INTEL' in gpu.Name.upper():
                        info['vendor'] = 'Intel'
                    break
        except:
            info['name'] = "Unknown GPU"
            info['vendor'] = "Unknown"

        return info

    def get_memory_info(self):

        try:

            import wmi
            c = wmi.WMI()
            memory_info = []

            for memory in c.Win32_PhysicalMemory():
                if memory.Speed and memory.MemoryType:
                    speed = memory.Speed

                    memory_types = {
                        20: "DDR",
                        21: "DDR2",
                        24: "DDR3",
                        26: "DDR4",
                        30: "DDR5"
                    }
                    mem_type = memory_types.get(memory.MemoryType, "Unknown")
                    memory_info.append(f"{mem_type}-{speed}")

            if memory_info:
                return ", ".join(set(memory_info))

        except Exception as e:
            pass

        return "Unknown Memory Type"

    def get_disk_type(self, drive):

        try:
            result = subprocess.run(['powershell', '-Command',
                                    f'Get-PhysicalDisk | Where-Object {{$_.DeviceID -eq 0}} | Select-Object MediaType'],
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0 and 'SSD' in result.stdout:
                return 'SSD'
            elif result.returncode == 0 and 'HDD' in result.stdout:
                return 'HDD'
        except:
            pass
        return 'Unknown'

    def calculate_overall_score(self):

        weights = {
            'cpu': 0.30,
            'memory': 0.20,
            'disk': 0.30,
            'gpu': 0.20
        }

        total_score = 0
        total_weight = 0

        for component, weight in weights.items():
            if component in self.results and 'score' in self.results[component]:
                total_score += self.results[component]['score'] * weight
                total_weight += weight

        if total_weight > 0:
            overall_score = round(total_score / total_weight, 1)
        else:
            overall_score = 0

        return {
            'score': overall_score,
            'rating': self.get_performance_rating(overall_score),
            'timestamp': datetime.now().isoformat()
        }

    def get_performance_rating(self, score):

        if score >= 90:
            return "Excellent"
        elif score >= 75:
            return "Very Good"
        elif score >= 60:
            return "Good"
        elif score >= 45:
            return "Average"
        elif score >= 30:
            return "Below Average"
        else:
            return "Poor"

    def save_results(self):

        try:
            results_dir = "benchmark_results"
            if not os.path.exists(results_dir):
                os.makedirs(results_dir)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(results_dir, f"benchmark_{timestamp}.json")

            with open(filename, 'w') as f:
                json.dump(self.results, f, indent=2)

        except Exception as e:
            print(f"Failed to save results: {e}")

    def load_previous_results(self):

        try:
            results_dir = "benchmark_results"
            if not os.path.exists(results_dir):
                return []

            results = []
            for filename in os.listdir(results_dir):
                if filename.endswith('.json'):
                    filepath = os.path.join(results_dir, filename)
                    try:
                        with open(filepath, 'r') as f:
                            data = json.load(f)
                            results.append(data)
                    except:
                        continue

            results.sort(key=lambda x: x.get('overall', {}).get('timestamp', ''), reverse=True)
            return results[:10]

        except Exception as e:
            print(f"Failed to load previous results: {e}")
            return []

    def stop_benchmark(self):

        self.is_running = False
        self.update_status("Benchmark stopped by user")
