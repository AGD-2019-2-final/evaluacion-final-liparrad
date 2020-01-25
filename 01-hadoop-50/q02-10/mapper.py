import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    for line in sys.stdin:
        varible_1 = line.split(',')[3]
        variable_2 = line.split(',')[4]
        sys.stdout.write("{}\t{}\n".format(varible_1,variable_2))