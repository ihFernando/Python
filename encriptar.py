palavra = input("Qual frase deseja criptografar? ");
def encriptar(k,m):
    aux = ""
    for letra in m:
        # k[letra] -> Olha na tabela
        aux = aux + k[letra] 
    return aux

def montarDicionario(gamma1, gamma2):
    if len(gamma1) != len(gamma2):
        return {}
    else:
        dic = {}
        z = zip(gamma1, gamma2)
        for (x,y) in z:
            dic[x] = y
        return dic
            
chave = montarDicionario(" ABCDEFGHIJKLMNOPQRSTUVWXYZ",
"DP JSQBTKCIHOVAREZULENGXWMF")

print encriptar(chave,format(palavra))