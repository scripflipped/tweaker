import subprocess
import winreg
import psutil
import ctypes
import sys
from typing import Dict, List, Tuple, Optional

class AdvancedOptimizer:
    def __init__(self):
        self.is_admin = self._check_admin_privileges()

    def _check_admin_privileges(self) -> bool:

        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def _run_command(self, command: str, shell: bool = True) -> Tuple[bool, str]:

        try:
            result = subprocess.run(command, shell=shell, capture_output=True, text=True, timeout=30)
            return result.returncode == 0, result.stdout + result.stderr
        except Exception as e:
            return False, str(e)

    def _set_registry_value(self, key_path: str, value_name: str, value_data, value_type: int) -> bool:

        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, value_name, 0, value_type, value_data)
            winreg.CloseKey(key)
            return True
        except Exception as e:
            try:

                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(key, value_name, 0, value_type, value_data)
                winreg.CloseKey(key)
                return True
            except:
                return False

    def optimize_process_priorities(self) -> Dict[str, bool]:

        if not self.is_admin:
            return {"error": "Administrator privileges required"}

        results = {}

        high_priority_services = [
            "Themes",
            "AudioSrv",
            "MMCSS",
            "Schedule",
            "Spooler",
            "UxSms",
            "WinDefend",
            "Dhcp",
            "Dnscache"
        ]

        low_priority_services = [
            "Fax",
            "TabletInputService",
            "WSearch",
            "SysMain",
            "WMPNetworkSvc",
            "RemoteRegistry",
            "TrkWks",
            "WbioSrvc",
            "Wlansvc",
            "WlanSvc",
            "DiagTrack",
            "dmwappushservice"
        ]

        for service in high_priority_services:
            try:

                success, output = self._run_command(f'sc queryex "{service}"')
                if success and "PID" in output:

                    for line in output.split('\n'):
                        if 'PID' in line:
                            pid = line.split(':')[-1].strip()
                            if pid.isdigit():

                                success, _ = self._run_command(f'wmic process where ProcessId={pid} CALL setpriority "high"')
                                results[f"{service}_high"] = success
                                break
            except Exception as e:
                results[f"{service}_high"] = False

        for service in low_priority_services:
            try:
                success, output = self._run_command(f'sc queryex "{service}"')
                if success and "PID" in output:
                    for line in output.split('\n'):
                        if 'PID' in line:
                            pid = line.split(':')[-1].strip()
                            if pid.isdigit():
                                success, _ = self._run_command(f'wmic process where ProcessId={pid} CALL setpriority "low"')
                                results[f"{service}_low"] = success
                                break
            except Exception as e:
                results[f"{service}_low"] = False

        return results

    def optimize_mouse_settings(self) -> Dict[str, bool]:

        results = {}

        mouse_tweaks = [

            ("Control Panel\\Mouse", "MouseSpeed", "0", winreg.REG_SZ),
            ("Control Panel\\Mouse", "MouseThreshold1", "0", winreg.REG_SZ),
            ("Control Panel\\Mouse", "MouseThreshold2", "0", winreg.REG_SZ),

            ("Control Panel\\Mouse", "MouseSensitivity", "10", winreg.REG_SZ),
            ("Control Panel\\Mouse", "MouseHoverTime", "8", winreg.REG_SZ),

            ("SYSTEM\\CurrentControlSet\\Services\\mouclass\\Parameters", "MouseDataQueueSize", 20, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Services\\mouclass\\Parameters", "ThreadPriority", 31, winreg.REG_DWORD),
        ]

        for key_path, value_name, value_data, value_type in mouse_tweaks:
            success = self._set_registry_value(key_path, value_name, value_data, value_type)
            results[f"mouse_{value_name}"] = success

        try:
            smooth_x_curve = bytes([
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0xC0, 0xCC, 0x0C, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x08, 0x09, 0x91, 0x90, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x04, 0x06, 0x62, 0x60, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x33, 0x33, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
            ])

            smooth_y_curve = bytes([
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x38, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x70, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0xA8, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0xE0, 0x00, 0x00, 0x00, 0x00, 0x00
            ])

            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Mouse", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "SmoothMouseXCurve", 0, winreg.REG_BINARY, smooth_x_curve)
            winreg.SetValueEx(key, "SmoothMouseYCurve", 0, winreg.REG_BINARY, smooth_y_curve)
            winreg.CloseKey(key)
            results["mouse_curves"] = True
        except Exception as e:
            results["mouse_curves"] = False

        return results

    def optimize_keyboard_settings(self) -> Dict[str, bool]:

        results = {}

        keyboard_tweaks = [

            ("Control Panel\\Keyboard", "KeyboardDelay", "0", winreg.REG_SZ),
            ("Control Panel\\Keyboard", "KeyboardSpeed", "31", winreg.REG_SZ),
            ("Control Panel\\Keyboard", "InitialKeyboardIndicators", "0", winreg.REG_SZ),

            ("Control Panel\\Accessibility\\StickyKeys", "Flags", "506", winreg.REG_SZ),
            ("Control Panel\\Accessibility\\ToggleKeys", "Flags", "58", winreg.REG_SZ),
            ("Control Panel\\Accessibility\\MouseKeys", "Flags", "38", winreg.REG_SZ),

            ("Control Panel\\Accessibility\\Keyboard Response", "AutoRepeatDelay", "200", winreg.REG_SZ),
            ("Control Panel\\Accessibility\\Keyboard Response", "AutoRepeatRate", "6", winreg.REG_SZ),
            ("Control Panel\\Accessibility\\Keyboard Response", "BounceTime", "0", winreg.REG_SZ),
            ("Control Panel\\Accessibility\\Keyboard Response", "DelayBeforeAcceptance", "0", winreg.REG_SZ),
            ("Control Panel\\Accessibility\\Keyboard Response", "Flags", "59", winreg.REG_SZ),
        ]

        for key_path, value_name, value_data, value_type in keyboard_tweaks:

            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(key, value_name, 0, value_type, value_data)
                winreg.CloseKey(key)
                results[f"keyboard_{value_name}"] = True
            except Exception as e:
                results[f"keyboard_{value_name}"] = False

        return results

    def optimize_memory_management(self) -> Dict[str, bool]:

        results = {}

        memory_tweaks = [

            ("SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management", "ClearPageFileAtShutdown", 1, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management", "LargeSystemCache", 0, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management", "DisablePagingExecutive", 1, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management", "IoPageLockLimit", 1048576, winreg.REG_DWORD),

            ("SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management", "FeatureSettingsOverride", 3, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management", "FeatureSettingsOverrideMask", 3, winreg.REG_DWORD),

            ("SYSTEM\\CurrentControlSet\\Control\\Power", "EnergyEstimationEnabled", 0, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Control\\Power", "EventProcessorEnabled", 0, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Control\\Power\\PowerThrottling", "PowerThrottlingOff", 1, winreg.REG_DWORD),

            ("SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Power", "CoalescingTimerInterval", 0, winreg.REG_DWORD),

            ("SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel", "DistributeTimers", 1, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel", "DisableTsx", 0, winreg.REG_DWORD),
        ]

        for key_path, value_name, value_data, value_type in memory_tweaks:
            success = self._set_registry_value(key_path, value_name, value_data, value_type)
            results[f"memory_{value_name}"] = success

        return results

    def optimize_network_settings(self) -> Dict[str, bool]:

        results = {}

        tcp_tweaks = [
            ("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", "EnableICMPRedirect", 1, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", "EnablePMTUDiscovery", 1, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", "Tcp1323Opts", 0, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", "TcpMaxDupAcks", 2, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", "TcpTimedWaitDelay", 32, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", "GlobalMaxTcpWindowSize", 8760, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", "TcpWindowSize", 8760, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", "MaxConnectionsPerServer", 0, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", "MaxUserPort", 65534, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", "SackOpts", 0, winreg.REG_DWORD),
            ("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", "DefaultTTL", 64, winreg.REG_DWORD),
        ]

        for key_path, value_name, value_data, value_type in tcp_tweaks:
            success = self._set_registry_value(key_path, value_name, value_data, value_type)
            results[f"tcp_{value_name}"] = success

        msmq_success = self._set_registry_value(
            "SYSTEM\\CurrentControlSet\\Services\\MSMQ\\Parameters",
            "TCPNoDelay",
            1,
            winreg.REG_DWORD
        )
        results["msmq_tcpnodelay"] = msmq_success

        rss_tweaks = [
            ("SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0001", "*RSSProfile", "3", winreg.REG_SZ),
        ]

        for key_path, value_name, value_data, value_type in rss_tweaks:
            success = self._set_registry_value(key_path, value_name, value_data, value_type)
            results[f"rss_{value_name}"] = success

        try:

            adapters = psutil.net_if_addrs()
            adapter_count = 0
            for adapter_name in adapters:
                if adapter_name != "Loopback Pseudo-Interface 1":
                    adapter_count += 1

                    adapter_key = f"SYSTEM\\CurrentControlSet\\Control\\Class\\{{4d36e972-e325-11ce-bfc1-08002be10318}}\\{adapter_count:04d}"
                    success = self._set_registry_value(adapter_key, "*RSSProfile", "3", winreg.REG_SZ)
                    results[f"adapter_{adapter_count}_rss"] = success
        except Exception as e:
            results["adapter_enumeration"] = False

        return results

    def run_all_optimizations(self) -> Dict[str, Dict[str, bool]]:

        all_results = {}

        print("Running Process Priority Optimization...")
        all_results["process_priorities"] = self.optimize_process_priorities()

        print("Running Mouse Settings Optimization...")
        all_results["mouse_settings"] = self.optimize_mouse_settings()

        print("Running Keyboard Settings Optimization...")
        all_results["keyboard_settings"] = self.optimize_keyboard_settings()

        print("Running Advanced Memory Management...")
        all_results["memory_management"] = self.optimize_memory_management()

        print("Running Network Optimizations...")
        all_results["network_settings"] = self.optimize_network_settings()

        return all_results

    def get_optimization_summary(self, results: Dict[str, Dict[str, bool]]) -> str:

        summary = "Advanced Optimization Results:\n\n"

        for category, category_results in results.items():
            if isinstance(category_results, dict):
                successful = sum(1 for v in category_results.values() if v is True)
                total = len(category_results)
                summary += f"{category.replace('_', ' ').title()}: {successful}/{total} successful\n"

                failed_items = [k for k, v in category_results.items() if v is False]
                if failed_items:
                    summary += f"  Failed: {', '.join(failed_items)}\n"
            else:
                summary += f"{category}: {category_results}\n"

        return summary
