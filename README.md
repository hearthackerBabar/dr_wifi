# Dr WiFi - WiFi Password Cracker Tool Only For Rooted Android Phones

A powerful WiFi network scanner and password cracker tool designed specifically for Termux Android environment.

## 🎯 Features

- **🔍 WiFi Network Scanning** - Automatically detects all nearby WiFi networks
- **📡 Network Details** - Shows SSID, BSSID, Channel, and Encryption type
- **🔓 Password Cracking** - Tests 118 common passwords against each network
- **🎨 Beautiful UI** - Colorful terminal output with progress indicators
- **⚡ Fast Performance** - Optimized for Termux environment
- **🛡️ Error Handling** - Robust error handling and user feedback

## 📱 Requirements

- Android device with Termux installed
- Root access (recommended for full functionality)
- Internet connection for initial setup

## 🚀 Installation

### Step 1: Install Termux
Download and install Termux from [F-Droid](https://f-droid.org/en/packages/com.termux/) or Google Play Store.

### Step 2: Clone Repository
```bash
git clone https://github.com/hearthackerBabar/dr-wifi.git
cd dr-wifi
```

### Step 3: Install Dependencies
```bash
pkg update && pkg upgrade
pkg install python
pkg install wireless-tools
pkg install aircrack-ng
pkg install git
```

### Step 4: Run the Tool
```bash
python dr_wifi.py
```

## 📋 Usage

1. **Start the tool:**
   ```bash
   python dr_wifi.py
   ```

2. **The tool will:**
   - Display the Dr WiFi logo
   - Check for required tools
   - Scan for nearby WiFi networks
   - Show network details
   - Test passwords from `password.txt`
   - Display successful cracks

3. **Results will show:**
   - Network name (SSID)
   - Password (if found)
   - BSSID (MAC address)

## 🔧 Troubleshooting

### If tools are not found:
```bash
pkg install wireless-tools
pkg install aircrack-ng
pkg install wpa_supplicant
```

### If permission denied:
```bash
termux-setup-storage
chmod +x dr_wifi.py
```

### If no wireless interfaces found:
- Make sure WiFi is enabled
- Try running with root access
- Check if your device supports wireless tools

## 📁 Files

- `dr_wifi.py` - Main WiFi cracker tool
- `password.txt` - Database of 118 common passwords
- `README.md` - This documentation file

## ⚠️ Disclaimer

This tool is for **educational purposes only**. Use only on networks you own or have explicit permission to test. Unauthorized access to WiFi networks may be illegal in your jurisdiction.

## 🤝 Contributing

Feel free to contribute by:
- Adding more passwords to `password.txt`
- Improving the scanning algorithm
- Adding new features
- Reporting bugs

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section
2. Make sure all dependencies are installed
3. Ensure you have proper permissions
4. Try running with root access

## 🎉 Credits

Created by Dr WiFi Team
For educational and ethical hacking purposes only.

---


**Remember: Always use this tool responsibly and legally!** 

