import sys
import re

# Solution for dmopc15c7p2
def wordcount(input_string):
    return len(re.findall('\\S+', str(input_string or '')))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Enter a text:')
        input = input()
    else:
        input = sys.argv[1]
    
    print('Wordcount', wordcount(input))
