import sys

PI = 3.141592653589793

# Solution for dmopc14c5p1
def calculate_cone_volume(radius, height):
    return (PI * radius ** 2 * height) / 3    


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Enter radius:')
        radius = input()
        print('Enter height:')
        height = input()
    elif len(sys.argv) == 3:
        radius = sys.argv[1]
        height = sys.argv[2]
    else:
        print("Use this program with a radius and a height.")
        exit(-1)
    
    print('Volume', calculate_cone_volume(int(radius), int(height)))