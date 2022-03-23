def polysum(n, s):
    '''
    n: number of sides of the polygon
    s: length of each side
    returns the sum of the area and square of the permiter of a regular polygon
    '''
    import math
    areaOfPolygon = 0.25 * n * s**2 / math.tan(math.pi / n)
    perimeterOfPolygon = (n * s)**2

    return round(areaOfPolygon + perimeterOfPolygon, 4)

# Test Cases
print(polysum(56, 20)) #1354117.2386
print(polysum(87, 23)) #4322490.7717
print(polysum(73, 19)) #2076763.1516
print(polysum(60, 2)) #15544.8682
print(polysum(90, 53)) #24562782.7981
print(polysum(71, 77)) #32264955.1408
print(polysum(96, 1)) #9949.1242
print(polysum(55, 66)) #14224343.7386
print(polysum(26, 98)) #7006428.3648
print(polysum(54, 68)) #14555362.6885