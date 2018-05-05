# Run file as:
# python -B input.txt output.txt k ,where k is int from 1 to 5

import sys
from OpenAdress import OpenAdress
from ChainedHash import ChainedHash

file_in = sys.argv[1]
file_out = sys.argv[2]
k = int(sys.argv[3])

def parse(file_in):
    with open(file_in) as file:
        parsed = file.read().split("\n")
        parsed[0] = parsed[0].split(" ")
        if parsed[-1] == '':
            del parsed[-1]
        N = int(parsed[0][0])
        arr = parsed[1:N+1]
        sums = parsed[N+1:]
    return [int(x) for x in arr], [int(x) for x in sums]

def output(file_out, args):
    with open(file_out, "a") as file:
        for arg in args:
            file.write(str(arg) + " ")
        file.write("\n")

# hash functions
def hash_division(data, m):
    return (data % m)

def hash_multiplicate(data, m):
    return int(((data*(2654435761/float(2**32))) % 1)*self.m)

def hash_linear(data, m, i):
    return (hash_division(data, m) + i) % m

def hash_qudratic(data, m, i):
    return (hash_division(data, m) + i + i**2) % m

def hash_double(data, m, i):
    return (hash_division + i*hash_multiplicate(data, m)) % m

# main
def main(file_in, file_out, k):
    array, sums = parse(file_in)
    if k == 1: table = ChainedHash(3*len(array), hash_division)
    elif k == 2: table = ChainedHash(3*len(array), hash_multiplicate)
    elif k == 3: table = OpenAdress(3*len(array), hash_linear)
    elif k == 4: table = OpenAdress(3*len(array), hash_qudratic)
    elif k == 5: table = OpenAdress(3*len(array), hash_double)

    for elem in array:
        table.insert(elem)
    output(file_out, [table.collisions()])

    for S in sums:
        found = False
        for elem in array:
            if(table.include(S-elem)):
                found = True; break
        if(found):
            output(file_out, [elem, S-elem])
        else:
            output(file_out, [0, 0])

# running
if __name__ == "__main__":
    main(file_in, file_out, k)
