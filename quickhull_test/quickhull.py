# python program to implement Quick Hull algorithm
# to find convex hull.
import time
import random

# Stores the result (points of convex hull)
hull = set()


# Returns the side of point p with respect to line
# joining points p1 and p2.
def findSide(p1, p2, p):
    val = (p.y - p1.y) * (p2.x - p1.x) - (p2.y - p1.y) * (p.x - p1.x)

    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0


# returns a value proportional to the distance
# between the point p and the line joining the
# points p1 and p2


def lineDist(p1, p2, p):
    dx1 = p.x - p1.x
    dy1 = p.y - p1.y
    dx2 = p2.x - p1.x
    dy2 = p2.y - p1.y
    return (dy1 * dx2 - dy2 * dx1) ** 2


# End points of line L are p1 and p2. side can have value
# 1 or -1 specifying each of the parts made by the line L
def quickHull(a, n, p1, p2, side):
    ind = -1
    max_dist_sq = 0

    for i in range(n):
        temp = lineDist(p1, p2, a[i])
        if (findSide(p1, p2, a[i]) == side) and (temp > max_dist_sq):
            ind = i
            max_dist_sq = temp

    # If no point is found, add the end points
    # of L to the convex hull.
    if ind == -1:
        hull.add("$".join(map(str, p1)))
        hull.add("$".join(map(str, p2)))
        return

    # Recur for the two parts divided by a[ind]
    quickHull(a, n, a[ind], p1, -findSide(a[ind], p1, p2))
    quickHull(a, n, a[ind], p2, -findSide(a[ind], p2, p1))


def printHull(a, n):
    # a[i].second -> y-coordinate of the ith point
    if n < 3:
        print("Convex hull not possible")
        return

    # Finding the point with minimum and
    # maximum x-coordinate
    min_x = 0
    max_x = 0
    for i in range(1, n):
        if a[i].x < a[min_x].x:
            min_x = i
        if a[i].x > a[max_x].x:
            max_x = i

    # Recursively find convex hull points on
    # one side of line joining a[min_x] and
    # a[max_x]
    quickHull(a, n, a[min_x], a[max_x], 1)

    # Recursively find convex hull points on
    # other side of line joining a[min_x] and
    # a[max_x]
    quickHull(a, n, a[min_x], a[max_x], -1)
