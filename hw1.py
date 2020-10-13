a, b, c, d, e, f, g = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
numEdge = (a+b+c+d+f+g) + (a*e) + (b*e) + (c*e) + (c*f) + (d*f) + (e*g)
numPath = g*(a*e + b*e + c*e) + c*f + d*f
print(numEdge)
print(numPath)
