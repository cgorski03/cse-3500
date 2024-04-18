// A C++ program to find convex hull of a set of points. Refer
// https://www.geeksforgeeks.org/orientation-3-ordered-points/
// for explanation of orientation()
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <chrono>
#include <random>
using namespace std;

struct Point
{
  int x, y;
};

// To find orientation of ordered triplet (p, q, r).
// The function returns following values
// 0 --> p, q and r are collinear
// 1 --> Clockwise
// 2 --> Counterclockwise
int orientation(Point p, Point q, Point r)
{
  int val = (q.y - p.y) * (r.x - q.x) -
            (q.x - p.x) * (r.y - q.y);

  if (val == 0)
    return 0;               // collinear
  return (val > 0) ? 1 : 2; // clock or counterclock wise
}

// Prints convex hull of a set of n points.
void convexHull(Point points[], int n)
{
  // There must be at least 3 points
  if (n < 3)
    return;

  // Initialize Result
  vector<Point> hull;

  // Find the leftmost point
  int l = 0;
  for (int i = 1; i < n; i++)
    if (points[i].x < points[l].x)
      l = i;

  // Start from leftmost point, keep moving counterclockwise
  // until reach the start point again. This loop runs O(h)
  // times where h is number of points in result or output.
  int p = l, q;
  do
  {
    // Add current point to result
    hull.push_back(points[p]);

    // Search for a point 'q' such that orientation(p, q,
    // x) is counterclockwise for all points 'x'. The idea
    // is to keep track of last visited most counterclock-
    // wise point in q. If any point 'i' is more counterclock-
    // wise than q, then update q.
    q = (p + 1) % n;
    for (int i = 0; i < n; i++)
    {
      // If i is more counterclockwise than current q, then
      // update q
      if (orientation(points[p], points[i], points[q]) == 2)
        q = i;
    }

    // Now q is the most counterclockwise with respect to p
    // Set p as q for next iteration, so that q is added to
    // result 'hull'
    p = q;

  } while (p != l); // While we don't come to first point
}

// Function to generate random points
void generateRandomPoints(Point points[], int n)
{
  // Use current time as seed for random generator
  unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
  std::default_random_engine generator(seed);
  std::uniform_int_distribution<int> distribution(-1000, 10000);

  // Generate random points
  for (int i = 0; i < n; i++)
  {
    points[i].x = distribution(generator);
    points[i].y = distribution(generator);
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
    Point points[n];
    generateRandomPoints(points, n);

    // Measure the execution time
    auto start = std::chrono::high_resolution_clock::now();

    // Perform convex hull calculation
    convexHull(points, n);

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    total_duration += duration.count();
  }

  // Print the execution time
  std::cout << "Gift WrappingExecution time: " << (total_duration / trials) << " seconds" << std::endl;

  return 0;
}
