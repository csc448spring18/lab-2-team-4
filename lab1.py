import sys


def read_file(filename):
    fp = open(filename, "r")
    fp.readline()
    toReturn = fp.read()
    fp.close()
    print(toReturn)
    return toReturn


def algorithm(filename):
    s = read_file(filename)
    count = 0
    for i in range(0, len(s)):
       if s[i] == 'G' or s[i] == 'C':
          count += 1
    return (count / len(s)) * 100

def print_results(filename):
    print(algorithm(filename))

if __name__ == "__main__":
    print_results(sys.argv[1])
