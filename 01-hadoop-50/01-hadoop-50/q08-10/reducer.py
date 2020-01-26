import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    suma = None
    total = None
    
    for line in sys.stdin:
        key, valor_1, contador = line.split("\t")
        valor_1 = float(valor_1)
        contador = int(contador)
        
        if key == curkey:
            suma += valor_1
            total += contador
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey,suma,str(suma/total)))

            curkey = key
            suma = valor_1
            total = contador

    sys.stdout.write("{}\t{}\t{}\n".format(curkey,suma,str(suma/total)))
