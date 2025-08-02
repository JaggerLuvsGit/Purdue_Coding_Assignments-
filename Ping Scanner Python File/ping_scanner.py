
# Developed by: Jagger Collins 
import subprocess
import platform
# Prompt for IP range
ip_range = input("Enter the IP range to scan (e.g., 192.168.1.1-192.168.1.254): ")

# Parse the IP range and generate a list of IPs
start_ip, end_ip = ip_range.split('-')
start_parts = list(map(int, start_ip.strip().split('.')))
if '.' in end_ip:
    end_parts = list(map(int, end_ip.strip().split('.')))
else:
    end_parts = start_parts.copy()
    end_parts[3] = int(end_ip.strip())

devices = []
prefix = '.'.join(map(str, start_parts[:3]))
for last_octet in range(start_parts[3], end_parts[3] + 1):
    devices.append(f"{prefix}.{last_octet}")

print(f"Scanning {len(devices)} IP addresses...")
ping_param = "-n" if platform.system().lower() == "windows" else "-c"
timeout_param = "-w" if platform.system().lower() == "windows" else "-W"

results = []
for device in devices:
    # Ping the device and log the result
    try:
        output = subprocess.run(["ping", ping_param, "1", timeout_param, "1", device], 
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if output.returncode == 0:
            results.append(f"{device} is up")
        else:
            results.append(f"{device} is down")
    except Exception as e:
        results.append(f"{device} is down (error: {e})")

# Export results to a file
with open("network_results.txt", "w") as file:
    for result in results:
        file.write(result + "\n")

print(f"Results saved to network_results.txt")
