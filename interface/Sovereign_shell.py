import sys
import subprocess
import os

try:
    import keyboard
    from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QLabel
    from PySide6.QtCore import Qt, Signal, Slot, QTimer
except ImportError as e:
    print(f"CRITICAL ERROR: Missing Library -> {e}")
    print("Run: python -m pip install PySide6 keyboard")
    sys.exit(1)

class SovereignShell(QWidget):
    toggle_signal = Signal()

    def __init__(self):
        super().__init__()
        # Correct path for root-level log
        self.log_file = r"C:\Users\Admin\AIOS_Memory\neural_log.txt"
        self.initUI()
        
        try:
            keyboard.add_hotkey('alt+space', lambda: self.toggle_signal.emit())
            self.toggle_signal.connect(self.toggle_visibility)
        except Exception as e:
            print(f"HOTKEY ERROR: {e}")

        self.log_timer = QTimer()
        self.log_timer.timeout.connect(self.update_neural_log)
        self.log_timer.start(2000)

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.status_label = QLabel("SYSTEM READY | SOVEREIGN KERNEL ACTIVE", self)
        self.status_label.setStyleSheet("color: #00FF41; font-family: 'Consolas'; font-size: 14px; background: rgba(0,0,0,150);")

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("🏛️ Sovereign Intent...")
        self.line_edit.setStyleSheet("background-color: #121212; color: #00FF41; border: 2px solid #00FF41; border-radius: 20px; padding: 12px; font-size: 18px;")
        self.line_edit.returnPressed.connect(self.execute_intent)

        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

        screen = QApplication.primaryScreen().geometry()
        self.setFixedSize(800, 100)
        self.move((screen.width() - 800) // 2, screen.height() - 150)

    def update_neural_log(self):
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, "r") as f:
                    lines = f.readlines()
                    if lines:
                        last_event = lines[-1].strip()
                        display_text = f"NEURAL LOG: {last_event[-80:]}"
                        
                        # Breakthrough Logic: Highlight the Money
                        if "₹" in display_text or "Savings" in display_text:
                            self.status_label.setStyleSheet("color: #FFD700; font-family: 'Consolas'; font-size: 14px; font-weight: bold; background: rgba(0,0,0,150);")
                        else:
                            self.status_label.setStyleSheet("color: #00FF41; font-family: 'Consolas'; font-size: 14px; background: rgba(0,0,0,150);")
                            
                        self.status_label.setText(display_text)
            except: pass

    @Slot()
    def toggle_visibility(self):
        if self.isVisible(): self.hide()
        else:
            self.show()
            self.activateWindow()
            self.line_edit.setFocus()

    def execute_intent(self):
        cmd = self.line_edit.text().lower()
        self.line_edit.clear()
        if "audit" in cmd: subprocess.Popen(["cmd", "/c", "start", "python", "core/watcher.py"])
        elif "exit" in cmd: sys.exit()
        elif "hide" in cmd: self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        shell = SovereignShell()
        shell.show()
        print("🏛️ Sovereign Shell is now active. Press Alt+Space to toggle.")
        sys.exit(app.exec())
    except Exception as e:
        print(f"STARTUP ERROR: {e}")