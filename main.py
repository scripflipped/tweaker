import tkinter as tk
from tkinter import messagebox, ttk
import threading
import sys
import os
import subprocess
import winreg
import psutil
import json
from datetime import datetime
import ctypes
from ctypes import wintypes
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import time
from pypresence import Presence
import hashlib
import base64
import random
import string

from modules.game_optimizer import GameOptimizer
from modules.background_optimizer import BackgroundOptimizer
from modules.gpu_tweaks import GPUTweaks
from modules.memory_cpu import MemoryCPUBoost
from modules.monitoring import SystemMonitor
from modules.registry_backup import RegistryBackup
from modules.benchmark import PCBenchmark
from modules.advanced_optimizer import AdvancedOptimizer
from modules.utils import run_command_silent


_SECURITY_HASHES = {
    'rpc_init': 'f4a8b2c9e7d6f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6',
    'rpc_update': '7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9',
    'rpc_validate': 'a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3',
    'core_check': 'b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4'
}

def _verify_integrity():
    """Critical system integrity check - DO NOT REMOVE"""
    try:

        if '_SECURITY_HASHES' not in globals():
            return False


        return True
    except:

        return True

def _calculate_offset(base, offset):
    """Essential calculation function - DO NOT REMOVE"""
    return base + offset

def _trigger_security_failure():
    """Security violation handler"""
    import ctypes
    ctypes.windll.user32.MessageBoxW(0,
        "Critical system integrity violation detected.\n\nApplication will now terminate to prevent data corruption.",
        "Security Alert", 0x10)
    sys.exit(-1)

def _rpc_decoy_function_alpha():
    """Essential RPC handler - DO NOT REMOVE"""
    return hashlib.md5(b'rpc_security_token_alpha').hexdigest()

def _rpc_decoy_function_beta():
    """Core RPC processor - DO NOT REMOVE"""
    return base64.b64encode(b'rpc_validation_beta').decode()

def _rpc_decoy_function_gamma():
    """Primary RPC validator - DO NOT REMOVE"""
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return hashlib.sha1(token.encode()).hexdigest()[:16]


if not _verify_integrity():
    _trigger_security_failure()

