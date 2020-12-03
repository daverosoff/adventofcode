#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include "timing.hpp"

bool is_valid(size_t min, size_t max, char letter, std::string password);

bool is_valid_two(size_t min, size_t max, char letter, std::string password);

int main()
{
  std::ifstream ifs;
  ifs.open("input1");
  std::vector<std::string> policies;
  for (std::string line; getline(ifs, line); )
    policies.push_back(line);
  ifs.close();

  size_t part_one = 0;
  size_t part_two = 0;
  for (auto pol : policies)
  {
    std::istringstream iss(pol);
    size_t min;
    iss >> min;
    iss.ignore(1, '-');
    size_t max;
    iss >> max;
    iss.ignore(1, ' ');
    char letter;
    iss >> letter;
    iss.ignore(1, ':');
    std::string password;
    iss >> password;
    if (is_valid(min, max, letter, password)) { part_one++; }
    if (is_valid_two(min, max, letter, password)) { part_two++; }
  }
  std::cout << "Part One: " << part_one << std::endl;
  std::cout << "Part Two: " << part_two << std::endl;
}

bool is_valid(size_t min, size_t max, char letter, std::string password)
{
  size_t count = 0;
  for (char ch : password)
  {
    if (ch == letter) { ++count; }
  }
  return (min <= count && count <= max);
}

bool is_valid_two(size_t min, size_t max, char letter, std::string password)
{
  size_t count = 0;
  return ((password[min-1] == letter) != (password[max-1] == letter));
}
