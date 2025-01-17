# Nornir EVE Telnet/SSH Automation

This repository contains an automation setup using [Nornir](https://nornir.readthedocs.io) to manage and configure multiple Cisco IOS devices via Telnet (initially) and SSH. It is designed to work in an EVE-NG lab environment, where routers and switches are connected to a cloud interface that bridges to an Ubuntu VM running Nornir.
I created this because I used to spend a lot of time configuring SSH on a device by device basis so I could use my other scripts that use SSH.

## Overview

- **Language**: Python 3
- **Automation Framework**: [Nornir](https://nornir.readthedocs.io)
- **Connection Library**: [Netmiko](https://github.com/ktbyers/netmiko)
- **Topology**: Created and emulated in EVE-NG

### Main Features

1. **Telnet Configuration**: Sets up or modifies devices (hostname, domain name, etc.) via Telnet for initial access.  
2. **SSH Transition**: Generates RSA keys, enables SSH, and can switch `transport input` to `ssh telnet` (or just `ssh`).  
3. **OSPF & Interfaces**: Automates interface IP assignments and OSPF configuration on specified routers.  
4. **Filtering**: Demonstrates how to exclude certain devices (e.g., R3) from mass configuration.  

## Topology

Below is an example of the lab topology in EVE-NG:

![Topology Diagram](images/topology.png)

> In this topology, R1, R2, R4, R5, R6, R7, and R8 are connected via various subnets and OSPF. R3 is bridging to the "cloud" interface that provides DHCP and external connectivity to an Ubuntu VM running Nornir.

## Installation & Usage

1. **Clone** this repository:
   
   git clone https://github.com/YOUR_USERNAME/Nornir-EVE-Telnet-SSH.git
   
   cd Nornir-EVE-Telnet-SSH

## Create and activate a Python virtual environment
  python3 -m venv venv
  source venv/bin/activate

## Install requirements:

  pip install -r requirements.txt

  This installs Nornir, Netmiko, and other dependencies.

## Configure:

Update nornir.yaml if needed.
Edit inventory/hosts.yaml to match your device IPs/ports (Notice that the ports are assigned by EVE, you can see its putting your mouse on the device, on the left-down corner you will see the ip and port).
Modify any script (configure_ssh.py, configure_ospf.py, etc.) as desired.

## Run:
  
  python configure_ssh.py


