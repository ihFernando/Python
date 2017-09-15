def otp(k,m):
    z = zip(k,m)
    aux = ""
    for (key,msg) in z:
        xr = ord(key) ^ ord(msg)
        aux = aux + chr(xr)
    return aux.encode("hex")
    # Decode tira
    
print otp("C4RL0S","CARLOS")