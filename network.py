def is_port_secure(port):
  #Let's say ports below 1024 are considered "privledged" (special) ports.
  #We'll consider a "secure" port to be one above 1024.
  return port > 1024



ports_to_check = [1025, 80, 443, 210, 23, 89, 5900, 8800, 9190, 10000]
    
for port in ports_to_check:
  secure = is_port_secure(port)
  print(f"Port {port} is {'secure' if secure else 'not secure'} (boolean value: {secure})")