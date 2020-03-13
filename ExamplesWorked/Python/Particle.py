speed = [10,8,3,6,3,2,2,4,8,1,6,7]
pos = 2

def collision(speed, pos):
    print(speed)
    i = 0
    while i < int(len(speed)):
        possible_collision = speed[0]
        print(possible_collision)
        i=i+1
    return possible_collision

collision(speed, pos)