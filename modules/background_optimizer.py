import winreg
import subprocess
import os
import psutil
from typing import List, Dict, Any

class BackgroundOptimizer:

    def __init__(self):
        self.startup_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        self.telemetry_keys = [
            r"SOFTWARE\Policies\Microsoft\Windows\DataCollection",
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection",
            r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags"
        ]
        self.update_key = r"SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"

    def get_startup_apps(self) -> List[Dict[str, Any]]:

        startup_apps = []

        try:

            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.startup_key) as key:
                i = 0
                while True:
                    try:
                        name, value, _ = winreg.EnumValue(key, i)
                        startup_apps.append({
                            'name': name,
                            'path': value,
                            'enabled': True,
                            'location': 'HKCU'
                        })
                        i += 1
                    except WindowsError:
                        break
        except Exception:
            pass

        try:

            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.startup_key) as key:
                i = 0
                while True:
                    try:
                        name, value, _ = winreg.EnumValue(key, i)
                        startup_apps.append({
                            'name': name,
                            'path': value,
                            'enabled': True,
                            'location': 'HKLM'
                        })
                        i += 1
                    except WindowsError:
                        break
        except Exception:
            pass

        try:
            result = subprocess.run([
                "schtasks", "/query", "/fo", "csv"
            ], capture_output=True, text=True, check=False)

            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                for line in lines[1:]:
                    if 'Ready' in line and 'Microsoft' not in line:
                        parts = line.split(',')
                        if len(parts) > 0:
                            task_name = parts[0].strip('"')
                            startup_apps.append({
                                'name': task_name,
                                'path': 'Task Scheduler',
                                'enabled': True,
                                'location': 'TASK'
                            })
        except Exception:
            pass

        return startup_apps

    def toggle_startup_app(self, app: Dict[str, Any], enable: bool) -> bool:

        try:
            if app['location'] == 'HKCU':
                hkey = winreg.HKEY_CURRENT_USER
            elif app['location'] == 'HKLM':
                hkey = winreg.HKEY_LOCAL_MACHINE
            else:
                return False

            if enable:

                with winreg.OpenKey(hkey, self.startup_key, 0, winreg.KEY_SET_VALUE) as key:
                    winreg.SetValueEx(key, app['name'], 0, winreg.REG_SZ, app['path'])
            else:

                with winreg.OpenKey(hkey, self.startup_key, 0, winreg.KEY_SET_VALUE) as key:
                    try:
                        winreg.DeleteValue(key, app['name'])
                    except FileNotFoundError:
                        pass

            return True
        except Exception as e:
            print(f"Error toggling startup app {app['name']}: {e}")
            return False

    def toggle_telemetry(self, disable: bool) -> bool:

        try:

            for key_path in self.telemetry_keys:
                try:
                    with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
                        if "DataCollection" in key_path:
                            winreg.SetValueEx(key, "AllowTelemetry", 0, winreg.REG_DWORD, 0 if disable else 1)
                            winreg.SetValueEx(key, "MaxTelemetryAllowed", 0, winreg.REG_DWORD, 0 if disable else 3)
                        elif "AppCompat" in key_path:
                            winreg.SetValueEx(key, "AITEnable", 0, winreg.REG_DWORD, 0 if disable else 1)
                            winreg.SetValueEx(key, "DisableInventory", 0, winreg.REG_DWORD, 1 if disable else 0)
                except Exception:
                    pass

            wer_key = r"SOFTWARE\Microsoft\Windows\Windows Error Reporting"
            try:
                with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, wer_key) as key:
                    winreg.SetValueEx(key, "Disabled", 0, winreg.REG_DWORD, 1 if disable else 0)
            except Exception:
                pass

            ceip_key = r"SOFTWARE\Microsoft\SQMClient\Windows"
            try:
                with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, ceip_key) as key:
                    winreg.SetValueEx(key, "CEIPEnable", 0, winreg.REG_DWORD, 0 if disable else 1)
            except Exception:
                pass

            adv_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo"
            try:
                with winreg.CreateKey(winreg.HKEY_CURRENT_USER, adv_key) as key:
                    winreg.SetValueEx(key, "Enabled", 0, winreg.REG_DWORD, 0 if disable else 1)
            except Exception:
                pass

            return True
        except Exception as e:
            print(f"Error toggling telemetry: {e}")
            return False

    def toggle_background_apps(self, disable: bool) -> bool:

        try:

            bg_apps_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications"
            try:
                with winreg.CreateKey(winreg.HKEY_CURRENT_USER, bg_apps_key) as key:
                    winreg.SetValueEx(key, "GlobalUserDisabled", 0, winreg.REG_DWORD, 1 if disable else 0)
            except Exception:
                pass

            common_bg_apps = [
                "Microsoft.Windows.Photos_8wekyb3d8bbwe",
                "Microsoft.SkypeApp_kzf8qxf38zg5c",
                "Microsoft.GetHelp_8wekyb3d8bbwe",
                "Microsoft.Getstarted_8wekyb3d8bbwe",
                "Microsoft.MicrosoftOfficeHub_8wekyb3d8bbwe",
                "Microsoft.OneConnect_8wekyb3d8bbwe",
                "Microsoft.People_8wekyb3d8bbwe",
                "Microsoft.BingFinance_8wekyb3d8bbwe",
                "Microsoft.BingNews_8wekyb3d8bbwe"
            ]

            for app in common_bg_apps:
                try:
                    app_key = f"{bg_apps_key}\\{app}"
                    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, app_key) as key:
                        winreg.SetValueEx(key, "Disabled", 0, winreg.REG_DWORD, 1 if disable else 0)
                except Exception:
                    pass

            return True
        except Exception as e:
            print(f"Error toggling background apps: {e}")
            return False

    def toggle_auto_updates(self, disable: bool) -> bool:

        try:

            with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, self.update_key) as key:
                if disable:

                    winreg.SetValueEx(key, "NoAutoUpdate", 0, winreg.REG_DWORD, 1)
                    winreg.SetValueEx(key, "AUOptions", 0, winreg.REG_DWORD, 2)
                    winreg.SetValueEx(key, "ScheduledInstallDay", 0, winreg.REG_DWORD, 0)
                    winreg.SetValueEx(key, "ScheduledInstallTime", 0, winreg.REG_DWORD, 3)
                else:

                    winreg.SetValueEx(key, "NoAutoUpdate", 0, winreg.REG_DWORD, 0)
                    winreg.SetValueEx(key, "AUOptions", 0, winreg.REG_DWORD, 4)

            if disable:
                try:
                    subprocess.run([
                        "sc", "config", "wuauserv", "start=", "disabled"
                    ], capture_output=True, check=False)
                except Exception:
                    pass
            else:
                try:
                    subprocess.run([
                        "sc", "config", "wuauserv", "start=", "auto"
                    ], capture_output=True, check=False)
                except Exception:
                    pass

            return True
        except Exception as e:
            print(f"Error toggling auto updates: {e}")
            return False

    def disable_unnecessary_services(self) -> bool:

        services_to_disable = [
            "Fax",
            "TapiSrv",
            "WSearch",
            "DiagTrack",
            "dmwappushservice",
            "RetailDemo",
            "WMPNetworkSvc",
            "RemoteRegistry",
            "Spooler"
        ]

        try:
            for service in services_to_disable:
                try:

                    subprocess.run([
                        "sc", "stop", service
                    ], capture_output=True, check=False)

                    subprocess.run([
                        "sc", "config", service, "start=", "disabled"
                    ], capture_output=True, check=False)
                except Exception:
                    pass

            return True
        except Exception as e:
            print(f"Error disabling services: {e}")
            return False

    def get_running_processes(self) -> List[Dict[str, Any]]:

        processes = []

        try:
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    proc_info = proc.info
                    if proc_info['cpu_percent'] > 0 or proc_info['memory_percent'] > 1:
                        processes.append({
                            'pid': proc_info['pid'],
                            'name': proc_info['name'],
                            'cpu_percent': proc_info['cpu_percent'],
                            'memory_percent': proc_info['memory_percent']
                        })
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
        except Exception as e:
            print(f"Error getting processes: {e}")

        return sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)

    def kill_process(self, pid: int) -> bool:

        try:
            proc = psutil.Process(pid)
            proc.terminate()
            return True
        except Exception as e:
            print(f"Error killing process {pid}: {e}")
            return False

    def run_disk_cleanup(self) -> tuple[bool, str]:

        try:
            import subprocess

            cleanup_command = [
                "cleanmgr", "/sagerun:1"
            ]

            try:

                cleanup_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches"
                cleanup_options = [
                    "Temporary Files",
                    "Downloaded Program Files",
                    "Recycle Bin",
                    "Temporary Internet Files",
                    "Thumbnail Cache",
                    "Old Chkdsk Files",
                    "System error memory dump files",
                    "Windows Error Reporting Archive Files",
                    "Windows Error Reporting Queue Files",
                    "Windows Error Reporting System Archive Files",
                    "Windows Error Reporting System Queue Files",
                    "Windows Update Cleanup",
                    "Windows Upgrade Log Files"
                ]

                for option in cleanup_options:
                    try:
                        option_key = f"{cleanup_key}\\{option}"
                        with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, option_key) as key:
                            winreg.SetValueEx(key, "StateFlags0001", 0, winreg.REG_DWORD, 2)
                    except Exception:
                        pass

            except Exception:
                pass

            result = subprocess.run(cleanup_command, capture_output=True, text=True, timeout=300)

            if result.returncode == 0:
                return True, "Disk cleanup completed successfully"
            else:

                try:

                    ps_command = """
                    Get-ChildItem -Path $env:TEMP -Recurse | Remove-Item -Force -Recurse -ErrorAction SilentlyContinue
                    Get-ChildItem -Path "$env:LOCALAPPDATA\\Temp" -Recurse | Remove-Item -Force -Recurse -ErrorAction SilentlyContinue
                    Get-ChildItem -Path "$env:WINDIR\\Temp" -Recurse | Remove-Item -Force -Recurse -ErrorAction SilentlyContinue
                    """

                    ps_result = subprocess.run([
                        "powershell", "-Command", ps_command
                    ], capture_output=True, text=True, timeout=120)

                    return True, "Temporary files cleaned using PowerShell"

                except Exception:
                    return False, f"Disk cleanup failed: {result.stderr}"

        except Exception as e:
            return False, f"Error running disk cleanup: {str(e)}"

    def clear_event_logs(self) -> tuple[bool, str]:

        try:
            import subprocess

            event_logs = [
                "Application",
                "Security",
                "System",
                "Setup",
                "Microsoft-Windows-Sysmon/Operational",
                "Microsoft-Windows-Windows Defender/Operational",
                "Microsoft-Windows-PowerShell/Operational",
                "Microsoft-Windows-TaskScheduler/Operational"
            ]

            cleared_logs = []
            failed_logs = []

            for log in event_logs:
                try:

                    result = subprocess.run([
                        "wevtutil", "cl", log
                    ], capture_output=True, text=True, check=True)

                    cleared_logs.append(log)

                except subprocess.CalledProcessError:
                    failed_logs.append(log)
                except Exception:
                    failed_logs.append(log)

            if cleared_logs:
                success_msg = f"Successfully cleared {len(cleared_logs)} event logs:\n"
                success_msg += "\n".join([f"• {log}" for log in cleared_logs])

                if failed_logs:
                    success_msg += f"\n\nFailed to clear {len(failed_logs)} logs (may require higher privileges)"

                return True, success_msg
            else:
                return False, "No event logs could be cleared. Administrator privileges may be required."

        except Exception as e:
            return False, f"Error clearing event logs: {str(e)}"

    def optimize_drives(self) -> tuple[bool, str]:

        try:
            import subprocess
            import psutil

            drives = []
            for partition in psutil.disk_partitions():
                if 'fixed' in partition.opts:
                    drives.append(partition.device[0])

            if not drives:
                return False, "No fixed drives found to optimize"

            optimized_drives = []
            failed_drives = []

            for drive in drives:
                try:

                    result = subprocess.run([
                        "defrag", f"{drive}:", "/O"
                    ], capture_output=True, text=True, timeout=1800)

                    if result.returncode == 0:
                        optimized_drives.append(f"Drive {drive}: (Optimized)")
                    else:

                        analyze_result = subprocess.run([
                            "defrag", f"{drive}:", "/A"
                        ], capture_output=True, text=True, timeout=300)

                        if analyze_result.returncode == 0:
                            optimized_drives.append(f"Drive {drive}: (Analyzed)")
                        else:
                            failed_drives.append(f"Drive {drive}:")

                except subprocess.TimeoutExpired:
                    failed_drives.append(f"Drive {drive}: (Timeout)")
                except Exception:
                    failed_drives.append(f"Drive {drive}: (Error)")

            if optimized_drives:
                success_msg = f"Drive optimization completed:\n"
                success_msg += "\n".join([f"✅ {drive}" for drive in optimized_drives])

                if failed_drives:
                    success_msg += f"\n\nSome drives could not be optimized:\n"
                    success_msg += "\n".join([f"❌ {drive}" for drive in failed_drives])

                return True, success_msg
            else:
                return False, "No drives could be optimized. This may take a while for large drives."

        except Exception as e:
            return False, f"Error optimizing drives: {str(e)}"
