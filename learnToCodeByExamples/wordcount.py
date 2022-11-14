import sys
import re


def wordcount(input_string):
    return len(re.findall('\\S+', str(input_string or '')))


if __name__ == '__main__':
    wordcount(sys.argv[1])
