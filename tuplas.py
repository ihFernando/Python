
def exemplo():
    pal1 = "FATEC"
    pal2 = "ETEC "
    
    z = zip(pal1,pal2)
    d ={}
    for (x,y) in z:
        d[x] = y
    print d
    print z

# CONTAR A FREQUENCIA DAS VOGAIS USANDO UM DICIONARIO

def freq(pal):
    d = {'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
    for letra in pal:
        if letra in "AEIOUaeiou":
            d[letra.upper()] = d[letra.upper()] + 1
    print d

#VERIFICAR A "MAIOR LETRA" EM CADA POSICAO DE
#DUAS PALAVRAS. RETORNE A PALAVRA FORMADA COM AS MAIORES
#LETRAS

def maiores(pal1, pal2):
    z = zip(pal1, pal2)
    aux = ""
    for (l1,l2) in z:
        if ord(l1) > ord(l2):
           aux = aux + l1
        else:
           aux = aux + l2
    return aux
freq("ARARAQUARA EH MTO LEGAL, UHUUu!")

print maiores("JAVA ", "PHP ")

print chr(65)





