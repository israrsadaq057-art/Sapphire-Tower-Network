# 🏢 SAPPHIRE TOWER - ENTERPRISE NETWORK INFRASTRUCTURE

## Complete Production-Ready Network Design for a 5-Floor Commercial Building

<div align="center">

![Cisco](https://img.shields.io/badge/Cisco-1BA0D7?style=for-the-badge&logo=cisco&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)

**[📊 Live Dashboard](https://htmlpreview.github.io/?https://github.com/israrsadaq057-art/Sapphire-Tower-Network/blob/main/dashboard/advanced_monitoring.html)** |
**[🗺️ Network Topology](https://htmlpreview.github.io/?https://github.com/israrsadaq057-art/Sapphire-Tower-Network/blob/main/diagrams/index.html)** |
**[📁 GitHub Repository](https://github.com/israrsadaq057-art/Sapphire-Tower-Network)**

</div>

---

## 📋 Project Overview

This project represents a **complete, production-ready enterprise network infrastructure** designed and configured for **Sapphire Tower**, a 5-floor commercial building located at **Shahrah-e-Faisal, Karachi, Pakistan**. The building houses **160+ employees** across departments including Executive, IT, Finance, Marketing, Sales, and Retail.

### 🏢 Building Specifications

| Parameter | Value |
|-----------|-------|
| **Location** | Shahrah-e-Faisal, Karachi, Pakistan |
| **Floors** | 5 + Basement |
| **Total Users** | 160+ |
| **Total Devices** | 450+ |
| **Departments** | Executive, IT, Finance, Marketing, Sales, Retail, Security |

---

## 📊 Network Statistics

| Component | Quantity | Details |
|-----------|----------|---------|
| **Core Switches** | 1 | Cisco Catalyst 9300-48P |
| **Distribution Switches** | 6 | Cisco Catalyst 9200-24P |
| **Access Switches** | 6 | Cisco Catalyst 9200-24P |
| **Total Switches** | 13 | All PoE+ capable |
| **Security Cameras** | 24 | Hikvision 4K PoE |
| **Access Points** | 20 | Cisco Catalyst 9120/9130AXI |
| **Firewalls** | 2 | Cisco Firepower 1120 (HA) |
| **NVR Storage** | 48TB | 30-day retention, RAID 10 |
| **Total Ports** | 312 | All active |
| **PoE Budget** | 1.8kW | For cameras and APs |

---

---

## 🌐 VLAN Design & Security Zones

| VLAN | Name | Subnet | Gateway | Purpose | Security Zone |
|------|------|--------|---------|---------|---------------|
| 10 | Management | 10.10.10.0/24 | 10.10.10.1 | Network Device Management | 🔒 Red |
| 20 | CCTV | 10.10.20.0/24 | 10.10.20.1 | Security Cameras | 🟡 Isolated |
| 30 | WiFi-Staff | 10.10.30.0/24 | 10.10.30.1 | Employee WiFi | 🟢 Internal |
| 40 | WiFi-Guest | 172.16.40.0/24 | 172.16.40.1 | Guest WiFi | ⚪ Internet Only |
| 50 | Data | 10.10.50.0/24 | 10.10.50.1 | User Workstations | 🟢 Internal |
| 60 | Control-Room | 10.10.60.0/24 | 10.10.60.1 | Security Operations | 🔒 Restricted |
| 70 | VoIP | 10.10.70.0/24 | 10.10.70.1 | Voice (Future) | 🟢 Internal |
| 80 | Server | 10.10.80.0/24 | 10.10.80.1 | Data Center Servers | 🔒 Gold |

---

## 📷 Security Camera System

### 24 Cameras Across All Floors

| Floor | Cameras | Locations | IP Range |
|-------|---------|-----------|----------|
| **Floor 1** | 4 | Lobby, Reception, Coffee Shop, Retail | 10.10.20.11-14 |
| **Floor 2** | 3 | Marketing, Sales, Elevator | 10.10.20.21-23 |
| **Floor 3** | 3 | Finance, HR, Elevator | 10.10.20.31-33 |
| **Floor 4** | 4 | IT Lab, NOC, Server Room, Elevator | 10.10.20.41-44 |
| **Floor 5** | 3 | Executive, Board Room, Elevator | 10.10.20.51-53 |
| **Basement** | 4 | Parking A, Parking B, Security Office, Elevator | 10.10.20.61-64 |

**Camera Specifications:**
- **Model:** Hikvision DS-2CD2386G2 (4K ColorVu)
- **Resolution:** 3840 x 2160 (4K)
- **Frame Rate:** 15 fps
- **Recording:** Continuous 24/7 + Motion Detection
- **Storage:** 48TB RAID 10 (30-day retention)

---

## 📶 Wireless Network

### 20 Cisco Catalyst Access Points

| Floor | APs | Model | SSID | Security |
|-------|-----|-------|------|----------|
| Floor 1 | 4 | Cisco 9120AXI | Sapphire-Staff | WPA2-Enterprise |
| Floor 2 | 3 | Cisco 9120AXI | Sapphire-Staff | WPA2-Enterprise |
| Floor 3 | 3 | Cisco 9120AXI | Sapphire-Staff | WPA2-Enterprise |
| Floor 4 | 4 | Cisco 9130AXI | Sapphire-Staff | WPA2-Enterprise |
| Floor 5 | 4 | Cisco 9130AXI | Sapphire-Executive | WPA3-Enterprise |
| Basement | 2 | Cisco 9120AXI | Sapphire-Staff | WPA2-Enterprise |

---

## 🔥 Security Features

### Firewall (Cisco Firepower 1120)

| Feature | Status | Details |
|---------|--------|---------|
| **IPS/IDS** | ✅ Active | Real-time threat prevention |
| **URL Filtering** | ✅ Active | Blocks social media, streaming during work hours |
| **Application Control** | ✅ Active | Blocks Facebook, YouTube, Netflix, Torrents |
| **VPN** | ✅ Active | Remote access for employees (IPSec AES-256) |
| **Guest Isolation** | ✅ Active | Guest WiFi: internet only, no internal access |
| **CCTV Security** | ✅ Active | Cameras only communicate with NVR |
| **Management Access** | ✅ Active | IT staff only via SSH/HTTPS |

### Threats Blocked (Last 24h)

| Threat Type | Count | Action |
|-------------|-------|--------|
| Port Scan Attempts | 12 | Blocked |
| Malware Signatures | 3 | Blocked |
| Phishing URLs | 8 | Blocked |
| Suspicious Logins | 2 | Investigated |

---

## 📁 Project Structure
```
Sapphire-Tower-Network/
│
├── diagrams/ # Network Diagrams
│ ├── index.html # 🗺️ Interactive Network Topology
│ ├── ip_addressing_diagram.html # 📡 IP & VLAN Design
│ └── cabling_diagram.html # 🔌 Cabling Infrastructure
│
├── dashboard/ # Monitoring Dashboards
│ ├── index.html # 🚀 Launch Dashboard
│ └── advanced_monitoring.html # 📊 Real-time Network Monitoring
│
├── configs/ # Device Configurations
│ ├── core/ # Core Switch Config
│ │ └── core_switch_config.txt
│ ├── distribution/ # 6 Distribution Switch Configs
│ │ ├── dist_switch_floor1.txt
│ │ ├── dist_switch_floor2.txt
│ │ ├── dist_switch_floor3.txt
│ │ ├── dist_switch_floor4.txt
│ │ ├── dist_switch_floor5.txt
│ │ └── dist_switch_basement.txt
│ ├── access/ # 6 Access Switch Configs
│ │ ├── access_switch_floor1_full.txt
│ │ ├── access_switch_floor2_full.txt
│ │ ├── access_switch_floor3_full.txt
│ │ ├── access_switch_floor4_full.txt
│ │ ├── access_switch_floor5_full.txt
│ │ └── access_switch_basement_full.txt
│ ├── firewall/ # Firewall Config
│ │ └── firewall_enterprise_config.txt
│ ├── wireless/ # Access Point Config
│ │ └── ap_config.txt
│ ├── nvr/ # NVR Config
│ │ └── nvr_config.txt
│ └── cctv/ # Camera Configurations
│ ├── cameras/ # 24 Individual Camera Configs
│ │ ├── CAM-F1-01_Lobby.txt
│ │ ├── CAM-F1-02_Reception.txt
│ │ ├── ... (24 files)
│ │ └── CAM-B1-04_Elevator.txt
│ ├── camera_ip_allocation.txt
│ ├── camera_config_template.txt
│ ├── nvr_camera_registration.txt
│ └── how_camera_ip_works.txt
│
└── README.md # 📖 This File
```

---

## 🚀 Quick Start

###  View the Interactive Dashboards

| Dashboard | Link |
|-----------|------|
| **Advanced Monitoring** | [Open Dashboard](https://htmlpreview.github.io/?https://github.com/israrsadaq057-art/Sapphire-Tower-Network/blob/main/dashboard/advanced_monitoring.html) |
| **Network Topology** | [Open Topology](https://htmlpreview.github.io/?https://github.com/israrsadaq057-art/Sapphire-Tower-Network/blob/main/diagrams/index.html) |
| **IP Addressing** | [Open IP Diagram](https://htmlpreview.github.io/?https://github.com/israrsadaq057-art/Sapphire-Tower-Network/blob/main/diagrams/ip_addressing_diagram.html) |
| **Cabling Diagram** | [Open Cabling](https://htmlpreview.github.io/?https://github.com/israrsadaq057-art/Sapphire-Tower-Network/blob/main/diagrams/cabling_diagram.html) |

 
## 👨‍💻 About the Engineer

### Israr Sadaq
**Network Engineer | Network Automation Specialist | IT Administrator**

<div align="center">
  
![Location](https://img.shields.io/badge/Location-Berlin%2C%20Germany-blue)
![Email](https://img.shields.io/badge/Email-israrsadaq057%40gmail.com-red)
![Phone](https://img.shields.io/badge/Phone-%2B49%20152525267799-green)
![GitHub](https://img.shields.io/badge/GitHub-israrsadaq057--art-black)

</div>

---

### 🎓 Certifications

| Certification | Year | Issuing Organization |
|---------------|------|---------------------|
| 🎓 **CCNA** (Cisco Certified Network Associate) | 2025 | Cisco |
| 🎓 **CCNP** (Cisco Certified Network Professional) | 2025 | Cisco |
| ⚙️ **Industrial Automation & PLC** | 2015 | National Training Bureau, Islamabad |
| 📡 **M.Sc. Information & Communication Engineering** | Present | BHT Berlin, Germany |

---

### 💼 Professional Experience

#### 🔬 Student Assistant - Optical Networks / Network Engineering
**Fraunhofer HHI Berlin** | Sep 2025 - Present | Berlin, Germany

- Developed network automation workflows for optical transport networks using Python, SDN controllers, and APIs
- Configured and tested PON technologies (GPON/XGS-PON) with performance and stability analysis
- Performed network device configuration, lab setup, and troubleshooting across optical and Ethernet environments
- Conducted optical and Ethernet performance measurements with fault analysis
- Worked on Time-Sensitive Networking (TSN) for industrial applications

#### 🏢 Junior Network Administrator & IT Administrator
**Resource Academia International** | Jul 2016 - May 2022 | Islamabad, Pakistan

**Network Engineering:**
- Managed enterprise LAN/WAN infrastructure for 300+ users across 6 departments
- Configured Cisco routers and switches (VLANs, routing, port security, STP)
- Implemented Cisco Firepower ACLs, VPN, and security policies
- Designed and deployed Zero-Touch Provisioning (ZTP) automation

**IT Administration:**
- Administered Active Directory for 100+ users, 6 departments, 12 security groups
- Automated user lifecycle management with PowerShell (onboarding, offboarding, bulk import)
- Configured Group Policy Objects (GPO) for security and desktop management
- Managed Windows Server (AD DS, DNS, DHCP, File Server)
- Implemented backup & disaster recovery procedures

---

### 🛠️ Technical Skills

#### 🌐 Network Engineering
| Technology | Proficiency |
|------------|-------------|
| Cisco IOS / NX-OS | ⭐⭐⭐⭐⭐ |
| VLANs, STP, OSPF, BGP | ⭐⭐⭐⭐⭐ |
| Cisco Firepower ACLs / IPS | ⭐⭐⭐⭐ |
| PON (GPON/XGS-PON) | ⭐⭐⭐⭐ |
| Time-Sensitive Networking (TSN) | ⭐⭐⭐⭐ |
| SDN Controllers / REST APIs | ⭐⭐⭐⭐ |

#### 🤖 Network Automation
| Technology | Proficiency |
|------------|-------------|
| Python (Netmiko, Paramiko) | ⭐⭐⭐⭐⭐ |
| Jinja2 Templating | ⭐⭐⭐⭐⭐ |
| YAML / JSON | ⭐⭐⭐⭐⭐ |
| Zero-Touch Provisioning (ZTP) | ⭐⭐⭐⭐⭐ |
| PowerShell Scripting | ⭐⭐⭐⭐⭐ |

#### 🏢 IT Administration
| Technology | Proficiency |
|------------|-------------|
| Active Directory (Users, Groups, GPO) | ⭐⭐⭐⭐⭐ |
| Windows Server (AD DS, DNS, DHCP) | ⭐⭐⭐⭐⭐ |
| Backup & Recovery | ⭐⭐⭐⭐ |
| Group Policy Management | ⭐⭐⭐⭐⭐ |

#### 📊 Monitoring & Visualization
| Technology | Proficiency |
|------------|-------------|
| HTML5 / CSS3 / JavaScript | ⭐⭐⭐⭐ |
| Chart.js / Data Visualization | ⭐⭐⭐⭐ |
| SNMP / NetFlow / Syslog | ⭐⭐⭐⭐ |
| Real-time Dashboards | ⭐⭐⭐⭐ |

#### 🛠️ DevOps & Tools
| Technology | Proficiency |
|------------|-------------|
| Git / GitHub | ⭐⭐⭐⭐⭐ |
| Linux (Ubuntu, CentOS) | ⭐⭐⭐⭐ |
| VS Code / PyCharm | ⭐⭐⭐⭐⭐ |
| Wireshark / Packet Tracer | ⭐⭐⭐⭐ |

---

### 🚀 Featured Projects

| Project | Description | Technologies |
|---------|-------------|--------------|
| **[Sapphire Tower Network](https://github.com/israrsadaq057-art/Sapphire-Tower-Network)** | Complete enterprise network design for 5-floor building with 13 switches, 24 cameras, 20 APs | Cisco, Python, HTML/CSS/JS |
| **[Network Automation Dashboard](https://github.com/israrsadaq057-art/Network-Automation-Dashboard)** | Real-time network monitoring with live device status and alerts | Python, Flask, Chart.js |
| **[AD Automation Suite](https://github.com/israrsadaq057-art/AD-Automation-Suite)** | Active Directory automation for 100+ users with PowerShell | PowerShell, AD, HTML/CSS |
| **[Zero-Touch Provisioning](https://github.com/israrsadaq057-art/resource-academia-network-automation)** | Cisco network automation with Python and Jinja2 | Python, Netmiko, Jinja2 |
| **[Network Telemetry Monitor](https://github.com/israrsadaq057-art/Network-Telemetry-Monitor)** | Streaming telemetry with gNMI/gRPC | Python, gNMI, InfluxDB |

---

### 🗣️ Languages

| Language | Proficiency | Level |
|----------|-------------|-------|
| **Urdu** | Native | Mother tongue |
| **English** | Professional | C1 (Fluent) |
| **German** | Professional | B2 (Working proficiency) |

---

### 📫 Contact & Social

| | |
|---|---|
| 📧 **Email** | israrsadaq057@gmail.com |
| 📱 **Phone** | +49 152525267799 |
| 📍 **Location** | Berlin, Germany |
| 🔗 **GitHub** | [github.com/israrsadaq057-art](https://github.com/israrsadaq057-art) |
| 💼 **LinkedIn** | [linkedin.com/in/israr-sadaq](https://linkedin.com/in/israr-sadaq) |

---

### 🏆 Key Achievements

- ✅ **80% reduction** in manual network configuration time through ZTP automation
- ✅ **CCNA & CCNP certified** with hands-on enterprise experience
- ✅ **100+ users** managed across 6 departments with Active Directory automation
- ✅ **24 cameras, 20 APs, 13 switches** configured for 5-floor building
- ✅ **8 VLANs** designed with security segmentation
- ✅ **Python automation** for network and IT operations
- ✅ **Real-time monitoring dashboard** with live device status

---

### 🎯 Interests & Focus Areas

- 🔧 Network Automation & Infrastructure as Code
- 🌐 Optical Networks (GPON, XGS-PON, TSN)
- 🛡️ Network Security & Zero-Trust Architecture
- 📊 Real-time Network Monitoring & Visualization
- 🤖 IT Automation with PowerShell & Python
- 🏢 Enterprise Network Design & Implementation

---

### 📜 Professional Philosophy

> *"Building networks that are secure, automated, and scalable. I believe in infrastructure as code, proactive monitoring, and continuous improvement. Every network should be designed with security in mind and automated wherever possible."*

---

### 💬 Quote

> *"The best network is the one that works seamlessly, is secure by design, and never requires manual intervention."*

---

**© 2026 Israr Sadaq | Network Engineer | Network Automation Specialist | IT Administrator**
