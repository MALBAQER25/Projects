# Importing libraries
import socket        # لمعرفة IP الداخلي للجهاز
import requests      # لجلب IP العام من الإنترنت
import uuid          # للحصول على عنوان MAC الفريد
import subprocess    # لتنفيذ أوامر النظام (لاستخراج كلمة مرور الواي فاي)
import tkinter as gui # لإنشاء واجهة رسومية أنيقة

# ============================
# Custom Class for System Info
# ============================
class DeviceInspector:
    def init(self):
        self.local_ip_address = "Unknown"
        self.external_ip_address = "Unknown"
        self.mac_identity = "Unknown"
        self.wifi_key = "Unknown"

    # Local IP Detection
    def fetch_local_ip(self):
        try:
            self.local_ip_address = socket.gethostbyname(socket.gethostname())
            return self.local_ip_address
        except:
            return "Local IP not found"

    # Public IP Detection
    def fetch_public_ip(self):
        try:
            self.external_ip_address = requests.get("https://api.ipify.org").text
            return self.external_ip_address
        except:
            return "Unable to reach internet"

    # MAC Address Detection
    def fetch_mac_address(self):
        try:
            mac_raw = uuid.getnode()
            formatted = ':'.join(['{:02x}'.format((mac_raw >> i) & 0xff) for i in range(40, -1, -8)])
            self.mac_identity = formatted.upper()
            return self.mac_identity
        except:
            return "MAC address unavailable"

    # Wi-Fi Password Retrieval
    def fetch_wifi_key(self):
        try:
            data = subprocess.check_output("netsh wlan show interfaces", shell=True, text=True)
            start = data.find("SSID") + 5
            end = data.find("\n", start)
            network_name = data[start:end].strip()
            command = f'netsh wlan show profile name="{network_name}" key=clear'
            output = subprocess.check_output(command, shell=True, text=True)
            key_line = [line for line in output.split("\n") if "Key Content" in line]
            if key_line:
                self.wifi_key = key_line[0].split(":")[1].strip()
                return self.wifi_key
            else:
                return "No password saved"
        except:
            return "Error fetching Wi-Fi details"

# ============================
# GUI Section
# ============================
def display_info():
    inspector = DeviceInspector()
    box.delete("1.0", gui.END)
    box.insert(gui.END, "Device Security Scan Started...\n\n")
    box.insert(gui.END, f"Local IP: {inspector.fetch_local_ip()}\n")
    box.insert(gui.END, f"Public IP: {inspector.fetch_public_ip()}\n")
    box.insert(gui.END, f"MAC Address: {inspector.fetch_mac_address()}\n")
    box.insert(gui.END, f"Wi-Fi Password: {inspector.fetch_wifi_key()}\n\n")
    box.insert(gui.END, "Scan Completed Successfully.\n")

# GUI Design
window = gui.Tk()
window.title("Network Insight Tool")
window.geometry("480x370")
window.config(bg="#1E293B")

heading = gui.Label(window, text="System & Network Inspector", fg="white", bg="#1E293B", font=("Segoe UI", 15, "bold"))
heading.pack(pady=12)

scan_button = gui.Button(window, text="Run Scan", bg="#2563EB", fg="white", font=("Segoe UI", 12, "bold"),
                         width=15, height=1, command=display_info)
scan_button.pack(pady=8)

box = gui.Text(window, height=12, width=55, font=("Consolas", 10), bg="#F8FAFC", fg="black", relief="flat")
box.pack(padx=10, pady=10)

credit = gui.Label(window, text="Developed by Muhammad Albaqer Shukur", bg="#1E293B", fg="#CBD5E1", font=("Calibri", 9))
credit.pack(side="bottom", pady=5)

window.mainloop()