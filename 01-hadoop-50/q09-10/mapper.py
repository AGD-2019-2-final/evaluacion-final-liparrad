import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#

if __name__ == "__main__":

    for line in sys.stdin:
       
        letra = line.split("   ")[0]
        fecha = line.split("   ")[1]
        valor_1 = line.split("   ")[2]
        valor_1 = int(valor_1)
        sys.stdout.write("{}\t{}\t{}\t{}\n".format(str(valor_1/100),letra,fecha,valor_1))
