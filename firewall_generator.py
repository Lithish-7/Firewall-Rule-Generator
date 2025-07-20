def generate_iptables_rules(allowed_ports, blocked_ips):
    rules = []

    rules.append("# Allow traffic on loopback interface")
    rules.append("iptables -A INPUT -i lo -j ACCEPT")

    rules.append("# Allow established connections")
    rules.append("iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")

    for port in allowed_ports:
        rules.append(f"iptables -A INPUT -p tcp --dport {port} -j ACCEPT")

    for ip in blocked_ips:
        rules.append(f"iptables -A INPUT -s {ip} -j DROP")

    rules.append("# Drop all other inbound traffic")
    rules.append("iptables -A INPUT -j DROP")

    return "\n".join(rules)

if __name__ == "__main__":
    allowed_ports = input("Enter allowed ports (comma-separated): ").split(",")
    blocked_ips = input("Enter IPs to block (comma-separated): ").split(",")

    allowed_ports = [port.strip() for port in allowed_ports if port.strip().isdigit()]
    blocked_ips = [ip.strip() for ip in blocked_ips if ip.strip()]

    print("\nGenerated iptables rules:\n")
    print(generate_iptables_rules(allowed_ports, blocked_ips))
