import socket
import argparse
import threading
from datetime import datetime

def scan(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketobject:
            socketobject.settimeout(0.5)
            if socketobject.connect_ex((ip, port)) == 0:
                print(f"[+] Port {port:<5} ---> OPEN")
            
    except:
        pass

def main():

    # Argument Parsing:
    parser = argparse.ArgumentParser(description= "A simple multi-threaded port scanner.")
    parser.add_argument("target", help="the IP address or domain to scan.")
    parser.add_argument("-p", "--ports", help="Port Range. For Example, 1-1024", default="1-1024")
    args = parser.parse_args()

    # Parsing the port range:

    try:
        start, end = map(int, args.ports.split('-'))

    except ValueError:
        print("[X] Error: Incorrect Format. Use format START-END (ex. 1-1000)")
        return
    
    # UI Setup

    print("-" * 60)
    print(f"Scanning Target: {args.target}")
    print(f"Scanning Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    threads = []
    for port in range(start, end + 1):

        t = threading.Thread(target=scan, args=(args.target, port))
        threads.append(t)
        t.start()

        # Limit to 100 threads at a time to prevent crashing your OS
        if len(threads) >= 100:
            for t in threads:
                t.join()
            threads = []

# Final cleanup for remaining threads
    for t in threads:
        t.join()

    print("-" * 50)
    print("Scan completed successfully.")

if __name__ == "__main__":
    main()