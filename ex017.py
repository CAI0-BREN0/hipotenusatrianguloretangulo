import math
print("vamos calcular o comprimento da hipotenusa de um triângulo retângulo")
n1 = float(input("qual o comprimento do cateto oposto ?"))
n2 = float(input("qual o comprimento do cateto adjacente ?"))
print(" usando o teorema de pitagoras {}² + {}² = √{} logo comprimento da hipotenusa  sera {}" .format(n1,n2,(math.pow(n1, 2)+math.pow(n2, 2)),math.hypot(n1,n2)))