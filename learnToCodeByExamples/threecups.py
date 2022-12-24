# coci06c5p1
LEFT_AND_MIDDLE='A'
MIDDLE_AND_RIGHT='B'
LEFT_AND_RIGHT='C'

LOCATION_LEFT = 1
LOCATION_MIDDLE = 2
LOCATION_RIGHT = 3

ball_location = LOCATION_LEFT
input = input()

for move in input:
    if move == LEFT_AND_MIDDLE:
        if ball_location == LOCATION_LEFT:
            ball_location = LOCATION_MIDDLE
        elif ball_location == LOCATION_MIDDLE:
            ball_location = LOCATION_LEFT
    elif move == MIDDLE_AND_RIGHT:
        if ball_location == LOCATION_MIDDLE:
            ball_location = LOCATION_RIGHT
        elif ball_location == LOCATION_RIGHT:
            ball_location = LOCATION_MIDDLE
    elif move == LEFT_AND_RIGHT:
        if ball_location == LOCATION_LEFT:
            ball_location = LOCATION_RIGHT
        elif ball_location == LOCATION_RIGHT:
            ball_location = LOCATION_LEFT

print( ball_location)