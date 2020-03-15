n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo Valor: "))

s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2

print("A SOMA É {}, O PRODUTO É {} E A DIVISÃO É {:.3f} ".format(s,m,d))
print("Divisão inteira {} e potencia {} ".format(di,p))