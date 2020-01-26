import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    maximum = None
    minimum = None
    
    for line in sys.stdin:

        key, valor_1 = line.split("\t")
        
        if key == curkey:
            maximum = max(maximum, valor_1)
            minimum = min(minimum, valor_1)
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey,maximum,minimum))
                
            curkey = key
            maximum = valor_1
            minimum = valor_1
            
    sys.stdout.write("{}\t{}\t{}\n".format(curkey,maximum,minimum))