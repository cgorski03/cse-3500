#include "gift_wrapping.cpp"
#include "graham_scan.cpp"
#include "quickhull.cpp"
#include "hull.h"
#include <iostream>

int main()
{
  Point a[] = {{0, 3}, {1, 1}, {2, 2}, {4, 4}, {0, 0}, {1, 2}, {3, 1}, {3, 3}};
  int n = sizeof(a) / sizeof(a[0]);
  run_quick_hull(a, n);
  return 0;
}