import sys
import subprocess
from datetime import datetime

def run_scan(target_ip):
    print(f"[*] Starting scan on target: {target_ip}")
    print(f"[*] Time started: {str(datetime.now())}\n")
    
    # Run a simple nmap scan against the top 100 ports
    command = f"nmap -F {target_ip}"
    
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        print(output)
        
        # Save scan output to a file
        filename = f"scan_results_{target_ip.replace('.', '_')}.txt"
        with open(filename, "w") as file:
            file.write(output)
            
        print(f"[*] Scan complete! Results saved to {filename}")
        
    except subprocess.CalledProcessError as e:
        print(f"[-] Error running Nmap scan: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scanner.py <target_ip>")
        print("Example: python3 scanner.py 127.0.0.1")
    else:
        target = sys.argv[1]
        run_scan(target)
