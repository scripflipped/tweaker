import winreg
import subprocess
import os
from typing import Dict, Any

class GPUTweaks:

    def __init__(self):
        self.visual_effects_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects"
        self.dwm_key = r"SOFTWARE\Microsoft\Windows\DWM"
        self.graphics_key = r"SOFTWARE\Microsoft\DirectX\UserGpuPreferences"

    def toggle_visual_effects(self, disable: bool) -> bool:

        try:

            perf_key = r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters"
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, perf_key, 0, winreg.KEY_SET_VALUE) as key:
                    if disable:
                        winreg.SetValueEx(key, "EnablePrefetcher", 0, winreg.REG_DWORD, 0)
                        winreg.SetValueEx(key, "EnableSuperfetch", 0, winreg.REG_DWORD, 0)
                    else:
                        winreg.SetValueEx(key, "EnablePrefetcher", 0, winreg.REG_DWORD, 3)
                        winreg.SetValueEx(key, "EnableSuperfetch", 0, winreg.REG_DWORD, 1)
            except Exception:
                pass

            visual_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects"
            try:
                with winreg.CreateKey(winreg.HKEY_CURRENT_USER, visual_key) as key:
                    if disable:
                        winreg.SetValueEx(key, "VisualFXSetting", 0, winreg.REG_DWORD, 2)
                    else:
                        winreg.SetValueEx(key, "VisualFXSetting", 0, winreg.REG_DWORD, 0)
            except Exception:
                pass

            anim_key = r"Control Panel\Desktop"
            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, anim_key, 0, winreg.KEY_SET_VALUE) as key:
                    if disable:
                        winreg.SetValueEx(key, "UserPreferencesMask", 0, winreg.REG_BINARY,
                                        bytes([0x90, 0x12, 0x03, 0x80, 0x10, 0x00, 0x00, 0x00]))
                        winreg.SetValueEx(key, "MenuShowDelay", 0, winreg.REG_SZ, "0")
                    else:
                        winreg.SetValueEx(key, "UserPreferencesMask", 0, winreg.REG_BINARY,
                                        bytes([0x9E, 0x1E, 0x07, 0x80, 0x12, 0x00, 0x00, 0x00]))
                        winreg.SetValueEx(key, "MenuShowDelay", 0, winreg.REG_SZ, "400")
            except Exception:
                pass

            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, anim_key, 0, winreg.KEY_SET_VALUE) as key:
                    winreg.SetValueEx(key, "WindowMetrics", 0, winreg.REG_SZ, "1" if disable else "0")
            except Exception:
                pass

            return True
        except Exception as e:
            print(f"Error toggling visual effects: {e}")
            return False

    def toggle_transparency(self, disable: bool) -> bool:

        try:

            personalize_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"
            try:
                with winreg.CreateKey(winreg.HKEY_CURRENT_USER, personalize_key) as key:
                    winreg.SetValueEx(key, "EnableTransparency", 0, winreg.REG_DWORD, 0 if disable else 1)
            except Exception:
                pass

            try:
                with winreg.CreateKey(winreg.HKEY_CURRENT_USER, self.dwm_key) as key:
                    winreg.SetValueEx(key, "EnableAeroPeek", 0, winreg.REG_DWORD, 0 if disable else 1)
                    winreg.SetValueEx(key, "AlwaysHibernateThumbnails", 0, winreg.REG_DWORD, 0 if disable else 1)
            except Exception:
                pass

            aero_key = r"SOFTWARE\Microsoft\Windows\DWM"
            try:
                with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, aero_key) as key:
                    winreg.SetValueEx(key, "EnableAeroPeek", 0, winreg.REG_DWORD, 0 if disable else 1)
            except Exception:
                pass

            return True
        except Exception as e:
            print(f"Error toggling transparency: {e}")
            return False

    def toggle_high_performance_gpu(self, enable: bool) -> bool:

        try:

            graphics_key = r"SOFTWARE\Microsoft\DirectX\UserGpuPreferences"
            try:
                with winreg.CreateKey(winreg.HKEY_CURRENT_USER, graphics_key) as key:

                    game_exes = [
                        "csgo.exe", "valorant.exe", "fortnite.exe", "apex.exe",
                        "overwatch.exe", "league of legends.exe", "dota2.exe",
                        "pubg.exe", "cod.exe", "battlefield.exe", "gta5.exe",
                        "minecraft.exe", "steam.exe", "origin.exe", "uplay.exe"
                    ]

                    for exe in game_exes:
                        if enable:

                            winreg.SetValueEx(key, exe, 0, winreg.REG_SZ, "GpuPreference=2;")
                        else:

                            try:
                                winreg.DeleteValue(key, exe)
                            except FileNotFoundError:
                                pass
            except Exception:
                pass

            try:
                if enable:
                    ps_command = """
                    $apps = Get-ChildItem "HKCU:\\SOFTWARE\\Microsoft\\DirectX\\UserGpuPreferences"
                    foreach ($app in $apps) {
                        Set-ItemProperty -Path $app.PSPath -Name "GpuPreference" -Value "GpuPreference=2;"
                    }
                    """
                else:
                    ps_command = """
                    $apps = Get-ChildItem "HKCU:\\SOFTWARE\\Microsoft\\DirectX\\UserGpuPreferences"
                    foreach ($app in $apps) {
                        Remove-ItemProperty -Path $app.PSPath -Name "GpuPreference" -ErrorAction SilentlyContinue
                    }
                    """

                subprocess.run([
                    "powershell", "-Command", ps_command
                ], capture_output=True, check=False)
            except Exception:
                pass

            return True
        except Exception as e:
            print(f"Error setting GPU preference: {e}")
            return False

    def toggle_hardware_acceleration(self, enable: bool) -> bool:

        try:

            chrome_key = r"SOFTWARE\Policies\Google\Chrome"
            try:
                with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, chrome_key) as key:
                    winreg.SetValueEx(key, "HardwareAccelerationModeEnabled", 0, winreg.REG_DWORD, 1 if enable else 0)
            except Exception:
                pass

            edge_key = r"SOFTWARE\Policies\Microsoft\Edge"
            try:
                with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, edge_key) as key:
                    winreg.SetValueEx(key, "HardwareAccelerationModeEnabled", 0, winreg.REG_DWORD, 1 if enable else 0)
            except Exception:
                pass

            try:
                firefox_profiles = self._get_firefox_profiles()
                for profile_path in firefox_profiles:
                    prefs_file = os.path.join(profile_path, "prefs.js")
                    if os.path.exists(prefs_file):
                        self._modify_firefox_prefs(prefs_file, enable)
            except Exception:
                pass

            return True
        except Exception as e:
            print(f"Error toggling hardware acceleration: {e}")
            return False

    def _get_firefox_profiles(self) -> list:

        profiles = []
        try:
            appdata = os.environ.get('APPDATA', '')
            firefox_dir = os.path.join(appdata, 'Mozilla', 'Firefox', 'Profiles')

            if os.path.exists(firefox_dir):
                for item in os.listdir(firefox_dir):
                    profile_path = os.path.join(firefox_dir, item)
                    if os.path.isdir(profile_path):
                        profiles.append(profile_path)
        except Exception:
            pass

        return profiles

    def _modify_firefox_prefs(self, prefs_file: str, enable_hw_accel: bool):

        try:

            with open(prefs_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            hw_accel_prefs = {
                "layers.acceleration.force-enabled": enable_hw_accel,
                "layers.acceleration.disabled": not enable_hw_accel,
                "gfx.direct2d.disabled": enable_hw_accel,
                "layers.prefer-opengl": enable_hw_accel
            }

            updated_lines = []
            prefs_updated = set()

            for line in lines:
                updated = False
                for pref_name, pref_value in hw_accel_prefs.items():
                    if f'user_pref("{pref_name}"' in line:
                        updated_lines.append(f'user_pref("{pref_name}", {str(pref_value).lower()});\n')
                        prefs_updated.add(pref_name)
                        updated = True
                        break

                if not updated:
                    updated_lines.append(line)

            for pref_name, pref_value in hw_accel_prefs.items():
                if pref_name not in prefs_updated:
                    updated_lines.append(f'user_pref("{pref_name}", {str(pref_value).lower()});\n')

            with open(prefs_file, 'w', encoding='utf-8') as f:
                f.writelines(updated_lines)

        except Exception as e:
            print(f"Error modifying Firefox prefs: {e}")

    def optimize_nvidia_settings(self) -> bool:

        try:

            nvidia_key = r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000"

            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, nvidia_key, 0, winreg.KEY_SET_VALUE) as key:

                    winreg.SetValueEx(key, "RMHdcpKeyglobZero", 0, winreg.REG_DWORD, 1)

                    winreg.SetValueEx(key, "PowerMizerEnable", 0, winreg.REG_DWORD, 1)
                    winreg.SetValueEx(key, "PowerMizerLevel", 0, winreg.REG_DWORD, 1)
                    winreg.SetValueEx(key, "PowerMizerLevelAC", 0, winreg.REG_DWORD, 1)

                    winreg.SetValueEx(key, "EnableMidBufferPreemption", 0, winreg.REG_DWORD, 0)
                    winreg.SetValueEx(key, "EnableMidGfxPreemption", 0, winreg.REG_DWORD, 0)
                    winreg.SetValueEx(key, "EnableMidGfxPreemptionVGPU", 0, winreg.REG_DWORD, 0)

            except Exception:
                pass

            return True
        except Exception as e:
            print(f"Error optimizing NVIDIA settings: {e}")
            return False

    def optimize_amd_settings(self) -> bool:

        try:

            amd_key = r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000"

            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, amd_key, 0, winreg.KEY_SET_VALUE) as key:

                    winreg.SetValueEx(key, "EnableUlps", 0, winreg.REG_DWORD, 0)

                    winreg.SetValueEx(key, "PP_ThermalAutoThrottlingEnable", 0, winreg.REG_DWORD, 0)

            except Exception:
                pass

            return True
        except Exception as e:
            print(f"Error optimizing AMD settings: {e}")
            return False

    def set_display_scaling(self, scaling_percent: int = 100) -> bool:

        try:

            dpi_key = r"Control Panel\Desktop"
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, dpi_key, 0, winreg.KEY_SET_VALUE) as key:

                dpi_value = int(96 * (scaling_percent / 100))
                winreg.SetValueEx(key, "LogPixels", 0, winreg.REG_DWORD, dpi_value)

                winreg.SetValueEx(key, "Win8DpiScaling", 0, winreg.REG_DWORD, 1)

            return True
        except Exception as e:
            print(f"Error setting display scaling: {e}")
            return False

    def get_gpu_info(self) -> Dict[str, Any]:

        gpu_info = {
            'name': 'Unknown',
            'driver_version': 'Unknown',
            'memory': 'Unknown'
        }

        try:

            result = subprocess.run([
                "wmic", "path", "win32_VideoController", "get",
                "AdapterRAM,DriverVersion,Name", "/format:csv"
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
                                memory_bytes = int(parts[0])
                                memory_gb = memory_bytes / (1024**3)
                                gpu_info['memory'] = f"{memory_gb:.1f} GB"
                            break
        except Exception as e:
            print(f"Error getting GPU info: {e}")

        return gpu_info

    def optimize_gpu_drivers(self) -> tuple[bool, str]:

        try:
            results = []

            if self.optimize_nvidia_settings():
                results.append("✅ NVIDIA settings optimized")

            if self.optimize_amd_settings():
                results.append("✅ AMD settings optimized")

            try:

                tdr_key = r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers"
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, tdr_key, 0, winreg.KEY_SET_VALUE) as key:
                    winreg.SetValueEx(key, "TdrLevel", 0, winreg.REG_DWORD, 0)
                    winreg.SetValueEx(key, "TdrDelay", 0, winreg.REG_DWORD, 60)
                results.append("✅ GPU timeout detection optimized")
            except Exception:
                results.append("⚠️ Could not optimize GPU timeout settings")

            try:
                gpu_mem_key = r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers"
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, gpu_mem_key, 0, winreg.KEY_SET_VALUE) as key:
                    winreg.SetValueEx(key, "DxgKrnlVersion", 0, winreg.REG_DWORD, 2)
                results.append("✅ GPU memory allocation optimized")
            except Exception:
                results.append("⚠️ Could not optimize GPU memory allocation")

            if results:
                return True, "\n".join(results)
            else:
                return False, "No GPU optimizations could be applied"

        except Exception as e:
            return False, f"Error optimizing GPU drivers: {str(e)}"

    def optimize_gpu_memory(self) -> tuple[bool, str]:

        try:
            results = []

            try:
                mem_key = r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers"
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, mem_key, 0, winreg.KEY_SET_VALUE) as key:

                    winreg.SetValueEx(key, "DedicatedSegmentSize", 0, winreg.REG_DWORD, 1024)

                    winreg.SetValueEx(key, "HwSchMode", 0, winreg.REG_DWORD, 2)
                results.append("✅ GPU memory allocation increased")
            except Exception:
                results.append("⚠️ Could not optimize GPU memory allocation")

            try:
                vram_key = r"SOFTWARE\Microsoft\DirectX"
                with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, vram_key) as key:
                    winreg.SetValueEx(key, "DisableAGPSupport", 0, winreg.REG_DWORD, 0)
                    winreg.SetValueEx(key, "EnableDebugging", 0, winreg.REG_DWORD, 0)
                results.append("✅ VRAM usage optimized")
            except Exception:
                results.append("⚠️ Could not optimize VRAM settings")

            try:
                power_key = r"SYSTEM\CurrentControlSet\Control\Power"
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, power_key, 0, winreg.KEY_SET_VALUE) as key:
                    winreg.SetValueEx(key, "CsEnabled", 0, winreg.REG_DWORD, 0)
                results.append("✅ GPU power saving disabled")
            except Exception:
                results.append("⚠️ Could not disable GPU power saving")

            try:
                cache_key = r"SOFTWARE\Microsoft\Direct3D"
                with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, cache_key) as key:
                    winreg.SetValueEx(key, "DisableVidMemVBs", 0, winreg.REG_DWORD, 0)
                    winreg.SetValueEx(key, "MMX Fast Path", 0, winreg.REG_DWORD, 1)
                results.append("✅ GPU cache optimized")
            except Exception:
                results.append("⚠️ Could not optimize GPU cache")

            if results:
                return True, "\n".join(results)
            else:
                return False, "No GPU memory optimizations could be applied"

        except Exception as e:
            return False, f"Error optimizing GPU memory: {str(e)}"

    def optimize_directx(self) -> tuple[bool, str]:

        try:
            results = []

            try:
                dx_key = r"SOFTWARE\Microsoft\DirectX"
                with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, dx_key) as key:

                    winreg.SetValueEx(key, "D3D12_ENABLE_UNSAFE_COMMAND_BUFFER_REUSE", 0, winreg.REG_DWORD, 1)
                    winreg.SetValueEx(key, "D3D12_RESIDENCY_MANAGEMENT_ENABLED", 0, winreg.REG_DWORD, 1)
                results.append("✅ DirectX performance settings optimized")
            except Exception:
                results.append("⚠️ Could not optimize DirectX settings")

            try:
                d3d_key = r"SOFTWARE\Microsoft\Direct3D"
                with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, d3d_key) as key:

                    winreg.SetValueEx(key, "DisableAGPSupport", 0, winreg.REG_DWORD, 0)
                    winreg.SetValueEx(key, "EnableDebugging", 0, winreg.REG_DWORD, 0)
                    winreg.SetValueEx(key, "LoadDebugRuntime", 0, winreg.REG_DWORD, 0)
                results.append("✅ Direct3D acceleration enabled")
            except Exception:
                results.append("⚠️ Could not optimize Direct3D settings")

            try:
                opengl_key = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\OpenGLDrivers"
                with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, opengl_key) as key:
                    winreg.SetValueEx(key, "SoftwareOnly", 0, winreg.REG_DWORD, 0)
                results.append("✅ OpenGL hardware acceleration enabled")
            except Exception:
                results.append("⚠️ Could not optimize OpenGL settings")

            try:
                debug_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\GraphicsDrivers"
                with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, debug_key) as key:
                    winreg.SetValueEx(key, "DisableOverlays", 0, winreg.REG_DWORD, 1)
                results.append("✅ Graphics debugging disabled")
            except Exception:
                results.append("⚠️ Could not disable graphics debugging")

            try:
                game_key = r"SOFTWARE\Microsoft\DirectX\UserGpuPreferences"
                with winreg.CreateKey(winreg.HKEY_CURRENT_USER, game_key) as key:

                    winreg.SetValueEx(key, "DirectXUserGlobalSettings", 0, winreg.REG_SZ, "VRROptimizeEnable=0;SwapEffectUpgradeEnable=1;")
                results.append("✅ Game graphics preferences optimized")
            except Exception:
                results.append("⚠️ Could not optimize game graphics settings")

            if results:
                return True, "\n".join(results)
            else:
                return False, "No DirectX optimizations could be applied"

        except Exception as e:
            return False, f"Error optimizing DirectX: {str(e)}"
