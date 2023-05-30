import socket
from random import randint

def generate_ip():
    ip = []
    for _ in range(4):
        octet = str(randint(0, 255))
        ip.append(octet)
    return '.'.join(ip)

def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

valid_ips = []
invalid_ips = []

while len(valid_ips) < 100:
    ip = generate_ip()
    if is_valid_ip(ip):
        valid_ips.append(ip)
    else:
        invalid_ips.append(ip)

# Salvar todos os IPs gerados em 'ipsGerados.txt'
with open('ipsGerados.txt', 'w') as file:
    file.write('\n'.join(valid_ips + invalid_ips))

# Salvar os IPs válidos em 'ipsValidos.txt'
with open('ipsValidos.txt', 'w') as file:
    file.write('\n'.join(valid_ips))

# Salvar os IPs inválidos em 'ipsInvalidos.txt'
with open('ipsInvalidos.txt', 'w') as file:
    file.write('\n'.join(invalid_ips))
