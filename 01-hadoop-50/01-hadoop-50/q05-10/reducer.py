import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    total = 0
    
    for line in sys.stdin:

        key, valor_1 = line.split("\t")
        valor_1 = int(valor_1)

        if key == curkey:
            total += valor_1
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, total))

            curkey = key
            total = valor_1

    sys.stdout.write("{}\t{}\n".format(curkey, total))