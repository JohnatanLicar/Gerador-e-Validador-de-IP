from random import randint
ips=''
for total in range(0, 101):
    ip = ' '
    for c in range(0, 4):
        número = randint(1, 500)
        if c > 0:
            ip += '.'
        ip += str(número)
    ips += ip + '\n'
with open('IpsGerados.txt', 'w') as SalvaIps:
    SalvaIps.write(ips)
