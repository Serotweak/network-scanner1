# Network & Port Scanner Tool

A lightweight Python reconnaissance script built in Kali Linux that automates basic network scanning using Nmap and exports findings to text logs.

## Overview
This tool allows you to specify **any target IP address, domain name, or local network range** as a command-line argument. It executes a rapid Nmap port scan against the target and automatically generates a timestamped text file containing the scan output.

## Features
- Accepts custom target inputs (IP addresses, domain names, or CIDR network ranges).
- Performs rapid top-100 port scans using `nmap -F`.
- Displays real-time scan output directly in the terminal.
- Exports structured findings into a target-specific `.txt` file.

## Usage
Run the script using Python 3, followed by the target you want to scan:

```bash
python3 scanner.py <target_ip_or_domain>
