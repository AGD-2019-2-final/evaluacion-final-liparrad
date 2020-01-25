import sys
import operator
from operator import itemgetter

#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':

    sort = sorted(sys.stdin, key=itemgetter(2))
       
    for line in sort:
        key, valor_1 = line.split(",")
        valor_1 = int(valor_1)
        
        sys.stdout.write("{},{}\n".format(key, valor_1))