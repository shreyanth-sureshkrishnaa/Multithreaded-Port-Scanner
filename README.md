# Multithreaded Port Scanner

A simple, fast, and efficient port scanner written in Python that uses multi-threading to scan TCP ports on a target host.

## Features

- **Multi-threaded scanning**: Scans multiple ports simultaneously for faster results
- **Customizable port ranges**: Specify exactly which ports to scan
- **Simple command-line interface**: Easy to use with clear output

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone or download the script
2. Ensure Python 3 is installed on your system

## Usage

### Basic Syntax

```bash
python scanner.py -p <PORT_RANGE_START-PORT_RANGE_END> <target>
```

### Arguments

- `target`: The IP address or domain name to scan (required)
- `-p, --ports`: Port range to scan in format START-END (default: 1-1024)

### Examples

Scan common ports (1-1024) on localhost:
```bash
python scanner.py 127.0.0.1
```

Scan a specific range of ports:
```bash
python scanner.py -p 20-100 127.0.0.1
```

## Legal and Ethical Use

**WARNING**: Only scan networks and systems you own or have explicit permission to test. Unauthorized port scanning may be illegal in your jurisdiction and violate terms of service agreements.

