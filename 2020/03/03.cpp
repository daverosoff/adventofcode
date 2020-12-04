#include <iostream>
#include <fstream>
#include <vector>
#include "timing.hpp"

size_t count_trees(std::vector<std::string> map, size_t deltax, size_t deltay);

int main()
{
  std::ifstream ifs;
  std::vector<std::string> ourmap;
  ifs.open("input");
  for (std::string line; getline(ifs, line); )
  {
    ourmap.push_back(line);
  }

  dwr::Clock cl;
  auto t0 = cl.now();
  auto p1 = count_trees(ourmap, 3, 1);
  auto t1 = cl.now();
  dwr::Duration elapsed = t1 - t0;

  std::cout << "Part One: " << p1 << ", " << elapsed.count() << " µsec" << std::endl;

  t0 = cl.now();
  int p2 = 1;
  p2 *= count_trees(ourmap, 1, 1);
  p2 *= count_trees(ourmap, 3, 1);
  p2 *= count_trees(ourmap, 5, 1);
  p2 *= count_trees(ourmap, 7, 1);
  p2 *= count_trees(ourmap, 9, 1);
  p2 *= count_trees(ourmap, 1, 2);
  t1 = cl.now();
  elapsed = t1 - t0;

  std::cout << "Part Two: " << p2 << ", " << elapsed.count() << " µsec" << std::endl;

}

size_t count_trees(std::vector<std::string> map, size_t deltax, size_t deltay)
{
  auto num_lines = map.size();
  auto map_width = map[0].length();
  size_t result = 0;
  size_t x = 0;
  size_t y = 0;

  while (y < num_lines)
  {
    if (map[y][x] == '#') { ++result; }
    x = (x + deltax) % map_width;
    y += deltay;
  }

  return result;
}
