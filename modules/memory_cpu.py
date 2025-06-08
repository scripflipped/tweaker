import winreg
import subprocess
import os
import psutil
from typing import Dict, Any, List
from .utils import run_command_silent

class MemoryCPUBoost:

    def __init__(self):
        self.cpu_parking_key = r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583"
        self.processor_key = r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel"
        self.hyperv_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\OptionalFeatures"

    def toggle_cpu_parking(self, disable: bool) -> bool:

        success_count = 0
        total_attempts = 0

        try:
            print(f"Attempting to {'disable' if disable else 'enable'} CPU core parking...")

            try:
                total_attempts += 1
                if disable:

                    result1 = run_command_silent([
                        "powercfg", "/setacvalueindex", "scheme_current",
                        "sub_processor", "CPMINCORES", "100"
                    ])

                    result2 = run_command_silent([
                        "powercfg", "/setdcvalueindex", "scheme_current",
                        "sub_processor", "CPMINCORES", "100"
                    ])

                    result3 = run_command_silent([
                        "powercfg", "/setacvalueindex", "scheme_current",
                        "sub_processor", "CPPMAXCORES", "0"
                    ])

                    result4 = run_command_silent([
                        "powercfg", "/setdcvalueindex", "scheme_current",
                        "sub_processor", "CPPMAXCORES", "0"
                    ])
                else:

                    result1 = run_command_silent([
                        "powercfg", "/setacvalueindex", "scheme_current",
                        "sub_processor", "CPMINCORES", "5"
                    ])

                    result2 = run_command_silent([
                        "powercfg", "/setdcvalueindex", "scheme_current",
                        "sub_processor", "CPMINCORES", "5"
                    ])

                    result3 = run_command_silent([
                        "powercfg", "/setdcvalueindex", "scheme_current",
                        "sub_processor", "CPPMAXCORES", "100"
                    ])

                    result4 = run_command_silent([
                        "powercfg", "/setdcvalueindex", "scheme_current",
                        "sub_processor", "CPPMAXCORES", "100"
                    ])

                apply_result = run_command_silent(["powercfg", "/setactive", "scheme_current"])

                if all(r.returncode == 0 for r in [result1, result2, result3, result4, apply_result]):
                    success_count += 1
                    print("✅ Powercfg method successful")
                else:
                    print(f"⚠️  Powercfg method failed - return codes: {[r.returncode for r in [result1, result2, result3, result4, apply_result]]}")

            except Exception as e:
                print(f"❌ Powercfg method failed: {e}")

            try:
                total_attempts += 1
                proc_key = r"SYSTEM\CurrentControlSet\Control\PriorityControl"
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, proc_key, 0, winreg.KEY_SET_VALUE) as key:
                    if disable:

                        winreg.SetValueEx(key, "Win32PrioritySeparation", 0, winreg.REG_DWORD, 38)
                    else:

                        winreg.SetValueEx(key, "Win32PrioritySeparation", 0, winreg.REG_DWORD, 2)
                success_count += 1
                print("✅ Registry processor scheduling method successful")
            except Exception as e:
                print(f"❌ Registry processor scheduling method failed: {e}")

            try:
                total_attempts += 1
                if disable:

                    result1 = run_command_silent([
                        "powercfg", "/setacvalueindex", "scheme_current",
                        "sub_processor", "PERFBOOSTMODE", "100"
                    ])

                    result2 = run_command_silent([
                        "powercfg", "/setdcvalueindex", "scheme_current",
                        "sub_processor", "PERFBOOSTMODE", "100"
                    ])

                    result3 = run_command_silent([
                        "powercfg", "/setacvalueindex", "scheme_current",
                        "sub_processor", "PROCTHROTTLEMIN", "1"
                    ])

                    result4 = run_command_silent([
                        "powercfg", "/setdcvalueindex", "scheme_current",
                        "sub_processor", "PROCTHROTTLEMIN", "1"
                    ])

                    if all(r.returncode == 0 for r in [result1, result2, result3, result4]):
                        success_count += 1
                        print("✅ Additional power settings method successful")
                    else:
                        print(f"⚠️  Additional power settings method failed")
                else:

                    run_command_silent([
                        "powercfg", "/setacvalueindex", "scheme_current",
                        "sub_processor", "PERFBOOSTMODE", "100"
                    ])

                    run_command_silent([
                        "powercfg", "/setdcvalueindex", "scheme_current",
                        "sub_processor", "PERFBOOSTMODE", "100"
                    ])

                    success_count += 1
                    print("✅ Power settings restored to defaults")

            except Exception as e:
                print(f"❌ Additional power settings method failed: {e}")

            try:
                run_command_silent(["powercfg", "/setactive", "scheme_current"])
            except Exception:
                pass

            print(f"CPU parking operation completed: {success_count}/{total_attempts} methods successful")

            return success_count > 0

        except Exception as e:
            print(f"Error in CPU parking operation: {e}")
            return False

    def toggle_high_priority(self, enable: bool) -> bool:

        try:

            self.high_priority_enabled = enable

            if enable:

                self._start_priority_monitor()
            else:

                self._reset_game_priorities()

            return True
        except Exception as e:
            print(f"Error toggling high priority: {e}")
            return False

    def _start_priority_monitor(self):

        game_processes = [
            "csgo.exe", "valorant.exe", "fortnite.exe", "apex.exe",
            "overwatch.exe", "league of legends.exe", "dota2.exe",
            "pubg.exe", "cod.exe", "battlefield.exe", "gta5.exe",
            "minecraft.exe", "steam.exe"
        ]

        try:
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    if proc.info['name'].lower() in [g.lower() for g in game_processes]:
                        process = psutil.Process(proc.info['pid'])
                        process.nice(psutil.HIGH_PRIORITY_CLASS)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
        except Exception as e:
            print(f"Error setting game priorities: {e}")

    def _reset_game_priorities(self):

        try:
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    process = psutil.Process(proc.info['pid'])
                    if process.nice() == psutil.HIGH_PRIORITY_CLASS:
                        process.nice(psutil.NORMAL_PRIORITY_CLASS)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
        except Exception as e:
            print(f"Error resetting priorities: {e}")

    def toggle_hyperv(self, disable: bool) -> bool:

        try:
            if disable:

                result = run_command_silent([
                    "dism", "/online", "/disable-feature",
                    "/featurename:Microsoft-Hyper-V-All", "/norestart"
                ])

                run_command_silent([
                    "bcdedit", "/set", "hypervisorlaunchtype", "off"
                ])
            else:

                result = run_command_silent([
                    "dism", "/online", "/enable-feature",
                    "/featurename:Microsoft-Hyper-V-All", "/norestart"
                ])

                run_command_silent([
                    "bcdedit", "/set", "hypervisorlaunchtype", "auto"
                ])

            return True
        except Exception as e:
            print(f"Error toggling Hyper-V: {e}")
            return False

    def optimize_memory_settings(self) -> bool:

        try:

            memory_key = r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management"
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, memory_key, 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, "DisablePagingExecutive", 0, winreg.REG_DWORD, 1)
                winreg.SetValueEx(key, "LargeSystemCache", 0, winreg.REG_DWORD, 0)

                winreg.SetValueEx(key, "SystemCacheLimit", 0, winreg.REG_DWORD, 0)
                winreg.SetValueEx(key, "SecondLevelDataCache", 0, winreg.REG_DWORD, 1024)
                winreg.SetValueEx(key, "ThirdLevelDataCache", 0, winreg.REG_DWORD, 8192)

            try:

                winreg.SetValueEx(key, "ClearPageFileAtShutdown", 0, winreg.REG_DWORD, 0)
            except Exception:
                pass

            return True
        except Exception as e:
            print(f"Error optimizing memory settings: {e}")
            return False

    def set_processor_affinity(self, process_name: str, cpu_cores: List[int]) -> bool:

        try:
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    if proc.info['name'].lower() == process_name.lower():
                        process = psutil.Process(proc.info['pid'])
                        process.cpu_affinity(cpu_cores)
                        return True
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            return False
        except Exception as e:
            print(f"Error setting processor affinity: {e}")
            return False

    def optimize_cpu_settings(self) -> bool:

        try:

            cpu_key = r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\893dee8e-2bef-41e0-89c6-b55d0929964c"
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, cpu_key, 0, winreg.KEY_SET_VALUE) as key:
                    winreg.SetValueEx(key, "ValueMax", 0, winreg.REG_DWORD, 100)
                    winreg.SetValueEx(key, "ValueMin", 0, winreg.REG_DWORD, 100)
            except Exception:
                pass

            boost_key = r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\be337238-0d82-4146-a960-4f3749d470c7"
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, boost_key, 0, winreg.KEY_SET_VALUE) as key:
                    winreg.SetValueEx(key, "ValueMax", 0, winreg.REG_DWORD, 100)
            except Exception:
                pass

            try:
                run_command_silent([
                    "powercfg", "/setacvalueindex", "scheme_current",
                    "sub_processor", "PERFBOOSTMODE", "0"
                ])
            except Exception:
                pass

            return True
        except Exception as e:
            print(f"Error optimizing CPU settings: {e}")
            return False

    def get_cpu_info(self) -> Dict[str, Any]:

        cpu_info = {
            'name': 'Unknown',
            'cores': 0,
            'threads': 0,
            'frequency': 0,
            'usage': 0
        }

        try:

            result = run_command_silent([
                "wmic", "cpu", "get", "name", "/format:value"
            ])

            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if line.startswith('Name='):
                        cpu_info['name'] = line.split('=', 1)[1].strip()
                        break

            cpu_info['cores'] = psutil.cpu_count(logical=False)
            cpu_info['threads'] = psutil.cpu_count(logical=True)

            freq = psutil.cpu_freq()
            if freq:
                cpu_info['frequency'] = freq.current

            cpu_info['usage'] = psutil.cpu_percent(interval=1)

        except Exception as e:
            print(f"Error getting CPU info: {e}")

        return cpu_info

    def get_memory_info(self) -> Dict[str, Any]:

        memory_info = {
            'total': 0,
            'available': 0,
            'used': 0,
            'percentage': 0
        }

        try:
            memory = psutil.virtual_memory()
            memory_info['total'] = memory.total / (1024**3)
            memory_info['available'] = memory.available / (1024**3)
            memory_info['used'] = memory.used / (1024**3)
            memory_info['percentage'] = memory.percent

        except Exception as e:
            print(f"Error getting memory info: {e}")

        return memory_info

    def clear_memory_cache(self) -> bool:

        try:

            try:
                import ctypes
                from ctypes import wintypes

                SYSTEM_MEMORY_LIST_INFORMATION = 80
                MemoryPurgeStandbyList = 4

                ntdll = ctypes.windll.ntdll

                result = ntdll.NtSetSystemInformation(
                    SYSTEM_MEMORY_LIST_INFORMATION,
                    ctypes.byref(ctypes.c_int(MemoryPurgeStandbyList)),
                    ctypes.sizeof(ctypes.c_int)
                )

                return result == 0
            except Exception:
                pass

            try:
                ps_command = """
                [System.GC]::Collect()
                [System.GC]::WaitForPendingFinalizers()
                [System.GC]::Collect()
                """
                run_command_silent([
                    "powershell", "-Command", ps_command
                ])
                return True
            except Exception:
                pass

            return False
        except Exception as e:
            print(f"Error clearing memory cache: {e}")
            return False

    def set_game_priority_realtime(self, process_name: str) -> bool:

        try:
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    if proc.info['name'].lower() == process_name.lower():
                        process = psutil.Process(proc.info['pid'])
                        process.nice(psutil.REALTIME_PRIORITY_CLASS)
                        return True
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            return False
        except Exception as e:
            print(f"Error setting realtime priority: {e}")
            return False

    def get_cpu_parking_status(self) -> Dict[str, Any]:

        status = {
            'parking_enabled': True,
            'min_cores': 'Unknown',
            'max_cores': 'Unknown',
            'current_scheme': 'Unknown',
            'processor_state_min': 'Unknown',
            'processor_state_max': 'Unknown'
        }

        try:

            result = run_command_silent(["powercfg", "/getactivescheme"])
            if result.returncode != 0:
                return status

            status['current_scheme'] = result.stdout.strip()

            try:
                result = run_command_silent([
                    "powercfg", "/query", "scheme_current",
                    "sub_processor", "CPMINCORES"
                ])

                if result.returncode == 0:
                    output = result.stdout

                    lines = output.split('\n')
                    for line in lines:
                        if 'Current AC Power Setting Index:' in line:
                            value = line.split(':')[-1].strip()
                            if value.startswith('0x'):
                                status['min_cores'] = str(int(value, 16))
                            else:
                                status['min_cores'] = value
                        elif 'Current DC Power Setting Index:' in line:
                            value = line.split(':')[-1].strip()
                            if value.startswith('0x'):
                                status['max_cores'] = str(int(value, 16))
                            else:
                                status['max_cores'] = value
            except Exception as e:
                print(f"Error checking core parking: {e}")

            try:
                result = run_command_silent([
                    "powercfg", "/query", "scheme_current",
                    "sub_processor", "PROCTHROTTLEMIN"
                ])

                if result.returncode == 0:
                    output = result.stdout
                    lines = output.split('\n')
                    for line in lines:
                        if 'Current AC Power Setting Index:' in line:
                            value = line.split(':')[-1].strip()
                            if value.startswith('0x'):
                                status['processor_state_min'] = str(int(value, 16)) + '%'
                            else:
                                status['processor_state_min'] = value + '%'
            except Exception as e:
                print(f"Error checking processor state: {e}")

            try:
                min_cores_val = int(status['min_cores']) if status['min_cores'].isdigit() else 100
                min_state_val = int(status['processor_state_min'].replace('%', '')) if status['processor_state_min'].replace('%', '').isdigit() else 5

                status['parking_enabled'] = not (min_cores_val == 0 or min_state_val >= 100)
            except Exception:
                pass

        except Exception as e:
            print(f"Error getting CPU parking status: {e}")

        return status
