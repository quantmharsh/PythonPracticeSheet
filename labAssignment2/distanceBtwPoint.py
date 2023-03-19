import math

# function to calculate distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# read the number of points
n = int(input("Enter the number of points: "))

# read the coordinates of the points
points = []
for i in range(n):
    x, y = map(float, input(f"Enter coordinates of point {i+1}: ").split())
    points.append((x, y))

# initialize variables to store farthest points and distance
max_distance = 0
farthest_points = (0, 0)

# iterate through all possible pairs of points
for i in range(n):
    for j in range(i+1, n):
        # calculate distance between current pair of points
        d = distance(points[i][0], points[i][1], points[j][0], points[j][1])
        # update farthest points and distance if necessary
        if d > max_distance:
            max_distance = d
            farthest_points = (i+1, j+1)

# print the indices of farthest points and distance between them
print(f"The farthest points are {farthest_points} with a distance of {max_distance:.2f}")
