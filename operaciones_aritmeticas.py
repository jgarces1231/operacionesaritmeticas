# Ejercico N.3 para calcular la suma,resta,multiplicacion,division,division entera,modulo y potencia

# input 

X=int(input("Digite primer valor de X: "))
Y=int(input("Digite segundo valor de Y: "))

# Prosessing 
S= X+Y 
R= X-Y 
M= X*Y
D= X/Y
DE= X//Y
MOD= X%Y 
P= X**Y

# Output

print("-------------------")
print("La suma de " + str(X) + " + " + str(Y) + " es " + str(S))
print("La resta de " + str(X) + " - " + str(Y) + " es " + str(R))
print("La multiplicacion de " + str(X) + " * " + str(Y) + " es " + str(M))
print("La division de " + str(X) + " / " + str(Y) + " es " + str(M))
print("La division enterda de " + str(X) +  " // " + str(Y) + " es " + str(DE))
print("El modulo  de " + str(X) +  " % " + str(Y) + " es " + str(MOD))
print("La potencia de " + str(X) +  " ** " + str(Y) + " es " + str(P))
print("-------------------")