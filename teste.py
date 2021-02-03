from conta import *
from cliente import *

cliente = Cliente('João', 'Mesquita', 1997)
conta = Conta(123, cliente, 3500, 5000)

print(conta)
