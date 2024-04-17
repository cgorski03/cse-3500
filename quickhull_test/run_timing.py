import random
from graham_scan import convexHull as graham_scan
from quickhull import printHull as quickHull
from Wrapping import convexHull as wrapping
import time

graph_sizes = [5, 10, 100, 1000, 10000, 100000, 250000, 400000, 1000000]
# graph_sizes = [100000]
TRIALS = 1


# A class used to store the x and y coordinates of points
class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __iter__(self):
        return iter([self.x, self.y])


def randList(n):
    point_list_Point = []
    for _ in range(n):
        randx = random.randint(0, 1000)
        randy = random.randint(0, 1000)
        point1 = Point(randx, randy)
        point_list_Point.append(point1)
    return point_list_Point


def run_timing(points_list, algorithm, n_points):
    start_time = time.time()
    algorithm(points_list, n_points)
    end_time = time.time()
    return end_time - start_time


def run_timing_for_n_trials(n_trials, algorithm, n_points):
    total_time = 0
    for _ in range(n_trials):
        print(
            f"Running trial {_ + 1} of {n_trials} for {algorithm.__name__} \r", end=""
        )
        points_list = randList(n_points)
        total_time += run_timing(points_list, algorithm, n_points)
    return total_time / n_trials


if __name__ == "__main__":
    algorithms = [graham_scan, quickHull, wrapping]
    algorithm_names = ["Graham Scan", "Quick Hull", "Wrapping"]

    for n_points in graph_sizes:
        print(f"\nNumber of points: {n_points}")
        for algorithm, name in zip(algorithms, algorithm_names):
            avg_time = run_timing_for_n_trials(TRIALS, algorithm, n_points)
            print(f"Average time for {name}: {avg_time:.6f} seconds {' ' * 10}")
