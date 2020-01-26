import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    maxi = None
    
    for line in sys.stdin:

        key, valor_1 = line.split("\t")
        valor_1 = int(valor_1)

        if key == curkey:
            maxi=max(valor_1,maxi)

        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, maxi))

            curkey = key
            maxi = valor_1

    sys.stdout.write("{}\t{}\n".format(curkey, maxi))