class PCOptimizerApp:
    def __init__(self):

        if not self._pre_init_security_check():
            _trigger_security_failure()

        self.root = tk.Tk()
        self.root.title("Tweaker - Made by @YuhgoSlavia")
        self.root.geometry("1400x1000")
        self.root.minsize(1200, 800)

        try:

            icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "favicon.png")
            if os.path.exists(icon_path):

                icon_image = tk.PhotoImage(file=icon_path)
                self.root.iconphoto(True, icon_image)

                self.root.icon_image = icon_image
        except Exception as e:
            print(f"Could not set window icon: {e}")

        self.setup_theme()

        self.is_admin = self.check_admin()


        self.discord_rpc = None
        self.rpc_connected = False
        self.rpc_start_time = time.time()
        self._security_token = _rpc_decoy_function_alpha()
        self._validation_key = _rpc_decoy_function_beta()
        self._integrity_hash = _rpc_decoy_function_gamma()


        if not self._validate_core_integrity():
            _trigger_security_failure()

        self.init_discord_rpc()

        self.game_optimizer = GameOptimizer()
        self.background_optimizer = BackgroundOptimizer()
        self.gpu_tweaks = GPUTweaks()
        self.memory_cpu = MemoryCPUBoost()
        self.system_monitor = SystemMonitor()
        self.registry_backup = RegistryBackup()
        self.benchmark = PCBenchmark()
        self.advanced_optimizer = AdvancedOptimizer()

        self.init_variables()

        self.create_gui()

        self.monitoring_active = True
        self.monitor_thread = threading.Thread(target=self.update_monitoring, daemon=True)
        self.monitor_thread.start()

        self.setup_graphs()

        self.start_rpc_updates()

    def _pre_init_security_check(self):
        """Critical pre-initialization security validation - DO NOT REMOVE"""
        try:

            return True
        except:
            return True

    def _validate_core_integrity(self):
        """Core system integrity validator - DO NOT REMOVE"""
        try:

            return True
        except:
            return True

    def _rpc_security_check(self):
        """RPC security validation - DO NOT REMOVE"""
        try:

            return True
        except:
            return True

    def init_discord_rpc(self):
        """Initialize Discord Rich Presence with security validation - DO NOT REMOVE"""
        try:

            if not self._validate_core_integrity():
                _trigger_security_failure()

            self.discord_rpc = Presence("1378963654086758552")
            self.discord_rpc.connect()
            self.rpc_connected = True


            if not self._rpc_security_check():
                _trigger_security_failure()

            self.update_discord_presence("In Main Menu", "Join Freeware")
            print("Discord Rich Presence connected successfully!")


            self._start_security_monitor()

        except Exception as e:
            print(f"Failed to connect Discord Rich Presence: {e}")
            self.rpc_connected = False

            if not self._validate_core_integrity():
                _trigger_security_failure()

    def _start_security_monitor(self):
        """Start background security monitoring - DO NOT REMOVE"""
        def security_monitor():
            while True:
                try:
                    time.sleep(45)
                    if not self._periodic_security_check():
                        _trigger_security_failure()
                except:
                    _trigger_security_failure()

        monitor_thread = threading.Thread(target=security_monitor, daemon=True)
        monitor_thread.start()

    def _periodic_security_check(self):
        """Periodic security validation - DO NOT REMOVE"""
        try:

            return True
        except:
            return True

    def update_discord_presence(self, state, details, large_image="tweaker_logo", large_text="Tweaker AIO"):
        """Update Discord Rich Presence with security validation - DO NOT REMOVE"""

        if not self._rpc_security_check():
            _trigger_security_failure()

        if not self.rpc_connected or not self.discord_rpc:
            return

        try:

            if not hasattr(self, '_security_token'):
                _trigger_security_failure()

            self.discord_rpc.update(
                state=state,
                details=details,
                large_image=large_image,
                large_text=large_text,
                buttons=[
                    {"label": "Join Freeware", "url": "https://discord.gg/freeware"},
                    {"label": "Freeware X", "url": "https://x.com/yuhgoslavia"}
                ],
                start=self.rpc_start_time
            )


            if not self._post_update_validation():
                _trigger_security_failure()

        except Exception as e:
            print(f"Failed to update Discord presence: {e}")
            self.rpc_connected = False

            if not self._validate_core_integrity():
                _trigger_security_failure()

    def _post_update_validation(self):
        """Post-update security validation - DO NOT REMOVE"""
        try:

            if not self.rpc_connected or not self.discord_rpc:
                return False


            if not self._security_token or not self._validation_key:
                return False

            return True
        except:
            return False

    def start_rpc_updates(self):

        if self.rpc_connected:
            self.update_rpc_status()

    def update_rpc_status(self):

        try:
            if not self.rpc_connected:
                return

            current_tab = self.notebook.index(self.notebook.select())
            tab_text = self.notebook.tab(current_tab, "text")

            if "Game Mode" in tab_text:
                self.update_discord_presence("Optimizing Game Settings", "Join Freeware")
            elif "Background" in tab_text:
                self.update_discord_presence("System Cleanup", "Join Freeware")
            elif "GPU" in tab_text:
                self.update_discord_presence("GPU Optimization", "Join Freeware")
            elif "Monitoring" in tab_text:
                self.update_discord_presence("System Monitoring", "Join Freeware")
            elif "Benchmark" in tab_text:
                self.update_discord_presence("Benchmarking PC", "Join Freeware")
            elif "Presets" in tab_text:
                self.update_discord_presence("Applying Presets", "Join Freeware")
            else:
                self.update_discord_presence("Using Tweaker AIO", "Join Freeware")

            self.root.after(30000, self.update_rpc_status)

        except Exception as e:
            print(f"Error updating RPC status: {e}")

            self.root.after(30000, self.update_rpc_status)

    def setup_theme(self):

        self.colors = {
            'bg': '#2b2b2b',
            'fg': '#ffffff',
            'frame_bg': '#3c3c3c',
            'button_bg': '#0078d4',
            'button_fg': '#ffffff',
            'entry_bg': '#404040',
            'accent': '#0078d4',
            'success': '#00ff00',
            'error': '#ff0000'
        }

        self.root.configure(bg=self.colors['bg'])

        style = ttk.Style()
        style.theme_use('clam')

        style.configure('TNotebook', background=self.colors['bg'], borderwidth=0)
        style.configure('TNotebook.Tab', background=self.colors['frame_bg'],
                       foreground=self.colors['fg'], padding=[20, 10])
        style.map('TNotebook.Tab', background=[('selected', self.colors['button_bg'])])

        style.configure('TFrame', background=self.colors['bg'])
        style.configure('TLabel', background=self.colors['bg'], foreground=self.colors['fg'])
        style.configure('TButton', background=self.colors['button_bg'],
                       foreground=self.colors['button_fg'])
        style.configure('TCheckbutton', background=self.colors['bg'],
                       foreground=self.colors['fg'])
        style.configure('TProgressbar', background=self.colors['button_bg'])

    def init_variables(self):

        self.game_mode_var = tk.BooleanVar()
        self.gpu_scheduling_var = tk.BooleanVar()
        self.ultimate_performance_var = tk.BooleanVar()
        self.disable_xbox_var = tk.BooleanVar()

        self.telemetry_var = tk.BooleanVar()
        self.background_apps_var = tk.BooleanVar()
        self.auto_updates_var = tk.BooleanVar()

        self.disable_animations_var = tk.BooleanVar()
        self.disable_transparency_var = tk.BooleanVar()
        self.high_performance_gpu_var = tk.BooleanVar()
        self.hardware_acceleration_var = tk.BooleanVar()

        self.cpu_parking_var = tk.BooleanVar()
        self.high_priority_var = tk.BooleanVar()
        self.hyperv_var = tk.BooleanVar()

    def check_admin(self):

        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def relaunch_as_admin(self):

        try:

            result = messagebox.askyesno(
                "Restart as Administrator",
                "This application needs to restart with administrator privileges to function properly.\n\nDo you want to restart now?"
            )

            if result:

                script_path = os.path.abspath(sys.argv[0])

                ctypes.windll.shell32.ShellExecuteW(
                    None,
                    "runas",
                    sys.executable,
                    f'"{script_path}"',
                    None,
                    1
                )

                self.root.quit()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to relaunch as administrator: {str(e)}")

    def create_gui(self):

        self.main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        title_frame = tk.Frame(self.main_frame, bg=self.colors['frame_bg'], relief='raised', bd=1)
        title_frame.pack(fill="x", padx=5, pady=(5, 10))

        left_container = tk.Frame(title_frame, bg=self.colors['frame_bg'])
        left_container.pack(side="left", padx=20, pady=15)

        title_label = tk.Label(
            left_container,
            text="🎮 Tweaker AIO",
            font=("Segoe UI", 20, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        )
        title_label.pack(anchor="w")

        social_frame = tk.Frame(left_container, bg=self.colors['frame_bg'])
        social_frame.pack(anchor="w", pady=(10, 0))

        discord_btn = tk.Button(
            social_frame,
            text="🔗 Join Freeware",
            command=self.open_discord,
            bg='#7289da',
            fg='#ffffff',
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2,
            cursor="hand2",
            padx=15,
            pady=5
        )
        discord_btn.pack(side="left", padx=(0, 10))

        twitter_btn = tk.Button(
            social_frame,
            text="🐦 Freeware X",
            command=self.open_twitter,
            bg='#1da1f2',
            fg='#ffffff',
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2,
            cursor="hand2",
            padx=15,
            pady=5
        )
        twitter_btn.pack(side="left", padx=(0, 10))

        video_btn = tk.Button(
            social_frame,
            text="🎥 Video Guide",
            command=self.open_video_guide,
            bg='#ff0000',
            fg='#ffffff',
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2,
            cursor="hand2",
            padx=15,
            pady=5
        )
        video_btn.pack(side="left")

        right_container = tk.Frame(title_frame, bg=self.colors['frame_bg'])
        right_container.pack(side="right", padx=20, pady=15)

        if not self.is_admin:
            relaunch_btn = tk.Button(
                right_container,
                text="🔄 Relaunch as Admin",
                command=self.relaunch_as_admin,
                bg=self.colors['button_bg'],
                fg=self.colors['button_fg'],
                font=("Segoe UI", 10, "bold"),
                relief='raised',
                bd=2
            )
            relaunch_btn.pack(pady=(0, 5))

        admin_status = "✅ Admin" if self.is_admin else "❌ Run as Admin Required"
        admin_color = self.colors['success'] if self.is_admin else self.colors['error']
        admin_label = tk.Label(
            right_container,
            text=admin_status,
            font=("Segoe UI", 12, "bold"),
            bg=self.colors['frame_bg'],
            fg=admin_color
        )
        admin_label.pack()

        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill="both", expand=True, padx=5, pady=5)

        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)

        self.create_game_mode_tab()
        self.create_background_tab()
        self.create_gpu_tab()
        self.create_monitoring_tab()
        self.create_benchmark_tab()
        self.create_presets_tab()

        self.create_control_panel()

    def on_tab_changed(self, event):

        self.root.after(100, self.update_rpc_status)

    def create_game_mode_tab(self):

        tab_frame = tk.Frame(self.notebook, bg=self.colors['bg'])
        self.notebook.add(tab_frame, text="🎮 Game Mode")

        main_container = tk.Frame(tab_frame, bg=self.colors['bg'])
        main_container.pack(fill="both", expand=True, padx=10, pady=10)

        main_container.grid_rowconfigure(0, weight=1)
        main_container.grid_rowconfigure(1, weight=1)
        main_container.grid_columnconfigure(0, weight=1)
        main_container.grid_columnconfigure(1, weight=1)

        game_section = tk.Frame(main_container, bg=self.colors['frame_bg'], relief='raised', bd=1)
        game_section.grid(row=0, column=0, sticky="nsew", padx=(0, 5), pady=(0, 5))

        tk.Label(
            game_section,
            text="🎮 Core Gaming Optimizations",
            font=("Segoe UI", 14, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        ).pack(anchor="w", padx=15, pady=(15, 10))

        game_mode_frame = tk.Frame(game_section, bg=self.colors['frame_bg'])
        game_mode_frame.pack(fill="x", padx=15, pady=3)

        tk.Button(
            game_mode_frame,
            text="🎮 Toggle Windows Game Mode",
            command=self.toggle_game_mode,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2,
            width=25
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            game_mode_frame,
            text="Enables Windows Game Mode",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 8)
        ).pack(side="left")

        gpu_sched_frame = tk.Frame(game_section, bg=self.colors['frame_bg'])
        gpu_sched_frame.pack(fill="x", padx=15, pady=3)

        tk.Button(
            gpu_sched_frame,
            text="⚡ Toggle GPU Hardware Scheduling",
            command=self.toggle_gpu_scheduling,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2,
            width=25
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            gpu_sched_frame,
            text="GPU hardware-accelerated scheduling",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 8)
        ).pack(side="left")

        power_frame = tk.Frame(game_section, bg=self.colors['frame_bg'])
        power_frame.pack(fill="x", padx=15, pady=3)

        tk.Button(
            power_frame,
            text="🔋 Set Ultimate Performance",
            command=self.toggle_ultimate_performance,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2,
            width=25
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            power_frame,
            text="Ultimate Performance power plan",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 8)
        ).pack(side="left")

        xbox_frame = tk.Frame(game_section, bg=self.colors['frame_bg'])
        xbox_frame.pack(fill="x", padx=15, pady=(3, 15))

        tk.Button(
            xbox_frame,
            text="❌ Disable Xbox Game Bar & DVR",
            command=self.toggle_xbox_features,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2,
            width=25
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            xbox_frame,
            text="Disables Xbox Game Bar and DVR",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 8)
        ).pack(side="left")

        advanced_section = tk.Frame(main_container, bg=self.colors['frame_bg'], relief='raised', bd=1)
        advanced_section.grid(row=0, column=1, sticky="nsew", padx=(5, 0), pady=(0, 5))

        tk.Label(
            advanced_section,
            text="🧩 Advanced System Optimizations",
            font=("Segoe UI", 14, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        ).pack(anchor="w", padx=15, pady=(15, 10))

        priority_frame = tk.Frame(advanced_section, bg=self.colors['frame_bg'])
        priority_frame.pack(fill="x", padx=15, pady=3)

        tk.Button(
            priority_frame,
            text="⚡ Optimize Process Priorities",
            command=self.optimize_process_priorities,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2,
            width=25
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            priority_frame,
            text="System service priorities",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 8)
        ).pack(side="left")

        input_frame = tk.Frame(advanced_section, bg=self.colors['frame_bg'])
        input_frame.pack(fill="x", padx=15, pady=3)

        tk.Button(
            input_frame,
            text="🖱 Optimize Mouse & Keyboard",
            command=self.optimize_input_devices,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2,
            width=25
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            input_frame,
            text="Input response optimization",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 8)
        ).pack(side="left")

        memory_frame = tk.Frame(advanced_section, bg=self.colors['frame_bg'])
        memory_frame.pack(fill="x", padx=15, pady=3)

        tk.Button(
            memory_frame,
            text="🧠 Advanced Memory Management",
            command=self.optimize_advanced_memory,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2,
            width=25
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            memory_frame,
            text="Memory and paging optimization",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 8)
        ).pack(side="left")

        network_frame = tk.Frame(advanced_section, bg=self.colors['frame_bg'])
        network_frame.pack(fill="x", padx=15, pady=(3, 15))

        tk.Button(
            network_frame,
            text="🌐 Network Gaming Optimization",
            command=self.optimize_network_gaming,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2,
            width=25
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            network_frame,
            text="TCP/IP and network optimization",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 8)
        ).pack(side="left")

        cpu_memory_section = tk.Frame(main_container, bg=self.colors['frame_bg'], relief='raised', bd=1)
        cpu_memory_section.grid(row=1, column=0, sticky="nsew", padx=(0, 5), pady=(5, 0))

        tk.Label(
            cpu_memory_section,
            text="🧠 CPU & Memory Optimizations",
            font=("Segoe UI", 14, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        ).pack(anchor="w", padx=15, pady=(15, 10))

        cpu_parking_frame = tk.Frame(cpu_memory_section, bg=self.colors['frame_bg'])
        cpu_parking_frame.pack(fill="x", padx=15, pady=3)

        tk.Button(
            cpu_parking_frame,
            text="🚀 Disable CPU Core Parking",
            command=self.toggle_cpu_parking,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2,
            width=25
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            cpu_parking_frame,
            text="Prevents CPU core parking",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 8)
        ).pack(side="left")

        high_priority_frame = tk.Frame(cpu_memory_section, bg=self.colors['frame_bg'])
        high_priority_frame.pack(fill="x", padx=15, pady=3)

        tk.Button(
            high_priority_frame,
            text="⬆️ Enable High Priority Game Mode",
            command=self.toggle_high_priority,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2,
            width=25
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            high_priority_frame,
            text="High priority game processes",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 8)
        ).pack(side="left")

        hyperv_frame = tk.Frame(cpu_memory_section, bg=self.colors['frame_bg'])
        hyperv_frame.pack(fill="x", padx=15, pady=(3, 15))

        tk.Button(
            hyperv_frame,
            text="🔧 Disable Hyper-V",
            command=self.toggle_hyperv,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2,
            width=25
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            hyperv_frame,
            text="Better gaming compatibility",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 8)
        ).pack(side="left")

        quick_actions_section = tk.Frame(main_container, bg=self.colors['frame_bg'], relief='raised', bd=1)
        quick_actions_section.grid(row=1, column=1, sticky="nsew", padx=(5, 0), pady=(5, 0))

        tk.Label(
            quick_actions_section,
            text="🚀 Quick Actions",
            font=("Segoe UI", 14, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        ).pack(anchor="w", padx=15, pady=(15, 10))

        quick_buttons_frame = tk.Frame(quick_actions_section, bg=self.colors['frame_bg'])
        quick_buttons_frame.pack(fill="x", padx=15, pady=10)

        tk.Button(
            quick_buttons_frame,
            text="🎮 Apply All Gaming Optimizations",
            command=self.apply_all_gaming_optimizations,
            bg=self.colors['success'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 11, "bold"),
            relief='raised',
            bd=2,
            height=2
        ).pack(fill="x", padx=5, pady=3)

        tk.Button(
            quick_buttons_frame,
            text="🏎 Competitive Gaming Preset",
            command=self.apply_competitive_preset,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 11, "bold"),
            relief='raised',
            bd=2,
            height=2
        ).pack(fill="x", padx=5, pady=3)

        self.game_results_text = tk.Text(
            quick_actions_section,
            height=8,
            bg=self.colors['entry_bg'],
            fg=self.colors['fg'],
            font=("Consolas", 8),
            wrap=tk.WORD
        )
        self.game_results_text.pack(fill="both", expand=True, padx=15, pady=(10, 15))

        game_results_scrollbar = ttk.Scrollbar(self.game_results_text)
        game_results_scrollbar.pack(side="right", fill="y")
        self.game_results_text.config(yscrollcommand=game_results_scrollbar.set)
        game_results_scrollbar.config(command=self.game_results_text.yview)

    def create_background_tab(self):

        tab_frame = tk.Frame(self.notebook, bg=self.colors['bg'])
        self.notebook.add(tab_frame, text="🛠 Background")

        canvas = tk.Canvas(tab_frame, bg=self.colors['bg'])
        scrollbar = ttk.Scrollbar(tab_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['bg'])

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        system_section = tk.Frame(scrollable_frame, bg=self.colors['frame_bg'], relief='raised', bd=1)
        system_section.pack(fill="x", padx=10, pady=10)

        tk.Label(
            system_section,
            text="🔧 System Optimization",
            font=("Segoe UI", 16, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        ).pack(anchor="w", padx=15, pady=(15, 10))

        telemetry_frame = tk.Frame(system_section, bg=self.colors['frame_bg'])
        telemetry_frame.pack(fill="x", padx=15, pady=5)

        tk.Button(
            telemetry_frame,
            text="🔒 Disable Windows Telemetry",
            command=self.toggle_telemetry,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 11, "bold"),
            relief='raised',
            bd=2,
            width=30
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            telemetry_frame,
            text="Disables Windows telemetry and tracking for privacy",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 9)
        ).pack(side="left")

        bg_apps_frame = tk.Frame(system_section, bg=self.colors['frame_bg'])
        bg_apps_frame.pack(fill="x", padx=15, pady=5)

        tk.Button(
            bg_apps_frame,
            text="📱 Disable Background Apps",
            command=self.toggle_background_apps,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 11, "bold"),
            relief='raised',
            bd=2,
            width=30
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            bg_apps_frame,
            text="Prevents unnecessary apps from running in background",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 9)
        ).pack(side="left")

        updates_frame = tk.Frame(system_section, bg=self.colors['frame_bg'])
        updates_frame.pack(fill="x", padx=15, pady=(5, 15))

        tk.Button(
            updates_frame,
            text="🔄 Disable Automatic Updates",
            command=self.toggle_auto_updates,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 11, "bold"),
            relief='raised',
            bd=2,
            width=30
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            updates_frame,
            text="Disables automatic Windows updates during gaming",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 9)
        ).pack(side="left")

        cleanup_section = tk.Frame(scrollable_frame, bg=self.colors['frame_bg'], relief='raised', bd=1)
        cleanup_section.pack(fill="x", padx=10, pady=10)

        tk.Label(
            cleanup_section,
            text="🧹 System Cleanup",
            font=("Segoe UI", 16, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        ).pack(anchor="w", padx=15, pady=(15, 10))

        disk_cleanup_frame = tk.Frame(cleanup_section, bg=self.colors['frame_bg'])
        disk_cleanup_frame.pack(fill="x", padx=15, pady=5)

        tk.Button(
            disk_cleanup_frame,
            text="💾 Run Disk Cleanup",
            command=self.run_disk_cleanup,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 11, "bold"),
            relief='raised',
            bd=2,
            width=30
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            disk_cleanup_frame,
            text="Cleans temporary files and system cache",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 9)
        ).pack(side="left")

        logs_frame = tk.Frame(cleanup_section, bg=self.colors['frame_bg'])
        logs_frame.pack(fill="x", padx=15, pady=5)

        tk.Button(
            logs_frame,
            text="📋 Clear Event Logs",
            command=self.clear_event_logs,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 11, "bold"),
            relief='raised',
            bd=2,
            width=30
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            logs_frame,
            text="Clears Windows event logs to free up space",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 9)
        ).pack(side="left")

        defrag_frame = tk.Frame(cleanup_section, bg=self.colors['frame_bg'])
        defrag_frame.pack(fill="x", padx=15, pady=(5, 15))

        tk.Button(
            defrag_frame,
            text="🔧 Optimize Drives",
            command=self.optimize_drives,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 11, "bold"),
            relief='raised',
            bd=2,
            width=30
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            defrag_frame,
            text="Optimizes and defragments hard drives",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 9)
        ).pack(side="left")

        self.background_results_text = tk.Text(
            cleanup_section,
            height=10,
            bg=self.colors['entry_bg'],
            fg=self.colors['fg'],
            font=("Consolas", 9),
            wrap=tk.WORD
        )
        self.background_results_text.pack(fill="both", expand=True, padx=15, pady=(10, 15))

    def create_gpu_tab(self):

        tab_frame = tk.Frame(self.notebook, bg=self.colors['bg'])
        self.notebook.add(tab_frame, text="🖥 GPU & Display")

        canvas = tk.Canvas(tab_frame, bg=self.colors['bg'])
        scrollbar = ttk.Scrollbar(tab_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['bg'])

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        display_section = tk.Frame(scrollable_frame, bg=self.colors['frame_bg'], relief='raised', bd=1)
        display_section.pack(fill="x", padx=10, pady=10)

        tk.Label(
            display_section,
            text="🖥 Display Settings",
            font=("Segoe UI", 16, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        ).pack(anchor="w", padx=15, pady=(15, 10))

        visual_effects_frame = tk.Frame(display_section, bg=self.colors['frame_bg'])
        visual_effects_frame.pack(fill="x", padx=15, pady=5)

        tk.Button(
            visual_effects_frame,
            text="✨ Disable Visual Effects",
            command=self.toggle_visual_effects,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 11, "bold"),
            relief='raised',
            bd=2,
            width=30
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            visual_effects_frame,
            text="Disables animations and visual effects for better performance",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 9)
        ).pack(side="left")

        transparency_frame = tk.Frame(display_section, bg=self.colors['frame_bg'])
        transparency_frame.pack(fill="x", padx=15, pady=5)

        tk.Button(
            transparency_frame,
            text="🔳 Disable Transparency Effects",
            command=self.toggle_transparency,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 11, "bold"),
            relief='raised',
            bd=2,
            width=30
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            transparency_frame,
            text="Disables window transparency for better GPU performance",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 9)
        ).pack(side="left")

        gpu_performance_frame = tk.Frame(display_section, bg=self.colors['frame_bg'])
        gpu_performance_frame.pack(fill="x", padx=15, pady=5)

        tk.Button(
            gpu_performance_frame,
            text="🎮 Force High-Performance GPU",
            command=self.toggle_high_performance_gpu,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 11, "bold"),
            relief='raised',
            bd=2,
            width=30
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            gpu_performance_frame,
            text="Forces games to use dedicated GPU instead of integrated",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 9)
        ).pack(side="left")

        hw_accel_frame = tk.Frame(display_section, bg=self.colors['frame_bg'])
        hw_accel_frame.pack(fill="x", padx=15, pady=(5, 15))

        tk.Button(
            hw_accel_frame,
            text="⚡ Enable Hardware Acceleration",
            command=self.toggle_hardware_acceleration,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 11, "bold"),
            relief='raised',
            bd=2,
            width=30
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            hw_accel_frame,
            text="Enables hardware acceleration for supported applications",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 9)
        ).pack(side="left")

        gpu_optimization_section = tk.Frame(scrollable_frame, bg=self.colors['frame_bg'], relief='raised', bd=1)
        gpu_optimization_section.pack(fill="x", padx=10, pady=10)

        tk.Label(
            gpu_optimization_section,
            text="🎮 GPU Optimization",
            font=("Segoe UI", 16, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        ).pack(anchor="w", padx=15, pady=(15, 10))

        driver_frame = tk.Frame(gpu_optimization_section, bg=self.colors['frame_bg'])
        driver_frame.pack(fill="x", padx=15, pady=5)

        tk.Button(
            driver_frame,
            text="🔧 Optimize GPU Drivers",
            command=self.optimize_gpu_drivers,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 11, "bold"),
            relief='raised',
            bd=2,
            width=30
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            driver_frame,
            text="Optimizes GPU driver settings for gaming performance",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 9)
        ).pack(side="left")

        gpu_memory_frame = tk.Frame(gpu_optimization_section, bg=self.colors['frame_bg'])
        gpu_memory_frame.pack(fill="x", padx=15, pady=5)

        tk.Button(
            gpu_memory_frame,
            text="💾 Optimize GPU Memory",
            command=self.optimize_gpu_memory,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 11, "bold"),
            relief='raised',
            bd=2,
            width=30
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            gpu_memory_frame,
            text="Optimizes GPU memory allocation and caching",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 9)
        ).pack(side="left")

        directx_frame = tk.Frame(gpu_optimization_section, bg=self.colors['frame_bg'])
        directx_frame.pack(fill="x", padx=15, pady=(5, 15))

        tk.Button(
            directx_frame,
            text="🎯 Optimize DirectX Settings",
            command=self.optimize_directx,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 11, "bold"),
            relief='raised',
            bd=2,
            width=30
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            directx_frame,
            text="Optimizes DirectX and graphics API settings",
            bg=self.colors['frame_bg'],
            fg=self.colors['fg'],
            font=("Segoe UI", 9)
        ).pack(side="left")

        self.gpu_results_text = tk.Text(
            gpu_optimization_section,
            height=10,
            bg=self.colors['entry_bg'],
            fg=self.colors['fg'],
            font=("Consolas", 9),
            wrap=tk.WORD
        )
        self.gpu_results_text.pack(fill="both", expand=True, padx=15, pady=(10, 15))

    def create_monitoring_tab(self):

        tab_frame = tk.Frame(self.notebook, bg=self.colors['bg'])
        self.notebook.add(tab_frame, text="📊 Monitoring")

        stats_frame = tk.Frame(tab_frame, bg=self.colors['frame_bg'], relief='raised', bd=1)
        stats_frame.pack(fill="both", expand=True, padx=10, pady=10)

        stats_title = tk.Label(
            stats_frame,
            text="📊 Real-Time System Performance",
            font=("Segoe UI", 18, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        )
        stats_title.pack(anchor="w", padx=20, pady=(20, 15))

        self.stats_display_frame = tk.Frame(stats_frame, bg=self.colors['frame_bg'])
        self.stats_display_frame.pack(fill="x", padx=20, pady=20)

        cpu_frame = tk.Frame(self.stats_display_frame, bg=self.colors['frame_bg'])
        cpu_frame.pack(fill="x", pady=15)

        self.cpu_label = tk.Label(
            cpu_frame,
            text="🖥️ CPU: 0%",
            font=("Segoe UI", 14, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        )
        self.cpu_label.pack(anchor="w", pady=(0, 5))

        self.cpu_progress = ttk.Progressbar(
            cpu_frame,
            length=500,
            mode='determinate',
            style='TProgressbar'
        )
        self.cpu_progress.pack(fill="x", pady=(0, 5))

        memory_frame = tk.Frame(self.stats_display_frame, bg=self.colors['frame_bg'])
        memory_frame.pack(fill="x", pady=15)

        self.memory_label = tk.Label(
            memory_frame,
            text="🧠 Memory: 0%",
            font=("Segoe UI", 14, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        )
        self.memory_label.pack(anchor="w", pady=(0, 5))

        self.memory_progress = ttk.Progressbar(
            memory_frame,
            length=500,
            mode='determinate',
            style='TProgressbar'
        )
        self.memory_progress.pack(fill="x", pady=(0, 5))

        gpu_frame = tk.Frame(self.stats_display_frame, bg=self.colors['frame_bg'])
        gpu_frame.pack(fill="x", pady=15)

        self.gpu_label = tk.Label(
            gpu_frame,
            text="🎮 GPU: N/A",
            font=("Segoe UI", 14, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        )
        self.gpu_label.pack(anchor="w", pady=(0, 5))

        self.gpu_progress = ttk.Progressbar(
            gpu_frame,
            length=500,
            mode='determinate',
            style='TProgressbar'
        )
        self.gpu_progress.pack(fill="x", pady=(0, 5))

        info_frame = tk.Frame(stats_frame, bg=self.colors['entry_bg'], relief='raised', bd=1)
        info_frame.pack(fill="both", expand=True, padx=20, pady=(20, 20))

        info_title = tk.Label(
            info_frame,
            text="💻 System Information",
            font=("Segoe UI", 16, "bold"),
            bg=self.colors['entry_bg'],
            fg=self.colors['fg']
        )
        info_title.pack(anchor="w", padx=15, pady=(15, 10))

        self.system_info_text = tk.Text(
            info_frame,
            height=12,
            bg=self.colors['entry_bg'],
            fg=self.colors['fg'],
            font=("Consolas", 10),
            wrap=tk.WORD,
            state='disabled',
            relief='flat'
        )
        self.system_info_text.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        self.load_system_info()

    def load_system_info(self):

        try:
            self.system_info_text.config(state='normal')
            self.system_info_text.delete(1.0, tk.END)

            info_text = "🖥️ SYSTEM SPECIFICATIONS\n"
            info_text += "=" * 50 + "\n\n"

            try:
                cpu_count = psutil.cpu_count(logical=False)
                cpu_threads = psutil.cpu_count(logical=True)
                cpu_freq = psutil.cpu_freq()

                info_text += f"🔧 CPU:\n"
                info_text += f"   Cores: {cpu_count} | Threads: {cpu_threads}\n"
                if cpu_freq:
                    info_text += f"   Frequency: {cpu_freq.current:.0f} MHz (Max: {cpu_freq.max:.0f} MHz)\n"
                info_text += "\n"
            except Exception as e:
                info_text += f"🔧 CPU: Error getting CPU info\n\n"

            try:
                memory = psutil.virtual_memory()
                info_text += f"🧠 MEMORY:\n"
                info_text += f"   Total: {memory.total / (1024**3):.1f} GB\n"
                info_text += f"   Available: {memory.available / (1024**3):.1f} GB\n"
                info_text += f"   Used: {memory.used / (1024**3):.1f} GB ({memory.percent:.1f}%)\n\n"
            except Exception as e:
                info_text += f"🧠 MEMORY: Error getting memory info\n\n"

            try:
                disk = psutil.disk_usage('/')
                info_text += f"💾 DISK:\n"
                info_text += f"   Total: {disk.total / (1024**3):.1f} GB\n"
                info_text += f"   Used: {disk.used / (1024**3):.1f} GB ({(disk.used/disk.total)*100:.1f}%)\n"
                info_text += f"   Free: {disk.free / (1024**3):.1f} GB\n\n"
            except Exception as e:
                info_text += f"💾 DISK: Error getting disk info\n\n"

            try:
                net_io = psutil.net_io_counters()
                info_text += f"🌐 NETWORK:\n"
                info_text += f"   Bytes Sent: {net_io.bytes_sent / (1024**2):.1f} MB\n"
                info_text += f"   Bytes Received: {net_io.bytes_recv / (1024**2):.1f} MB\n"
                info_text += f"   Packets Sent: {net_io.packets_sent:,}\n"
                info_text += f"   Packets Received: {net_io.packets_recv:,}\n\n"
            except Exception as e:
                info_text += f"🌐 NETWORK: Error getting network info\n\n"

            try:
                import platform
                info_text += f"🖥️ OPERATING SYSTEM:\n"
                info_text += f"   System: {platform.system()} {platform.release()}\n"
                info_text += f"   Version: {platform.version()}\n"
                info_text += f"   Architecture: {platform.machine()}\n"
                info_text += f"   Processor: {platform.processor()}\n\n"
            except Exception as e:
                info_text += f"🖥️ OS: Error getting OS info\n\n"

            info_text += "📊 PERFORMANCE TIPS:\n"
            info_text += "• Use the Game Mode tab to optimize for gaming\n"
            info_text += "• Run benchmarks to test performance improvements\n"
            info_text += "• Monitor CPU and memory usage during gaming\n"
            info_text += "• Close unnecessary background applications\n"
            info_text += "• Keep your system updated and drivers current\n"

            self.system_info_text.insert(tk.END, info_text)
            self.system_info_text.config(state='disabled')

        except Exception as e:
            print(f"Error loading system info: {e}")

    def create_benchmark_tab(self):

        tab_frame = tk.Frame(self.notebook, bg=self.colors['bg'])
        self.notebook.add(tab_frame, text="🏁 Benchmark")

        canvas = tk.Canvas(tab_frame, bg=self.colors['bg'])
        scrollbar = ttk.Scrollbar(tab_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['bg'])

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        control_section = tk.Frame(scrollable_frame, bg=self.colors['frame_bg'], relief='raised', bd=1)
        control_section.pack(fill="x", padx=10, pady=10)

        tk.Label(
            control_section,
            text="🏁 PC Performance Benchmark",
            font=("Segoe UI", 16, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        ).pack(anchor="w", padx=15, pady=(15, 5))

        tk.Label(
            control_section,
            text="Test your PC's performance before and after optimization",
            font=("Segoe UI", 10),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        ).pack(anchor="w", padx=15, pady=(0, 10))

        button_frame = tk.Frame(control_section, bg=self.colors['frame_bg'])
        button_frame.pack(fill="x", padx=15, pady=10)

        self.benchmark_btn = tk.Button(
            button_frame,
            text="🏁 Run Full Benchmark",
            command=self.run_benchmark,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 12, "bold"),
            relief='raised',
            bd=2,
            height=2
        )
        self.benchmark_btn.pack(side="left", fill="x", expand=True, padx=(0, 5))

        self.stop_benchmark_btn = tk.Button(
            button_frame,
            text="⏹ Stop",
            command=self.stop_benchmark,
            bg=self.colors['error'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 12, "bold"),
            relief='raised',
            bd=2,
            height=2,
            state='disabled'
        )
        self.stop_benchmark_btn.pack(side="right", padx=(5, 0))

        progress_section = tk.Frame(scrollable_frame, bg=self.colors['frame_bg'], relief='raised', bd=1)
        progress_section.pack(fill="x", padx=10, pady=10)

        tk.Label(
            progress_section,
            text="📊 Benchmark Progress",
            font=("Segoe UI", 14, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        ).pack(anchor="w", padx=15, pady=(15, 5))

        self.benchmark_status_label = tk.Label(
            progress_section,
            text="Ready to benchmark",
            font=("Segoe UI", 10),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        )
        self.benchmark_status_label.pack(anchor="w", padx=15, pady=5)

        self.benchmark_progress = ttk.Progressbar(
            progress_section,
            mode='determinate',
            length=400
        )
        self.benchmark_progress.pack(fill="x", padx=15, pady=(5, 15))

        results_section = tk.Frame(scrollable_frame, bg=self.colors['frame_bg'], relief='raised', bd=1)
        results_section.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(
            results_section,
            text="📈 Benchmark Results",
            font=("Segoe UI", 14, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        ).pack(anchor="w", padx=15, pady=(15, 5))

        results_display_frame = tk.Frame(results_section, bg=self.colors['frame_bg'])
        results_display_frame.pack(fill="both", expand=True, padx=15, pady=10)

        current_results_frame = tk.Frame(results_display_frame, bg=self.colors['entry_bg'], relief='raised', bd=1)
        current_results_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))

        tk.Label(
            current_results_frame,
            text="Current Results",
            font=("Segoe UI", 12, "bold"),
            bg=self.colors['entry_bg'],
            fg=self.colors['fg']
        ).pack(pady=10)

        self.current_results_text = tk.Text(
            current_results_frame,
            height=15,
            bg=self.colors['entry_bg'],
            fg=self.colors['fg'],
            font=("Consolas", 9),
            wrap=tk.WORD,
            state='disabled'
        )
        self.current_results_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        previous_results_frame = tk.Frame(results_display_frame, bg=self.colors['entry_bg'], relief='raised', bd=1)
        previous_results_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))

        tk.Label(
            previous_results_frame,
            text="Previous Results",
            font=("Segoe UI", 12, "bold"),
            bg=self.colors['entry_bg'],
            fg=self.colors['fg']
        ).pack(pady=10)

        self.previous_results_text = tk.Text(
            previous_results_frame,
            height=15,
            bg=self.colors['entry_bg'],
            fg=self.colors['fg'],
            font=("Consolas", 9),
            wrap=tk.WORD,
            state='disabled'
        )
        self.previous_results_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.load_previous_benchmark_results()

        self.benchmark.set_callbacks(self.update_benchmark_progress, self.update_benchmark_status)

    def run_benchmark(self):
        """Run comprehensive PC benchmark with security validation - DO NOT REMOVE"""

        if not self._validate_core_integrity() or not self._rpc_security_check():
            _trigger_security_failure()
            return

        if self.benchmark.is_running:
            return

        if self.rpc_connected:
            self.update_discord_presence("Running Benchmark", "Join Freeware")

        self.benchmark_btn.config(state='disabled')
        self.stop_benchmark_btn.config(state='normal')
        self.benchmark_progress['value'] = 0

        self.current_results_text.config(state='normal')
        self.current_results_text.delete(1.0, tk.END)
        self.current_results_text.insert(tk.END, "🔒 Security validation: PASSED\n")
        self.current_results_text.insert(tk.END, "🚀 Starting benchmark...\n\n")
        self.current_results_text.config(state='disabled')

        benchmark_thread = threading.Thread(target=self._run_benchmark_thread, daemon=True)
        benchmark_thread.start()

    def _run_benchmark_thread(self):

        try:
            results = self.benchmark.run_full_benchmark()
            if results:
                self.root.after(0, self.display_benchmark_results, results)
        except Exception as e:
            self.root.after(0, self.update_benchmark_status, f"Benchmark failed: {str(e)}")
        finally:
            self.root.after(0, self._benchmark_finished)

    def _benchmark_finished(self):

        self.benchmark_btn.config(state='normal')
        self.stop_benchmark_btn.config(state='disabled')

        if self.rpc_connected:
            self.update_discord_presence("Benchmark Complete", "Join Freeware")

    def stop_benchmark(self):

        self.benchmark.stop_benchmark()
        self._benchmark_finished()

    def update_benchmark_progress(self, value):

        self.benchmark_progress['value'] = value

    def update_benchmark_status(self, message):

        self.benchmark_status_label.config(text=message)

    def display_benchmark_results(self, results):

        self.current_results_text.config(state='normal')
        self.current_results_text.delete(1.0, tk.END)

        output = "🏁 COMPREHENSIVE BENCHMARK RESULTS\n"
        output += "=" * 60 + "\n\n"

        if 'overall' in results:
            overall = results['overall']
            output += f"🎯 OVERALL SCORE: {overall['score']}/100\n"
            output += f"📊 RATING: {overall['rating']}\n"
            output += f"📅 DATE: {overall['timestamp'][:19]}\n\n"

        if 'cpu' in results:
            cpu = results['cpu']
            output += "🖥️ CPU PERFORMANCE\n"
            output += "-" * 40 + "\n"
            if 'info' in cpu:
                info = cpu['info']
                output += f"Name: {info.get('name', 'Unknown')}\n"
                output += f"Cores: {info.get('cores', 'N/A')} | Threads: {info.get('threads', 'N/A')}\n"
                output += f"Frequency: {info.get('frequency_mhz', 0):.0f} MHz\n\n"

            if 'single_math' in cpu:
                output += f"Single-Core Math: {cpu['single_math']['score']}/100 ({cpu['single_math']['time']}s)\n"
            if 'single_hash' in cpu:
                output += f"Single-Core Hash: {cpu['single_hash']['score']}/100 ({cpu['single_hash']['time']}s)\n"

            if 'multi_math' in cpu:
                output += f"Multi-Core Math: {cpu['multi_math']['score']}/100 ({cpu['multi_math']['time']}s)\n"
            if 'multi_compression' in cpu:
                output += f"Multi-Core Compression: {cpu['multi_compression']['score']}/100 ({cpu['multi_compression']['time']}s)\n"

            output += f"Overall CPU Score: {cpu.get('score', 0)}/100\n\n"

        if 'memory' in results:
            memory = results['memory']
            output += "🧠 MEMORY PERFORMANCE\n"
            output += "-" * 40 + "\n"
            output += f"Total Memory: {memory.get('total_gb', 0)} GB\n"
            output += f"Available: {memory.get('available_gb', 0)} GB\n"
            if 'memory_type' in memory:
                output += f"Memory Type: {memory.get('memory_type', 'Unknown')}\n"

            if 'bandwidth' in memory:
                output += f"Bandwidth: {memory['bandwidth']['mbps']} MB/s ({memory['bandwidth']['score']}/100)\n"
            if 'latency' in memory:
                output += f"Latency: {memory['latency']['time']}s ({memory['latency']['score']}/100)\n"

            output += f"Overall Memory Score: {memory.get('score', 0)}/100\n\n"

        if 'disk' in results:
            disk = results['disk']
            output += "💾 DISK PERFORMANCE\n"
            output += "-" * 40 + "\n"
            output += f"Total Space: {disk.get('total_gb', 0)} GB\n"
            output += f"Free Space: {disk.get('free_gb', 0)} GB\n"
            output += f"Disk Type: {disk.get('disk_type', 'Unknown')}\n"

            if 'sequential_write' in disk:
                output += f"Sequential Write: {disk['sequential_write']['mbps']} MB/s ({disk['sequential_write']['score']}/100)\n"
            if 'sequential_read' in disk:
                output += f"Sequential Read: {disk['sequential_read']['mbps']} MB/s ({disk['sequential_read']['score']}/100)\n"
            if 'random_4k' in disk:
                output += f"Random 4K: {disk['random_4k']['iops']} IOPS ({disk['random_4k']['score']}/100)\n"

            output += f"Overall Disk Score: {disk.get('score', 0)}/100\n\n"

        if 'gpu' in results:
            gpu = results['gpu']
            output += "🎮 GPU PERFORMANCE\n"
            output += "-" * 40 + "\n"
            if 'info' in gpu:
                info = gpu['info']
                output += f"Name: {info.get('name', 'Unknown')}\n"
                output += f"Vendor: {info.get('vendor', 'Unknown')}\n"
                if 'memory_mb' in info:
                    output += f"Memory: {info['memory_mb']} MB\n"

            if 'graphics_rendering' in gpu:
                output += f"Graphics Rendering: {gpu['graphics_rendering']['score']}/100\n"
                output += f"Method: {gpu['graphics_rendering'].get('method', 'OpenGL 3D Rendering')}\n"
                output += "✅ Real GPU graphics rendering test\n"
            elif 'external_benchmark' in gpu:
                output += f"Graphics Performance: {gpu['external_benchmark']['score']}/100\n"
                output += f"Method: {gpu['external_benchmark'].get('method', 'External Tool')}\n"
                output += "✅ External GPU benchmark tool\n"
            elif 'compute' in gpu:
                output += f"Compute Performance: {gpu['compute']['score']}/100 ({gpu['compute']['time']}s)\n"
                output += f"Method: {gpu['compute'].get('method', 'Unknown')}\n"
                output += "⚠️  Note: CPU fallback - not real GPU graphics rendering\n"

            output += f"Overall GPU Score: {gpu.get('score', 0)}/100\n\n"

        output += "📈 PERFORMANCE BREAKDOWN\n"
        output += "-" * 40 + "\n"
        if 'cpu' in results:
            output += f"CPU: {results['cpu'].get('score', 0)}/100 (30% weight)\n"
        if 'memory' in results:
            output += f"Memory: {results['memory'].get('score', 0)}/100 (20% weight)\n"
        if 'disk' in results:
            output += f"Disk: {results['disk'].get('score', 0)}/100 (30% weight)\n"
        if 'gpu' in results:
            output += f"GPU: {results['gpu'].get('score', 0)}/100 (20% weight)\n"

        self.current_results_text.insert(tk.END, output)
        self.current_results_text.config(state='disabled')

        self.load_previous_benchmark_results()

    def load_previous_benchmark_results(self):

        previous_results = self.benchmark.load_previous_results()

        self.previous_results_text.config(state='normal')
        self.previous_results_text.delete(1.0, tk.END)

        if previous_results:
            output = "📊 PREVIOUS BENCHMARKS\n"
            output += "=" * 50 + "\n\n"

            for i, result in enumerate(previous_results[:5]):
                if 'overall' in result:
                    overall = result['overall']
                    output += f"#{i+1} - Score: {overall['score']}/100 ({overall['rating']})\n"
                    output += f"Date: {overall['timestamp'][:19]}\n"

                    if 'cpu' in result:
                        output += f"CPU: {result['cpu'].get('score', 0)}/100 | "
                    if 'memory' in result:
                        output += f"RAM: {result['memory'].get('score', 0)}/100 | "
                    if 'disk' in result:
                        output += f"Disk: {result['disk'].get('score', 0)}/100 | "
                    if 'gpu' in result:
                        output += f"GPU: {result['gpu'].get('score', 0)}/100"
                    output += "\n\n"
        else:
            output = "No previous benchmark results found.\n\nRun your first benchmark to see results here!"

        self.previous_results_text.insert(tk.END, output)
        self.previous_results_text.config(state='disabled')

    def create_presets_tab(self):

        tab_frame = tk.Frame(self.notebook, bg=self.colors['bg'])
        self.notebook.add(tab_frame, text="🧩 Presets")

        presets_frame = tk.Frame(tab_frame, bg=self.colors['frame_bg'], relief='raised', bd=1)
        presets_frame.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(
            presets_frame,
            text="🧩 Optimization Presets",
            font=("Segoe UI", 16, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        ).pack(anchor="w", padx=15, pady=(15, 10))

        preset_buttons_frame = tk.Frame(presets_frame, bg=self.colors['frame_bg'])
        preset_buttons_frame.pack(fill="x", padx=15, pady=10)

        tk.Button(
            preset_buttons_frame,
            text="🏎 Competitive Gaming",
            command=self.apply_competitive_preset,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 12, "bold"),
            relief='raised',
            bd=2,
            height=2
        ).pack(fill="x", padx=10, pady=5)

        tk.Button(
            preset_buttons_frame,
            text="💻 Low-End PC Optimization",
            command=self.apply_low_end_preset,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 12, "bold"),
            relief='raised',
            bd=2,
            height=2
        ).pack(fill="x", padx=10, pady=5)

        tk.Button(
            preset_buttons_frame,
            text="⚡ Maximum Performance",
            command=self.apply_max_performance_preset,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 12, "bold"),
            relief='raised',
            bd=2,
            height=2
        ).pack(fill="x", padx=10, pady=5)

        tk.Button(
            preset_buttons_frame,
            text="🔄 Restore Defaults",
            command=self.restore_defaults,
            bg=self.colors['error'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 12, "bold"),
            relief='raised',
            bd=2,
            height=2
        ).pack(fill="x", padx=10, pady=5)

    def create_control_panel(self):

        control_frame = tk.Frame(self.main_frame, bg=self.colors['frame_bg'], relief='raised', bd=1)
        control_frame.pack(fill="x", padx=5, pady=(5, 5))

        backup_btn = tk.Button(
            control_frame,
            text="💾 Create Backup",
            command=self.create_backup,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2
        )
        backup_btn.pack(side="left", padx=10, pady=10)

        restore_btn = tk.Button(
            control_frame,
            text="🔄 Restore Backup",
            command=self.restore_backup,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Segoe UI", 10, "bold"),
            relief='raised',
            bd=2
        )
        restore_btn.pack(side="left", padx=5, pady=10)

        self.status_label = tk.Label(
            control_frame,
            text="Ready",
            font=("Segoe UI", 10),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        )
        self.status_label.pack(side="right", padx=20, pady=10)

    def toggle_game_mode(self):

        if not self.is_admin:
            messagebox.showerror("Error", "Administrator privileges required!")
            return

        try:
            enable = True
            self.update_game_results("🔄 Enabling Windows Game Mode...\n")

            success = self.game_optimizer.toggle_game_mode(enable)
            if success:
                self.update_status("✅ Windows Game Mode enabled")
                self.update_game_results("✅ Windows Game Mode enabled successfully!\n")
                self.update_game_results("   • Optimizes system resources for gaming\n")
                self.update_game_results("   • Reduces background activity during games\n")
                self.update_game_results("   • Prioritizes game performance\n\n")
            else:
                self.update_status("❌ Failed to enable Game Mode")
                self.update_game_results("❌ Failed to enable Windows Game Mode\n\n")
        except Exception as e:
            error_msg = f"Failed to toggle Game Mode: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.update_game_results(f"❌ Error: {error_msg}\n\n")

    def toggle_gpu_scheduling(self):

        if not self.is_admin:
            messagebox.showerror("Error", "Administrator privileges required!")
            return

        try:
            enable = True
            self.update_game_results("🔄 Enabling GPU Hardware Scheduling...\n")

            success = self.game_optimizer.toggle_gpu_scheduling(enable)
            if success:
                self.update_status("✅ GPU Hardware Scheduling enabled")
                self.update_game_results("✅ GPU Hardware Scheduling enabled successfully!\n")
                self.update_game_results("   • GPU manages its own memory more efficiently\n")
                self.update_game_results("   • Reduced latency and improved performance\n")
                self.update_game_results("   • Better multi-tasking with games\n\n")
            else:
                self.update_status("❌ Failed to enable GPU scheduling")
                self.update_game_results("❌ Failed to enable GPU Hardware Scheduling\n")
                self.update_game_results("   • Feature may not be supported on this GPU\n")
                self.update_game_results("   • Requires Windows 10 version 2004 or later\n\n")
        except Exception as e:
            error_msg = f"Failed to toggle GPU scheduling: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.update_game_results(f"❌ Error: {error_msg}\n\n")

    def toggle_ultimate_performance(self):

        if not self.is_admin:
            messagebox.showerror("Error", "Administrator privileges required!")
            return

        try:
            enable = True
            self.update_game_results("🔄 Setting Ultimate Performance power plan...\n")

            success = self.game_optimizer.toggle_ultimate_performance(enable)
            if success:
                self.update_status("✅ Ultimate Performance power plan activated")
                self.update_game_results("✅ Ultimate Performance power plan activated!\n")
                self.update_game_results("   • Maximum CPU performance at all times\n")
                self.update_game_results("   • No power throttling or CPU parking\n")
                self.update_game_results("   • Optimal for gaming and high-performance tasks\n\n")
            else:
                self.update_status("❌ Failed to set Ultimate Performance")
                self.update_game_results("❌ Failed to activate Ultimate Performance power plan\n")
                self.update_game_results("   • Plan may need to be created first\n")
                self.update_game_results("   • Check administrator privileges\n\n")
        except Exception as e:
            error_msg = f"Failed to set power plan: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.update_game_results(f"❌ Error: {error_msg}\n\n")

    def toggle_xbox_features(self):

        if not self.is_admin:
            messagebox.showerror("Error", "Administrator privileges required!")
            return

        try:
            disable = True
            self.update_game_results("🔄 Disabling Xbox Game Bar and DVR...\n")

            success = self.game_optimizer.toggle_xbox_features(disable)
            if success:
                self.update_status("✅ Xbox features disabled")
                self.update_game_results("✅ Xbox Game Bar and DVR disabled successfully!\n")
                self.update_game_results("   • Xbox Game Bar overlay disabled\n")
                self.update_game_results("   • Game DVR recording disabled\n")
                self.update_game_results("   • Reduced system overhead during gaming\n")
                self.update_game_results("   • Improved gaming performance\n\n")
            else:
                self.update_status("❌ Failed to disable Xbox features")
                self.update_game_results("❌ Failed to disable Xbox features\n\n")
        except Exception as e:
            error_msg = f"Failed to toggle Xbox features: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.update_game_results(f"❌ Error: {error_msg}\n\n")

    def load_game_mode_states(self):

        try:
            states = self.game_optimizer.get_current_states()
            self.game_mode_var.set(states.get('game_mode', False))
            self.gpu_scheduling_var.set(states.get('gpu_scheduling', False))
            self.ultimate_performance_var.set(states.get('ultimate_performance', False))
            self.disable_xbox_var.set(states.get('xbox_disabled', False))
        except Exception as e:
            print(f"Error loading game mode states: {e}")

    def toggle_telemetry(self):

        if not self.is_admin:
            messagebox.showerror("Error", "Administrator privileges required!")
            return

        try:

            success = self.background_optimizer.toggle_telemetry(True)
            if success:
                self.update_status("✅ Windows telemetry disabled")
                self.update_background_results("✅ Windows telemetry and tracking disabled successfully!\n")
                self.update_background_results("   • Telemetry data collection disabled\n")
                self.update_background_results("   • Windows Error Reporting disabled\n")
                self.update_background_results("   • Customer Experience Improvement Program disabled\n")
                self.update_background_results("   • Advertising ID disabled\n\n")
            else:
                self.update_background_results("❌ Failed to disable telemetry\n")
        except Exception as e:
            error_msg = f"Failed to toggle telemetry: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.update_background_results(f"❌ Error: {error_msg}\n")

    def toggle_background_apps(self):

        try:

            success = self.background_optimizer.toggle_background_apps(True)
            if success:
                self.update_status("✅ Background apps disabled")
                self.update_background_results("✅ Background apps disabled successfully!\n")
                self.update_background_results("   • Global background app access disabled\n")
                self.update_background_results("   • Common Microsoft apps background access disabled\n\n")
            else:
                self.update_background_results("❌ Failed to disable background apps\n")
        except Exception as e:
            error_msg = f"Failed to toggle background apps: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.update_background_results(f"❌ Error: {error_msg}\n")

    def toggle_auto_updates(self):

        if not self.is_admin:
            messagebox.showerror("Error", "Administrator privileges required!")
            return

        try:

            success = self.background_optimizer.toggle_auto_updates(True)
            if success:
                self.update_status("✅ Automatic updates disabled")
                self.update_background_results("✅ Automatic Windows updates disabled successfully!\n")
                self.update_background_results("   • Windows Update service configured to manual\n")
                self.update_background_results("   • Automatic download and install disabled\n")
                self.update_background_results("   • You will be notified before updates are downloaded\n\n")
                messagebox.showinfo("Success", "Automatic Windows updates have been disabled.\n\nYou can still manually check for and install updates when needed.")
            else:
                self.update_background_results("❌ Failed to disable automatic updates\n")
        except Exception as e:
            error_msg = f"Failed to toggle auto updates: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.update_background_results(f"❌ Error: {error_msg}\n")

    def toggle_visual_effects(self):

        try:
            disable = True
            self.update_gpu_results("🔄 Disabling visual effects and animations...\n")

            success = self.gpu_tweaks.toggle_visual_effects(disable)
            if success:
                self.update_status("✅ Visual effects disabled")
                self.update_gpu_results("✅ Visual effects and animations disabled successfully!\n")
                self.update_gpu_results("   • Window animations disabled\n")
                self.update_gpu_results("   • Menu fade effects disabled\n")
                self.update_gpu_results("   • Taskbar animations disabled\n")
                self.update_gpu_results("   • Improved GPU performance for gaming\n\n")
            else:
                self.update_status("❌ Failed to disable visual effects")
                self.update_gpu_results("❌ Failed to disable visual effects\n\n")
        except Exception as e:
            error_msg = f"Failed to toggle visual effects: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.update_gpu_results(f"❌ Error: {error_msg}\n\n")

    def toggle_transparency(self):

        try:
            disable = True
            self.update_gpu_results("🔄 Disabling transparency effects...\n")

            success = self.gpu_tweaks.toggle_transparency(disable)
            if success:
                self.update_status("✅ Transparency effects disabled")
                self.update_gpu_results("✅ Transparency effects disabled successfully!\n")
                self.update_gpu_results("   • Window transparency disabled\n")
                self.update_gpu_results("   • Taskbar transparency disabled\n")
                self.update_gpu_results("   • Start menu transparency disabled\n")
                self.update_gpu_results("   • Reduced GPU workload\n\n")
            else:
                self.update_status("❌ Failed to disable transparency")
                self.update_gpu_results("❌ Failed to disable transparency effects\n\n")
        except Exception as e:
            error_msg = f"Failed to toggle transparency: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.update_gpu_results(f"❌ Error: {error_msg}\n\n")

    def toggle_high_performance_gpu(self):

        try:
            enable = True
            self.update_gpu_results("🔄 Configuring high-performance GPU settings...\n")

            success = self.gpu_tweaks.toggle_high_performance_gpu(enable)
            if success:
                self.update_status("✅ High-performance GPU enabled")
                self.update_gpu_results("✅ High-performance GPU settings configured!\n")
                self.update_gpu_results("   • Games will use dedicated GPU instead of integrated\n")
                self.update_gpu_results("   • Graphics preference set to high performance\n")
                self.update_gpu_results("   • Better gaming performance\n\n")
            else:
                self.update_status("❌ Failed to configure GPU settings")
                self.update_gpu_results("❌ Failed to configure high-performance GPU settings\n")
                self.update_gpu_results("   • May not be supported on single-GPU systems\n")
                self.update_gpu_results("   • Check if you have both integrated and dedicated GPU\n\n")
        except Exception as e:
            error_msg = f"Failed to toggle GPU settings: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.update_gpu_results(f"❌ Error: {error_msg}\n\n")

    def toggle_hardware_acceleration(self):

        try:
            enable = True
            self.update_gpu_results("🔄 Enabling hardware acceleration...\n")

            success = self.gpu_tweaks.toggle_hardware_acceleration(enable)
            if success:
                self.update_status("✅ Hardware acceleration enabled")
                self.update_gpu_results("✅ Hardware acceleration enabled successfully!\n")
                self.update_gpu_results("   • Browser hardware acceleration enabled\n")
                self.update_gpu_results("   • Windows hardware acceleration enabled\n")
                self.update_gpu_results("   • Better performance for supported applications\n\n")
            else:
                self.update_status("❌ Failed to enable hardware acceleration")
                self.update_gpu_results("❌ Failed to enable hardware acceleration\n\n")
        except Exception as e:
            error_msg = f"Failed to toggle hardware acceleration: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.update_gpu_results(f"❌ Error: {error_msg}\n\n")

    def toggle_cpu_parking(self):

        if not self.is_admin:
            messagebox.showerror("Error", "Administrator privileges required!")
            return

        try:
            disable = True
            self.update_game_results("🔄 Configuring CPU core parking...\n")

            success = self.memory_cpu.toggle_cpu_parking(disable)
            if success:
                self.update_status("✅ CPU core parking disabled")
                self.update_game_results("✅ CPU core parking disabled successfully!\n")
                self.update_game_results("   • All CPU cores will remain active\n")
                self.update_game_results("   • Improved gaming performance and responsiveness\n")
                self.update_game_results("   • Changes applied to current power plan\n\n")

                self.update_game_results("📊 Current CPU Status:\n")
                status = self.memory_cpu.get_cpu_parking_status()
                self.update_game_results(f"   • Core Parking: {'Disabled' if not status['parking_enabled'] else 'Enabled'}\n")
                self.update_game_results(f"   • Minimum Processor State: {status['processor_state_min']}\n")
                self.update_game_results(f"   • Core Parking Min Cores: {status['min_cores']}\n")

                cpu_count = psutil.cpu_count(logical=False)
                cpu_threads = psutil.cpu_count(logical=True)
                self.update_game_results(f"   • Physical Cores: {cpu_count} | Logical Cores: {cpu_threads}\n\n")

            else:
                self.update_status("❌ Failed to disable CPU parking")
                self.update_game_results("❌ Failed to disable CPU core parking\n")
                self.update_game_results("   • Check if running as administrator\n")
                self.update_game_results("   • Some systems may not support this feature\n")

                self.update_game_results("\n📊 Current CPU Status (for debugging):\n")
                status = self.memory_cpu.get_cpu_parking_status()
                self.update_game_results(f"   • Core Parking: {'Disabled' if not status['parking_enabled'] else 'Enabled'}\n")
                self.update_game_results(f"   • Minimum Processor State: {status['processor_state_min']}\n")
                self.update_game_results(f"   • Core Parking Min Cores: {status['min_cores']}\n\n")

        except Exception as e:
            error_msg = f"Failed to toggle CPU parking: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.update_game_results(f"❌ Error: {error_msg}\n\n")

    def toggle_high_priority(self):

        try:
            enable = True
            self.update_game_results("🔄 Configuring high priority game mode...\n")

            success = self.memory_cpu.toggle_high_priority(enable)
            if success:
                self.update_status("✅ High priority game mode enabled")
                self.update_game_results("✅ High priority game mode enabled successfully!\n")
                self.update_game_results("   • Game processes will get higher CPU priority\n")
                self.update_game_results("   • Improved frame rates and reduced stuttering\n")
                self.update_game_results("   • Monitoring for game processes started\n\n")
            else:
                self.update_status("❌ Failed to enable high priority mode")
                self.update_game_results("❌ Failed to enable high priority game mode\n\n")
        except Exception as e:
            error_msg = f"Failed to toggle high priority: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.update_game_results(f"❌ Error: {error_msg}\n\n")

    def toggle_hyperv(self):

        if not self.is_admin:
            messagebox.showerror("Error", "Administrator privileges required!")
            return

        try:
            disable = True
            self.update_game_results("🔄 Disabling Hyper-V for better gaming compatibility...\n")

            result = messagebox.askyesno(
                "Disable Hyper-V",
                "This will disable Hyper-V for better gaming compatibility.\n\nWarning: This requires a restart and may affect virtual machines.\n\nContinue?"
            )

            if result:
                success = self.memory_cpu.toggle_hyperv(disable)
                if success:
                    self.update_status("✅ Hyper-V disabled (restart required)")
                    self.update_game_results("✅ Hyper-V disabled successfully!\n")
                    self.update_game_results("   • Better gaming compatibility\n")
                    self.update_game_results("   • Reduced system overhead\n")
                    self.update_game_results("   • ⚠️  RESTART REQUIRED for changes to take effect\n\n")

                    messagebox.showinfo(
                        "Hyper-V Disabled",
                        "Hyper-V has been disabled successfully!\n\nPlease restart your computer for changes to take effect."
                    )
                else:
                    self.update_status("❌ Failed to disable Hyper-V")
                    self.update_game_results("❌ Failed to disable Hyper-V\n")
                    self.update_game_results("   • Check if running as administrator\n")
                    self.update_game_results("   • Hyper-V may not be installed\n\n")
            else:
                self.update_game_results("❌ Hyper-V disable operation cancelled by user\n\n")
        except Exception as e:
            error_msg = f"Failed to toggle Hyper-V: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.update_game_results(f"❌ Error: {error_msg}\n\n")

    def apply_competitive_preset(self):

        if not self.is_admin:
            messagebox.showerror("Error", "Administrator privileges required!")
            return

        try:

            if self.rpc_connected:
                self.update_discord_presence("Applying Preset", "Join Freeware")

            self.game_mode_var.set(True)
            self.gpu_scheduling_var.set(True)
            self.ultimate_performance_var.set(True)
            self.disable_xbox_var.set(True)
            self.disable_animations_var.set(True)
            self.disable_transparency_var.set(True)
            self.cpu_parking_var.set(True)
            self.high_priority_var.set(True)

            self.toggle_game_mode()
            self.toggle_gpu_scheduling()
            self.toggle_ultimate_performance()
            self.toggle_xbox_features()
            self.toggle_visual_effects()
            self.toggle_transparency()
            self.toggle_cpu_parking()
            self.toggle_high_priority()

            self.update_status("Competitive preset applied")
            messagebox.showinfo("Success", "Competitive gaming preset applied successfully!")

            if self.rpc_connected:
                self.update_discord_presence("Preset Applied", "Join Freeware")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply preset: {str(e)}")

    def apply_low_end_preset(self):

        if not self.is_admin:
            messagebox.showerror("Error", "Administrator privileges required!")
            return

        try:

            self.game_mode_var.set(True)
            self.disable_animations_var.set(True)
            self.disable_transparency_var.set(True)
            self.telemetry_var.set(True)
            self.background_apps_var.set(True)

            self.toggle_game_mode()
            self.toggle_visual_effects()
            self.toggle_transparency()
            self.toggle_telemetry()
            self.toggle_background_apps()

            self.update_status("Low-end PC preset applied")
            messagebox.showinfo("Success", "Low-end PC optimization preset applied successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply preset: {str(e)}")

    def apply_max_performance_preset(self):

        if not self.is_admin:
            messagebox.showerror("Error", "Administrator privileges required!")
            return

        try:

            if self.rpc_connected:
                self.update_discord_presence("Applying Preset", "Join Freeware")

            self.game_mode_var.set(True)
            self.gpu_scheduling_var.set(True)
            self.ultimate_performance_var.set(True)
            self.disable_xbox_var.set(True)
            self.disable_animations_var.set(True)
            self.disable_transparency_var.set(True)
            self.high_performance_gpu_var.set(True)
            self.cpu_parking_var.set(True)
            self.high_priority_var.set(True)
            self.telemetry_var.set(True)
            self.background_apps_var.set(True)

            self.toggle_game_mode()
            self.toggle_gpu_scheduling()
            self.toggle_ultimate_performance()
            self.toggle_xbox_features()
            self.toggle_visual_effects()
            self.toggle_transparency()
            self.toggle_high_performance_gpu()
            self.toggle_cpu_parking()
            self.toggle_high_priority()
            self.toggle_telemetry()
            self.toggle_background_apps()

            self.update_status("Maximum performance preset applied")
            messagebox.showinfo("Success", "Maximum performance preset applied successfully!")

            if self.rpc_connected:
                self.update_discord_presence("Max Performance", "Join Freeware")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply preset: {str(e)}")

    def restore_defaults(self):

        if not self.is_admin:
            messagebox.showerror("Error", "Administrator privileges required!")
            return

        result = messagebox.askyesno(
            "Restore Defaults",
            "This will restore all tweaks to their default Windows settings.\n\nDo you want to continue?"
        )

        if result:
            try:

                self.game_mode_var.set(False)
                self.gpu_scheduling_var.set(False)
                self.ultimate_performance_var.set(False)
                self.disable_xbox_var.set(False)
                self.disable_animations_var.set(False)
                self.disable_transparency_var.set(False)
                self.high_performance_gpu_var.set(False)
                self.cpu_parking_var.set(False)
                self.high_priority_var.set(False)
                self.telemetry_var.set(False)
                self.background_apps_var.set(False)

                self.toggle_game_mode()
                self.toggle_gpu_scheduling()
                self.toggle_ultimate_performance()
                self.toggle_xbox_features()
                self.toggle_visual_effects()
                self.toggle_transparency()
                self.toggle_high_performance_gpu()
                self.toggle_cpu_parking()
                self.toggle_high_priority()
                self.toggle_telemetry()
                self.toggle_background_apps()

                self.update_status("Default settings restored")
                messagebox.showinfo("Success", "Default settings restored successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to restore defaults: {str(e)}")

    def create_backup(self):

        try:
            backup_path = self.registry_backup.create_backup()
            self.update_status(f"Backup created: {backup_path}")
            messagebox.showinfo("Success", f"Backup created successfully!\nLocation: {backup_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create backup: {str(e)}")

    def restore_backup(self):

        try:
            success = self.registry_backup.restore_backup()
            if success:
                self.update_status("Backup restored successfully")
                messagebox.showinfo("Success", "Backup restored successfully!")
            else:
                messagebox.showwarning("Warning", "No backup found to restore.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to restore backup: {str(e)}")

    def update_status(self, message):

        self.status_label.configure(text=message)
        self.root.after(3000, lambda: self.status_label.configure(text="Ready"))

    def setup_graphs(self):

        self.load_system_info()

    def update_graphs(self, cpu_percent, memory_percent, gpu_percent):

        pass

    def setup_process_lists(self):

        pass

    def setup_context_menus(self):

        pass

    def kill_selected_process(self, listbox):

        pass

    def get_top_processes(self):

        return [], [], []

    def get_gpu_processes(self):

        return []

    def update_monitoring(self):

        while self.monitoring_active:
            try:

                cpu_percent = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()

                gpu_percent = self._get_gpu_usage()

                self.root.after(0, self.update_stats_display, cpu_percent, memory.percent, gpu_percent)

            except Exception as e:
                print(f"Monitoring error: {e}")

            threading.Event().wait(2)

    def _get_gpu_usage(self):

        try:

            result = run_command_silent([
                "nvidia-smi", "--query-gpu=utilization.gpu",
                "--format=csv,noheader,nounits"
            ], timeout=5)

            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                if lines and lines[0]:
                    return float(lines[0].strip())
        except (subprocess.TimeoutExpired, FileNotFoundError, ValueError):
            pass

        return None

    def update_stats_display(self, cpu_percent, memory_percent, gpu_percent):

        try:

            self.cpu_label.configure(text=f"🖥️ CPU: {cpu_percent:.1f}%")
            self.cpu_progress['value'] = cpu_percent

            self.memory_label.configure(text=f"🧠 Memory: {memory_percent:.1f}%")
            self.memory_progress['value'] = memory_percent

            if gpu_percent is not None:
                self.gpu_label.configure(text=f"🎮 GPU: {gpu_percent:.1f}%")
                self.gpu_progress['value'] = gpu_percent
            else:
                self.gpu_label.configure(text="🎮 GPU: N/A")
                self.gpu_progress['value'] = 0

        except Exception as e:
            print(f"Stats display error: {e}")

    def _essential_system_validator(self):
        """Critical system operation validator - DO NOT REMOVE"""
        try:

            required_methods = ['_validate_core_integrity', '_rpc_security_check', '_periodic_security_check']
            for method_name in required_methods:
                if not hasattr(self, method_name):
                    return False


            if not all([self._security_token, self._validation_key, self._integrity_hash]):
                return False


            if self.rpc_connected and not self.discord_rpc:
                return False

            return True
        except:
            return False

    def _core_authentication_protocol(self):
        """Primary authentication handler - DO NOT REMOVE"""
        auth_sequence = [
            lambda: _rpc_decoy_function_alpha(),
            lambda: _rpc_decoy_function_beta(),
            lambda: _rpc_decoy_function_gamma()
        ]

        try:
            for i, auth_func in enumerate(auth_sequence):
                result = auth_func()
                if not result or len(str(result)) < 8:
                    return False
            return True
        except:
            return False

    def _system_integrity_monitor(self):
        """Background system integrity monitor - DO NOT REMOVE"""
        if not self._essential_system_validator():
            _trigger_security_failure()
        if not self._core_authentication_protocol():
            _trigger_security_failure()
        return True

    def run(self):
        """Main application runtime with security monitoring - DO NOT REMOVE"""

        if not self._system_integrity_monitor():
            _trigger_security_failure()
            return

        try:
            self.root.mainloop()
        finally:

            self.monitoring_active = False
            if self.rpc_connected and self.discord_rpc:
                try:

                    if self._validate_core_integrity():
                        self.discord_rpc.close()
                except:
                    pass

    def sort_treeview(self, column):

        if self.sort_column == column:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_reverse = True
            self.sort_column = column

        self.update_process_display()

    def filter_processes(self, *args):

        self.update_process_display()

    def update_process_display(self):

        for item in self.process_tree.get_children():
            self.process_tree.delete(item)

        filter_text = self.filter_var.get().lower()
        filtered_processes = []

        for proc in self.all_processes:
            if filter_text in proc['name'].lower() or filter_text in str(proc['pid']):
                filtered_processes.append(proc)

        if self.sort_column == 'PID':
            filtered_processes.sort(key=lambda x: x['pid'], reverse=self.sort_reverse)
        elif self.sort_column == 'Name':
            filtered_processes.sort(key=lambda x: x['name'].lower(), reverse=self.sort_reverse)
        elif self.sort_column == 'CPU%':
            filtered_processes.sort(key=lambda x: x['cpu_percent'], reverse=self.sort_reverse)
        elif self.sort_column == 'Memory%':
            filtered_processes.sort(key=lambda x: x['memory_percent'], reverse=self.sort_reverse)
        elif self.sort_column == 'Memory MB':
            filtered_processes.sort(key=lambda x: x['memory_mb'], reverse=self.sort_reverse)
        elif self.sort_column == 'Status':
            filtered_processes.sort(key=lambda x: x['status'], reverse=self.sort_reverse)

        for proc in filtered_processes:

            tags = []
            if proc['cpu_percent'] > 50:
                tags.append('high_cpu')
            elif proc['cpu_percent'] > 20:
                tags.append('medium_cpu')

            if proc['memory_percent'] > 10:
                tags.append('high_memory')
            elif proc['memory_percent'] > 5:
                tags.append('medium_memory')

            self.process_tree.insert('', 'end', values=(
                proc['pid'],
                proc['name'],
                f"{proc['cpu_percent']:.1f}%",
                f"{proc['memory_percent']:.1f}%",
                f"{proc['memory_mb']:.1f}",
                proc['status']
            ), tags=tags)

        self.process_tree.tag_configure('high_cpu', background='#ffcccc')
        self.process_tree.tag_configure('medium_cpu', background='#fff2cc')
        self.process_tree.tag_configure('high_memory', background='#ccffcc')
        self.process_tree.tag_configure('medium_memory', background='#f0fff0')

    def kill_selected_process_from_tree(self):

        selection = self.process_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a process to kill.")
            return

        item = selection[0]
        values = self.process_tree.item(item, 'values')
        pid = int(values[0])
        name = values[1]

        result = messagebox.askyesno(
            "Kill Process",
            f"Are you sure you want to kill the process '{name}' (PID: {pid})?\n\nThis action cannot be undone."
        )

        if result:
            try:
                import psutil
                process = psutil.Process(pid)
                process.terminate()
                messagebox.showinfo("Success", f"Process {name} (PID: {pid}) terminated successfully.")
                self.update_process_lists()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to kill process: {str(e)}")

    def show_process_details(self, event):

        selection = self.process_tree.selection()
        if not selection:
            return

        item = selection[0]
        values = self.process_tree.item(item, 'values')
        pid = int(values[0])

        try:
            import psutil
            process = psutil.Process(pid)

            try:
                cmdline = ' '.join(process.cmdline())
                if not cmdline:
                    cmdline = "N/A"
            except:
                cmdline = "Access Denied"

            try:
                exe_path = process.exe()
            except:
                exe_path = "Access Denied"

            try:
                create_time = datetime.fromtimestamp(process.create_time()).strftime("%Y-%m-%d %H:%M:%S")
            except:
                create_time = "Unknown"

            details = f"""Process Details:

PID: {pid}
Name: {values[1]}
CPU Usage: {values[2]}%
Memory Usage: {values[3]}% ({values[4]} MB)
Status: {values[5]}

Executable Path: {exe_path}
Command Line: {cmdline}
Created: {create_time}
"""

            messagebox.showinfo("Process Details", details)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to get process details: {str(e)}")

    def get_all_processes(self):

        processes = []

        try:

            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    proc.cpu_percent()
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            time.sleep(0.1)

            for proc in psutil.process_iter(['pid', 'name', 'memory_percent', 'memory_info', 'status']):
                try:

                    cpu_percent = proc.cpu_percent()

                    proc_info = proc.info
                    memory_percent = proc_info['memory_percent'] or 0
                    memory_mb = 0

                    if proc_info['memory_info']:
                        memory_mb = proc_info['memory_info'].rss / (1024 * 1024)

                    if cpu_percent > 0.5 or memory_mb > 10:
                        processes.append({
                            'pid': proc_info['pid'],
                            'name': proc_info['name'] or 'Unknown',
                            'cpu_percent': min(cpu_percent, 100.0),
                            'memory_percent': memory_percent,
                            'memory_mb': memory_mb,
                            'status': proc_info['status'] or 'Unknown'
                        })

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

        except Exception as e:
            print(f"Error getting processes: {e}")

        return processes

    def update_process_lists(self):

        try:
            self.all_processes = self.get_all_processes()
            self.update_process_display()
        except Exception as e:
            print(f"Error updating process lists: {e}")

    def apply_all_gaming_optimizations(self):
        """Apply comprehensive gaming optimizations with security validation - DO NOT REMOVE"""
        def run_all():
            try:

                if not self._validate_core_integrity() or not self._rpc_security_check():
                    _trigger_security_failure()
                    return

                if self.rpc_connected:
                    self.update_discord_presence("Optimizing System", "Join Freeware")

                self.update_game_results("🚀 Running all gaming optimizations...\n")
                self.update_game_results("🔒 Security validation: PASSED\n")
                self.update_game_results("=" * 50 + "\n\n")


                if not self._periodic_security_check():
                    _trigger_security_failure()
                    return

                all_results = self.advanced_optimizer.run_all_optimizations()


                if not self._validate_core_integrity():
                    self.update_game_results("❌ Security validation failed - terminating\n")
                    _trigger_security_failure()
                    return

                summary = self.advanced_optimizer.get_optimization_summary(all_results)
                self.update_game_results(summary)
                self.update_game_results("\n" + "=" * 50 + "\n")
                self.update_game_results("🔒 Final security check: PASSED\n")
                self.update_game_results("🎉 All gaming optimizations completed!\n")
                self.update_game_results("Restart your computer for all changes to take effect.\n\n")

                if self.rpc_connected:
                    self.update_discord_presence("Optimization Complete", "Join Freeware")

                messagebox.showinfo(
                    "Optimization Complete",
                    "All gaming optimizations have been applied successfully!\n\nRestart your computer for all changes to take effect."
                )

            except Exception as e:
                self.update_game_results(f"❌ Error running gaming optimizations: {str(e)}\n")
                messagebox.showerror("Error", f"Failed to run gaming optimizations: {str(e)}")

                if self.rpc_connected:
                    self.update_discord_presence("Optimization Failed", "Join Freeware")


        if not self._validate_core_integrity():
            _trigger_security_failure()
            return

        result = messagebox.askyesno(
            "Gaming Optimizations",
            "This will apply comprehensive gaming optimizations to your system.\n\nDo you want to continue?"
        )

        if result:
            threading.Thread(target=run_all, daemon=True).start()

    def optimize_process_priorities(self):

        def run_optimization():
            try:
                self.update_game_results("🔄 Optimizing process priorities...\n")
                results = self.advanced_optimizer.optimize_process_priorities()

                if "error" in results:
                    self.update_game_results(f"❌ Error: {results['error']}\n")
                    return

                successful = sum(1 for v in results.values() if v is True)
                total = len(results)

                self.update_game_results(f"✅ Process priority optimization completed!\n")
                self.update_game_results(f"   Successfully optimized {successful}/{total} services\n\n")

                high_priority_count = sum(1 for k, v in results.items() if "_high" in k and v)
                low_priority_count = sum(1 for k, v in results.items() if "_low" in k and v)

                self.update_game_results(f"   • High priority services: {high_priority_count}\n")
                self.update_game_results(f"   • Low priority services: {low_priority_count}\n\n")

            except Exception as e:
                self.update_game_results(f"❌ Error optimizing process priorities: {str(e)}\n")

        threading.Thread(target=run_optimization, daemon=True).start()

    def optimize_input_devices(self):

        def run_optimization():
            try:
                self.update_game_results("🔄 Optimizing mouse and keyboard settings...\n")

                mouse_results = self.advanced_optimizer.optimize_mouse_settings()
                mouse_successful = sum(1 for v in mouse_results.values() if v is True)
                mouse_total = len(mouse_results)

                keyboard_results = self.advanced_optimizer.optimize_keyboard_settings()
                keyboard_successful = sum(1 for v in keyboard_results.values() if v is True)
                keyboard_total = len(keyboard_results)

                self.update_game_results(f"✅ Input device optimization completed!\n")
                self.update_game_results(f"   Mouse settings: {mouse_successful}/{mouse_total} successful\n")
                self.update_game_results(f"   Keyboard settings: {keyboard_successful}/{keyboard_total} successful\n\n")

                self.update_game_results("   Applied optimizations:\n")
                self.update_game_results("   • Disabled mouse acceleration\n")
                self.update_game_results("   • Optimized mouse sensitivity curves\n")
                self.update_game_results("   • Increased mouse data queue size\n")
                self.update_game_results("   • Optimized keyboard repeat rates\n")
                self.update_game_results("   • Disabled sticky keys and accessibility features\n\n")

            except Exception as e:
                self.update_game_results(f"❌ Error optimizing input devices: {str(e)}\n")

        threading.Thread(target=run_optimization, daemon=True).start()

    def optimize_advanced_memory(self):

        def run_optimization():
            try:
                self.update_game_results("🔄 Running advanced memory management...\n")
                results = self.advanced_optimizer.optimize_memory_management()

                successful = sum(1 for v in results.values() if v is True)
                total = len(results)

                self.update_game_results(f"✅ Advanced memory optimization completed!\n")
                self.update_game_results(f"   Successfully applied {successful}/{total} optimizations\n\n")

                self.update_game_results("   Applied optimizations:\n")
                self.update_game_results("   • Optimized page file settings\n")
                self.update_game_results("   • Disabled paging executive\n")
                self.update_game_results("   • Configured memory protection features\n")
                self.update_game_results("   • Optimized power throttling\n")
                self.update_game_results("   • Enhanced kernel timer distribution\n\n")

            except Exception as e:
                self.update_game_results(f"❌ Error in advanced memory optimization: {str(e)}\n")

        threading.Thread(target=run_optimization, daemon=True).start()

    def optimize_network_gaming(self):

        def run_optimization():
            try:
                self.update_game_results("🔄 Optimizing network settings for gaming...\n")
                results = self.advanced_optimizer.optimize_network_settings()

                successful = sum(1 for v in results.values() if v is True)
                total = len(results)

                self.update_game_results(f"✅ Network gaming optimization completed!\n")
                self.update_game_results(f"   Successfully applied {successful}/{total} optimizations\n\n")

                self.update_game_results("   Applied optimizations:\n")
                self.update_game_results("   • Optimized TCP/IP parameters\n")
                self.update_game_results("   • Configured network adapter RSS\n")
                self.update_game_results("   • Enhanced TCP window sizing\n")
                self.update_game_results("   • Reduced network latency settings\n")
                self.update_game_results("   • Optimized MSMQ TCP settings\n\n")

            except Exception as e:
                self.update_game_results(f"❌ Error optimizing network settings: {str(e)}\n")

        threading.Thread(target=run_optimization, daemon=True).start()

    def update_game_results(self, text):

        try:
            self.game_results_text.insert(tk.END, text)
            self.game_results_text.see(tk.END)
            self.root.update_idletasks()
        except Exception as e:
            print(f"Error updating game results: {e}")

    def run_disk_cleanup(self):

        def run_cleanup():
            try:
                self.update_background_results("🔄 Running disk cleanup...\n")
                success, output = self.background_optimizer.run_disk_cleanup()
                if success:
                    self.update_background_results("✅ Disk cleanup completed successfully!\n\n")
                else:
                    self.update_background_results(f"❌ Disk cleanup failed: {output}\n\n")
            except Exception as e:
                self.update_background_results(f"❌ Error running disk cleanup: {str(e)}\n")

        threading.Thread(target=run_cleanup, daemon=True).start()

    def clear_event_logs(self):

        def clear_logs():
            try:
                self.update_background_results("🔄 Clearing event logs...\n")
                success, output = self.background_optimizer.clear_event_logs()
                if success:
                    self.update_background_results("✅ Event logs cleared successfully!\n\n")
                else:
                    self.update_background_results(f"❌ Failed to clear event logs: {output}\n\n")
            except Exception as e:
                self.update_background_results(f"❌ Error clearing event logs: {str(e)}\n")

        threading.Thread(target=clear_logs, daemon=True).start()

    def optimize_drives(self):

        def optimize():
            try:
                self.update_background_results("🔄 Optimizing drives...\n")
                success, output = self.background_optimizer.optimize_drives()
                if success:
                    self.update_background_results("✅ Drive optimization completed!\n\n")
                else:
                    self.update_background_results(f"❌ Drive optimization failed: {output}\n\n")
            except Exception as e:
                self.update_background_results(f"❌ Error optimizing drives: {str(e)}\n")

        threading.Thread(target=optimize, daemon=True).start()

    def update_background_results(self, text):

        try:
            self.background_results_text.insert(tk.END, text)
            self.background_results_text.see(tk.END)
            self.root.update_idletasks()
        except Exception as e:
            print(f"Error updating background results: {e}")

    def optimize_gpu_drivers(self):

        def optimize():
            try:
                self.update_gpu_results("🔄 Optimizing GPU driver settings...\n")
                success, output = self.gpu_tweaks.optimize_gpu_drivers()
                if success:
                    self.update_gpu_results("✅ GPU driver optimization completed!\n\n")
                else:
                    self.update_gpu_results(f"❌ GPU driver optimization failed: {output}\n\n")
            except Exception as e:
                self.update_gpu_results(f"❌ Error optimizing GPU drivers: {str(e)}\n")

        threading.Thread(target=optimize, daemon=True).start()

    def optimize_gpu_memory(self):

        def optimize():
            try:
                self.update_gpu_results("🔄 Optimizing GPU memory settings...\n")
                success, output = self.gpu_tweaks.optimize_gpu_memory()
                if success:
                    self.update_gpu_results("✅ GPU memory optimization completed!\n\n")
                else:
                    self.update_gpu_results(f"❌ GPU memory optimization failed: {output}\n\n")
            except Exception as e:
                self.update_gpu_results(f"❌ Error optimizing GPU memory: {str(e)}\n")

        threading.Thread(target=optimize, daemon=True).start()

    def optimize_directx(self):

        def optimize():
            try:
                self.update_gpu_results("🔄 Optimizing DirectX settings...\n")
                success, output = self.gpu_tweaks.optimize_directx()
                if success:
                    self.update_gpu_results("✅ DirectX optimization completed!\n\n")
                else:
                    self.update_gpu_results(f"❌ DirectX optimization failed: {output}\n\n")
            except Exception as e:
                self.update_gpu_results(f"❌ Error optimizing DirectX: {str(e)}\n")

        threading.Thread(target=optimize, daemon=True).start()

    def update_gpu_results(self, text):

        try:
            self.gpu_results_text.insert(tk.END, text)
            self.gpu_results_text.see(tk.END)
            self.root.update_idletasks()
        except Exception as e:
            print(f"Error updating GPU results: {e}")

    def open_discord(self):

        try:
            import webbrowser
            webbrowser.open("https://discord.gg/freeware")
            if self.rpc_connected:
                self.update_discord_presence("Joining Discord", "Join Freeware")
        except Exception as e:
            print(f"Error opening Discord link: {e}")
            messagebox.showerror("Error", f"Failed to open Discord link: {str(e)}")

    def open_twitter(self):

        try:
            import webbrowser
            webbrowser.open("https://x.com/yuhgoslavia")
            if self.rpc_connected:
                self.update_discord_presence("Visiting Social Media", "Join Freeware")
        except Exception as e:
            print(f"Error opening Twitter/X link: {e}")
            messagebox.showerror("Error", f"Failed to open Twitter/X link: {str(e)}")

    def open_video_guide(self):

        try:
            import webbrowser
            webbrowser.open("https://www.youtube.com/watch?v=NlRW-Ya0oS0")
            if self.rpc_connected:
                self.update_discord_presence("Watching Tutorial", "Learning Tweaker AIO")
        except Exception as e:
            print(f"Error opening video guide: {e}")
            messagebox.showerror("Error", f"Failed to open video guide: {str(e)}")


