import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    for line in sys.stdin:
        letra = line.split(',')[0]
        numero = line.split(',')[1]
        numero = int(numero)
        sys.stdout.write("{},{}\n".format(letra,numero))
