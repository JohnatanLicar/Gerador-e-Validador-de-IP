def ipOK(ip):
    for n in ip.split('.'):
        if int(n) < 255:
            check = True
        else:
            return False
    return check


ips = open('IpsGerados.txt', 'r')
ipsvalido = open('IpsValidos.txt', 'w')
ipsInvalidos = open('IpsInvalidos.txt', 'w')
for i in ips.readlines():
    if ipOK(i):
        ipsvalido.write(i)
    else:
        ipsInvalidos.write(i)
ips.close()
ipsvalido.close()
ipsInvalidos.close()
with open('IpsValidos.txt', 'r') as Ler:
    print(Ler.read())
