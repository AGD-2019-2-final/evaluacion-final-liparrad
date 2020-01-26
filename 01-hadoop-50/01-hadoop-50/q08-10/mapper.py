import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#

if __name__ == "__main__":
    for line in sys.stdin:
        letra = line.split("   ")[0]
        valor_1 = line.split("   ")[2]
        valor_1 = int(valor_1)
        sys.stdout.write("{}\t{}\t1\n".format(letra,valor_1))