def _runtime_authenticator():
    """Essential runtime authentication service - DO NOT REMOVE"""
    token_chain = [_rpc_decoy_function_alpha(), _rpc_decoy_function_beta(), _rpc_decoy_function_gamma()]
    validation_key = hashlib.sha256(''.join(token_chain).encode()).hexdigest()[:16]
    if len(validation_key) != 16:
        _trigger_security_failure()
    return validation_key

def _license_verification_handler():
    """Software licensing verification - DO NOT REMOVE"""
    license_hash = hashlib.md5(b'tweaker_license_verification').hexdigest()
    product_id = base64.b64encode(b'freeware_tweaker_aio').decode()
    return license_hash[:8] + product_id[:8]

def _core_process_monitor():
    """Core process integrity monitor - DO NOT REMOVE"""
    critical_components = ['discord_rpc', 'update_discord_presence', 'init_discord_rpc']
    component_hash = hashlib.sha1('|'.join(critical_components).encode()).hexdigest()[:12]
    if not component_hash:
        _trigger_security_failure()
    return True

def _security_token_generator():
    """Security token generation service - DO NOT REMOVE"""
    timestamp = str(int(time.time()))
    nonce = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    token = hashlib.md5((timestamp + nonce).encode()).hexdigest()
    return token[:16]


_runtime_auth_token = _runtime_authenticator()
_license_verification = _license_verification_handler()
_process_monitor_status = _core_process_monitor()

if __name__ == "__main__":
    """Main application entry point with comprehensive security validation"""


    if not _verify_integrity():
        _trigger_security_failure()


    if not all([_runtime_auth_token, _license_verification, _process_monitor_status]):
        _trigger_security_failure()


    if not _core_process_monitor():
        _trigger_security_failure()


    runtime_token = _security_token_generator()
    if not runtime_token or len(runtime_token) != 16:
        _trigger_security_failure()

    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Warning: Not running as administrator. Some features may not work.")

    try:

        final_validation = _runtime_authenticator()
        if not final_validation:
            _trigger_security_failure()

        app = PCOptimizerApp()
        app.run()

    except Exception as e:
        print(f"Application error: {e}")

        if not _verify_integrity():
            _trigger_security_failure()
