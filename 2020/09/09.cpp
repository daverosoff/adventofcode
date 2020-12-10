#include <iostream>
#include <fstream>
#include <vector>
#include "timing.hpp"

class Puzzle09
{
public:
  Puzzle09(std::string filename = "input");
  int64_t part_one(size_t preamble_length = 25);
  int64_t part_two(int64_t target);
  std::vector<int64_t> lines;
};

Puzzle09::Puzzle09(std::string filename)
{
  std::vector<int64_t> tempv;
  std::ifstream ifs;
  ifs.open(filename);
  for (std::string line; std::getline(ifs, line); )
  {
    tempv.push_back(std::stoll(line));
  }
  ifs.close();
  this->lines = tempv;
}

int64_t Puzzle09::part_one(size_t preamble_length)
{
  for (size_t i = preamble_length; i < lines.size(); ++i)
  {
    size_t current_begin = i - preamble_length;
    size_t current_end = i; // one past end as usual
    bool found = false;
    for (size_t j = current_begin; j < current_end && !found; ++j)
    {
      for (size_t k = current_begin; k < current_end && !found; ++k)
      {
        if (k != j && (lines[j] + lines[k] == lines[i])) { found = true; }
      }
    }
    if (!found) { return lines[i]; }
  }
  return -1;
}

int64_t Puzzle09::part_two(int64_t target)
{

}

int main()
{
  Puzzle09 p("input");
  dwr::Clock cl;
  auto t0 = cl.now();
  auto p1 = p.part_one(25);
  auto t1 = cl.now();
  dwr::Duration elapsed = t1 - t0;
  std::cout << p1 << " (" << elapsed.count() << " µs)" << std::endl;
}
