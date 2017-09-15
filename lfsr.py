#Gerador
#Gerador sera um objeto da classe dos geradores

def g1():
    yield 1
    yield 2
    yield 3
    yield 4

def g2():
    i = 0
    #Loop infinito
    while True:
        yield i
        i = i + 2
    
def g3(seed):
    x = []
    for n in seed:
        x.append(int(n))
    i = 0
    print x
    while True:
        # x[1+2]
        formula = x[i+1] ^ x[1]
        x.append(formula)
        yield formula
        i = i + 1

gerador = g3("0110")
print "Digite quantos numeros: "
n = int(raw_input())
for i in range(n):
    print gerador.next()