# Roboty bounded in circle
def isRobotBounded(instructions):
    position = [0,0]
    direction = 0
    for i, step in enumerate(instructions*4):
        if step == "L":
            if direction == 0:
                direction = 360-90
            else:
                direction -= 90
        elif step == "R":
            if direction == 360:
                direction = 0 + 90
            else:
                direction += 90
        else:
            if direction == 0 or direction == 360:
                position[1] += 1
            elif direction == 90:
                position[0] += 1
            elif direction == 180:
                position[1] -= 1
            else:
                position[0] -= 1
            if position == [0,0] and i-1%len(instructions) == 0:
                    print(f"i is: {i}, len is {len(instructions)}")
                    return True
        print(f"position is: {position}, step is {step}")
    return position == [0,0]

print(isRobotBounded("GLGLGGLGL"))
print(isRobotBounded("GL"))