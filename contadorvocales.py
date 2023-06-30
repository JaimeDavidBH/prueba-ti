texto = "wellcome to the jungle"

cont_a = 0

for i in texto:
    if (i=="a" or i=="e"):
        if(i=="a"):
            cont_a += 1
        print("es una vocal")
    elif(i==" "):
        print("es un espacio")
    else:
        print("es una consonante")

cont_e = 0
for i in texto:
    if (i=="e" or i=="a"):
        if(i=="e"):
            cont_a += 1

cont_i = 0
for i in texto:
    if (i=="i" or i=="a"):
        if(i=="i"):
            cont_a += 1

cont_o = 0
for i in texto:
    if (i=="o" or i=="a"):
        if(i=="o"):
            cont_o += 1

cont_u = 0
for i in texto:
    if (i=="u" or i=="a"):
        if(i=="u"):
            cont_o += 1
print(f"la cantidad de la vocal e es {cont_a}")
print(f"la cantidad de la vocal a es {cont_e}")
print(f"la cantidad de la vocal i es {cont_i}")
print(f"la cantidad de la vocal o es {cont_o}")
print(f"la cantidad de la vocal u es {cont_u}")