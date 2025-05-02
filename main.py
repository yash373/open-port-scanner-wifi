# Imports
import ipaddress
import socket
import os

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# Get network range of wifi
def get_subnet(ip_address_with_prefix):
  """
  Extracts the subnet from an IP address string with a prefix length.

  Args:
    ip_address_with_prefix: A string representing the IP address and prefix 
      length (e.g., "192.168.1.10/24").

  Returns:
    An ipaddress.IPv4Network or ipaddress.IPv6Network object representing the 
    subnet, or None if the input is invalid.
  """
  try:
    network = ipaddress.ip_network(ip_address_with_prefix, strict=False)
    return network
  except ValueError:
    return None

# Run nmap to get open ports on network range
def run_nmap(subnet):
    os.system(f"nmap -p- {subnet}")

# Run Script
if __name__ == "__main__":
    run_nmap(get_subnet(f"{IPAddr}"))