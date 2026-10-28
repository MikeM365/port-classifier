def is_port_privileged(port):
    # Ports 0-1023 are "privileged" (well-known) ports, reserved for
    # standard services and typically requiring admin rights to bind to.
    # Ports 1024+ are "unprivileged" and available to any application.
    return port <= 1024


ports_to_check = [1025, 80, 443, 210, 23, 89, 5900, 8800, 9190, 10000]

print("--- Running Port Privilege Classification ---")
for port in ports_to_check:
    privileged = is_port_privileged(port)
    label = "privileged" if privileged else "unprivileged"
    print(f"Port {port} is {label} (boolean value: {privileged})")
