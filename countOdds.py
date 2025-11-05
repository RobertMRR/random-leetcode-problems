# Count Odd Numbers in an Interval Range
def countOdds(low, high):
    if low % 2 == 0:
        return (high-low+1)//2
    return (high-low)//2 + 1

print(countOdds(798273637, 970699661))