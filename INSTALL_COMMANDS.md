# Dr WiFi - Complete Installation Commands

## 🚀 Step-by-Step Installation Guide for Termux

### Step 1: Termux Installation
```bash
# Download Termux from F-Droid or Google Play Store
# No commands needed - just install the app
```

### Step 2: Update Termux
```bash
pkg update && pkg upgrade
```

### Step 3: Install Required Packages
```bash
pkg install python
pkg install git
pkg install wireless-tools
pkg install aircrack-ng
pkg install wpa_supplicant
```

### Step 4: Setup Storage Permissions
```bash
termux-setup-storage
```

### Step 5: Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/dr-wifi.git
```

### Step 6: Navigate to Directory
```bash
cd dr-wifi
```

### Step 7: Check Files
```bash
ls -la
```

### Step 8: Make Script Executable
```bash
chmod +x dr_wifi.py
```

### Step 9: Run Dr WiFi Tool
```bash
python dr_wifi.py
```

---

## 📋 Complete Command List (Copy-Paste Ready)

```bash
# 1. Update Termux
pkg update && pkg upgrade

# 2. Install all dependencies
pkg install python git wireless-tools aircrack-ng wpa_supplicant

# 3. Setup storage
termux-setup-storage

# 4. Clone repository (replace YOUR_USERNAME with your GitHub username)
git clone https://github.com/YOUR_USERNAME/dr-wifi.git

# 5. Navigate to folder
cd dr-wifi

# 6. Check files
ls -la

# 7. Make executable
chmod +x dr_wifi.py

# 8. Run tool
python dr_wifi.py
```

---

## 🔧 Troubleshooting Commands

### If git clone fails:
```bash
pkg install git
git clone https://github.com/hearthackerBabar/dr-wifi.git
```

### If python not found:
```bash
pkg install python
python dr_wifi.py
```

### If wireless tools missing:
```bash
pkg install wireless-tools
pkg install aircrack-ng
```

### If permission denied:
```bash
chmod +x dr_wifi.py
termux-setup-storage
```

### If no wireless interfaces:
```bash
# Enable WiFi on your device first
# Then run:
python dr_wifi.py
```

---

## 📱 Quick Start (One-Liner)

```bash
pkg update && pkg upgrade && pkg install python git wireless-tools aircrack-ng wpa_supplicant && termux-setup-storage && git clone https://github.com/YOUR_USERNAME/dr-wifi.git && cd dr-wifi && chmod +x dr_wifi.py && python dr_wifi.py
```

---

## 🎯 Expected Output

After running `python dr_wifi.py`, you should see:

1. **Dr WiFi ASCII Logo** - Beautiful colored logo
2. **Requirements Check** - ✅ Available tools
3. **WiFi Scanning** - 📡 Scanning networks
4. **Network List** - Found WiFi networks
5. **Password Testing** - 🔓 Testing passwords
6. **Results** - ✅ Successful cracks (if any)

---

## ⚠️ Important Notes

- **Replace `YOUR_USERNAME`** with your actual GitHub username
- **Enable WiFi** on your device before running
- **Root access** recommended for full functionality
- **Use responsibly** - only test your own networks

---

## 🆘 If Something Goes Wrong

```bash
# Reset everything and start fresh
cd ~
rm -rf dr-wifi
pkg update && pkg upgrade
pkg install python git wireless-tools aircrack-ng wpa_supplicant
git clone https://github.com/YOUR_USERNAME/dr-wifi.git
cd dr-wifi
python dr_wifi.py
```

---


**🎉 That's it! Your Dr WiFi tool is ready to use!** 
