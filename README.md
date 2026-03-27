# 🛡️ Custom C2 Stealth Agent (Proof of Concept)

A Python-based Command & Control (C2) agent designed to demonstrate **Advanced Persistent Threat (APT)** simulation and **"Living off the Land" (LotL)** execution techniques.

> ⚠️ **DISCLAIMER:** This project is for **EDUCATIONAL and ETHICAL purposes only**. This tool was developed within a controlled lab environment (Kali Linux and Windows 10 VM) to understand malware behavior and endpoint detection. Unauthorized use of this tool against systems you do not own is strictly prohibited.

## 🚀 Project Overview
This project establishes a **Reverse TCP Shell** between a Windows 10 target and a Kali Linux attack station. It bypasses standard user-level detection by utilizing windowless execution, remaining persistent in the background after the initial terminal session is closed.

### Key Features:
* **Reverse TCP Connection:** Initiates an outbound connection to bypass inbound firewall rules.
* **Windowless Execution:** Uses `pythonw` to run the agent without a visible console window.
* **System Enumeration:** Capable of remote command execution for system info, directory listing, and user identification.

## 🛠️ Technical Workflow

### 1. Attacker Setup (Kali Linux)
Start the listener to wait for the incoming connection:
```bash
python3 listner.py
