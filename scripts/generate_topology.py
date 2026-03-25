#!/usr/bin/env python3
"""
Sapphire Tower Network Topology Generator
Network Engineer: Israr Sadaq
Generates network topology data in JSON format
"""

import json
import os
from datetime import datetime

# Network topology data
topology = {
    "building": {
        "name": "Sapphire Tower",
        "location": "Shahrah-e-Faisal, Karachi, Pakistan",
        "floors": 6,
        "total_users": 160,
        "total_devices": 220
    },
    
    "core_layer": {
        "switch": {
            "name": "Core-SW-01",
            "model": "Cisco Catalyst 9300-48P",
            "ip": "10.10.10.1",
            "ports": 48,
            "poe_budget": "740W",
            "location": "Basement - Server Room"
        },
        "firewall": {
            "name": "Firewall-01",
            "model": "Cisco Firepower 1120",
            "ip": "10.10.10.254",
            "throughput": "1.2 Gbps"
        },
        "internet": {
            "isp": "PTCL Flash Fiber",
            "speed": "100 Mbps",
            "cost": "₨ 25,000/month"
        }
    },
    
    "distribution_layer": [
        {"name": "Dist-SW-F1", "floor": "Floor 1", "ip": "10.10.10.11", "uplink": "Core-SW-01"},
        {"name": "Dist-SW-F2", "floor": "Floor 2", "ip": "10.10.10.12", "uplink": "Core-SW-01"},
        {"name": "Dist-SW-F3", "floor": "Floor 3", "ip": "10.10.10.13", "uplink": "Core-SW-01"},
        {"name": "Dist-SW-F4", "floor": "Floor 4", "ip": "10.10.10.14", "uplink": "Core-SW-01"},
        {"name": "Dist-SW-F5", "floor": "Floor 5", "ip": "10.10.10.15", "uplink": "Core-SW-01"},
        {"name": "Dist-SW-B1", "floor": "Basement", "ip": "10.10.10.16", "uplink": "Core-SW-01"}
    ],
    
    "access_layer": {
        "floor_1": {
            "cameras": 4,
            "access_points": 4,
            "workstations": 15,
            "departments": ["Reception", "Coffee Shop", "Retail"]
        },
        "floor_2": {
            "cameras": 3,
            "access_points": 3,
            "workstations": 20,
            "departments": ["Marketing", "Sales"]
        },
        "floor_3": {
            "cameras": 3,
            "access_points": 3,
            "workstations": 25,
            "departments": ["Finance", "HR", "Training"]
        },
        "floor_4": {
            "cameras": 4,
            "access_points": 4,
            "workstations": 30,
            "departments": ["IT", "NOC", "Server Room"]
        },
        "floor_5": {
            "cameras": 3,
            "access_points": 4,
            "workstations": 20,
            "departments": ["Executive", "Board Room"]
        },
        "basement": {
            "cameras": 4,
            "access_points": 2,
            "workstations": 8,
            "departments": ["Security Control Room", "Parking"]
        }
    },
    
    "statistics": {
        "total_cameras": 21,
        "total_access_points": 20,
        "total_switches": 13,
        "total_workstations": 118,
        "total_ports": 312,
        "total_poe_power": 1850,
        "storage_capacity": "48TB",
        "retention_days": 30
    },
    
    "vlans": [
        {"id": 10, "name": "Management", "subnet": "10.10.10.0/24"},
        {"id": 20, "name": "CCTV", "subnet": "10.10.20.0/24"},
        {"id": 30, "name": "WiFi-Staff", "subnet": "10.10.30.0/24"},
        {"id": 40, "name": "WiFi-Guest", "subnet": "172.16.40.0/24"},
        {"id": 50, "name": "Data", "subnet": "10.10.50.0/24"},
        {"id": 60, "name": "Control-Room", "subnet": "10.10.60.0/24"},
        {"id": 70, "name": "VoIP", "subnet": "10.10.70.0/24"},
        {"id": 80, "name": "Server", "subnet": "10.10.80.0/24"}
    ],
    
    "generated_at": datetime.now().isoformat()
}

# Save to JSON file
output_path = os.path.join("inventory", "topology_data.json")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, 'w') as f:
    json.dump(topology, f, indent=2)

print("="*60)
print("SAPPHIRE TOWER NETWORK TOPOLOGY")
print("="*60)
print(f"Building: {topology['building']['name']}")
print(f"Location: {topology['building']['location']}")
print(f"Floors: {topology['building']['floors']}")
print(f"Total Users: {topology['building']['total_users']}")
print(f"Total Devices: {topology['building']['total_devices']}")
print()
print("Network Statistics:")
print(f"  - Core Switch: {topology['core_layer']['switch']['model']}")
print(f"  - Firewall: {topology['core_layer']['firewall']['model']}")
print(f"  - Distribution Switches: {len(topology['distribution_layer'])}")
print(f"  - Access Points: {topology['statistics']['total_access_points']}")
print(f"  - Cameras: {topology['statistics']['total_cameras']}")
print(f"  - Switches: {topology['statistics']['total_switches']}")
print()
print(f"✅ Topology data saved to: {output_path}")