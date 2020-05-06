#O valor da variável NUMERO é iniciado com zero. 
NUMERO = int(0)

#Desde que a variável "NUMERO" esteja entre 0 e 1000, o comando IF será acionado.
for NUMERO in range(0, 1000):
    if NUMERO % 3 == 0:
        print(NUMERO)
