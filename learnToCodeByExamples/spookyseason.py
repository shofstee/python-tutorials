import sys

# Solution wc16c1j1
def calculate_spookines(spook_factor):
    spookiness = 'o' * spook_factor
    return 'sp' + spookiness + 'ky'

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Enter the spook factor:')
        input = input()
    else:
        input = sys.argv[1]
    
    if int(input) >= 2:
        print(f"It's a {calculate_spookines(int(input))} season!")
    else:
        print("It's not spooky at all!")