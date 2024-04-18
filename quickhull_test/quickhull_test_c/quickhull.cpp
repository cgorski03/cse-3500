// C++ program to implement Quick Hull algorithm
// to find convex hull.
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <chrono>
#include <random>
using namespace std;

// iPair is integer pairs
#define iPair pair<int, int>

// Stores the result (points of convex hull)
set<iPair> hull;

// Returns the side of point p with respect to line
// joining points p1 and p2.
int findSide(iPair p1, iPair p2, iPair p)
{
  int val = (p.second - p1.second) * (p2.first - p1.first) -
            (p2.second - p1.second) * (p.first - p1.first);

  if (val > 0)
    return 1;
  if (val < 0)
    return -1;
  return 0;
}

// returns a value proportional to the distance
// between the point p and the line joining the
// points p1 and p2
int lineDist(iPair p1, iPair p2, iPair p)
{
  return abs((p.second - p1.second) * (p2.first - p1.first) -
             (p2.second - p1.second) * (p.first - p1.first));
}

// End points of line L are p1 and p2. side can have value
// 1 or -1 specifying each of the parts made by the line L
void quickHull(iPair a[], int n, iPair p1, iPair p2, int side)
{
  int ind = -1;
  int max_dist = 0;

  // finding the point with maximum distance
  // from L and also on the specified side of L.
  for (int i = 0; i < n; i++)
  {
    int temp = lineDist(p1, p2, a[i]);
    if (findSide(p1, p2, a[i]) == side && temp > max_dist)
    {
      ind = i;
      max_dist = temp;
    }
  }

  // If no point is found, add the end points
  // of L to the convex hull.
  if (ind == -1)
  {
    hull.insert(p1);
    hull.insert(p2);
    return;
  }

  // Recur for the two parts divided by a[ind]
  quickHull(a, n, a[ind], p1, -findSide(a[ind], p1, p2));
  quickHull(a, n, a[ind], p2, -findSide(a[ind], p2, p1));
}

void printHull(iPair a[], int n)
{
  // a[i].second -> y-coordinate of the ith point
  if (n < 3)
  {
    cout << "Convex hull not possible\n";
    return;
  }

  // Finding the point with minimum and
  // maximum x-coordinate
  int min_x = 0, max_x = 0;
  for (int i = 1; i < n; i++)
  {
    if (a[i].first < a[min_x].first)
      min_x = i;
    if (a[i].first > a[max_x].first)
      max_x = i;
  }

  // Recursively find convex hull points on
  // one side of line joining a[min_x] and
  // a[max_x]
  quickHull(a, n, a[min_x], a[max_x], 1);

  // Recursively find convex hull points on
  // other side of line joining a[min_x] and
  // a[max_x]
  quickHull(a, n, a[min_x], a[max_x], -1);
}
// Function to generate random points
void generateRandomPoints(iPair points[], int n)
{
  // Use current time as seed for random generator
  unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
  std::default_random_engine generator(seed);
  std::uniform_int_distribution<int> distribution(-1000, 10000);

  // Generate random points
  for (int i = 0; i < n; i++)
  {
    points[i].first = distribution(generator);
    points[i].second = distribution(generator);
  }
}

int main(int argc, char *argv[])
{
  if (argc != 3)
  {
    std::cout << "Usage: ./program_name <number_of_points> <number_of_trials>" << std::endl;
    return 1;
  }

  int n = std::stoi(argv[1]);      // Number of points
  int trials = std::stoi(argv[2]); // Number of trials
  if (n <= 0)
  {
    std::cout << "Number of points must be a positive integer" << std::endl;
    return 1;
  }
  double total_duration = 0.0;
  for (int i = 0; i < trials; i++)
  {
    // Generate random points
    iPair points[n];
    generateRandomPoints(points, n);

    // Measure the execution time
    auto start = std::chrono::high_resolution_clock::now();

    // Perform convex hull calculation
    printHull(points, n);

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    total_duration += duration.count();
  }

  // Print the execution time
  std::cout << "Quickhull Execution time: " << (total_duration / trials) << " seconds" << std::endl;

  return 0;
}
