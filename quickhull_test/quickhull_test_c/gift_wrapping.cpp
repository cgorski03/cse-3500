// A C++ program to find convex hull of a set of points. Refer
// https://www.geeksforgeeks.org/orientation-3-ordered-points/
// for explanation of orientation()
#include <iostream>
#include <stack>
#include <stdlib.h>
#include "hull.h"
using namespace std;

// To find orientation of ordered triplet (p, q, r).
// The function returns following values
// 0 --> p, q and r are collinear
// 1 --> Clockwise
// 2 --> Counterclockwise

// Prints convex hull of a set of n points.
void gift_wrapping_hull(Point points[], int n)
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

  // Print Result
  for (int i = 0; i < hull.size(); i++)
    cout << "(" << hull[i].x << ", "
         << hull[i].y << ")\n";
}
