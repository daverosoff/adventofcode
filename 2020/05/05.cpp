#include <vector>
#include <iostream>
#include <fstream>
#include <cmath>

int interpret(char ch)
{
  switch (ch)
  {
    case 'F': return 0;
    case 'B': return 1;
    case 'L': return 0;
    case 'R': return 1;
  }
}

int convert(std::string pass)
{
  int result = 0;
  for (size_t i = pass.length(); i --> 0; )
  {
    if (interpret(pass[i]))
    {
      result += pow(2, pass.length() - 1 - i);
    }
  }
  return result;
}

int main()
{
  std::ifstream ifs;
  ifs.open("input");
  int max = 0;
  std::vector<std::string> passes;
  for (std::string line; getline(ifs, line); )
  {
    passes.push_back(line);
    int current = convert(line);
    if (current > max) { max = current; }
  }
  std::cout << "Part 1: " << max << std::endl;

  std::vector<int> ids(passes.size());
  for (size_t i = 0; i < ids.size(); ++i)
  {
    ids[i] = convert(passes[i]);
  }

  sort(begin(ids), end(ids));

  for (size_t i = 1; i < ids.size()-1; ++i)
  {
    if (ids[i-1] == ids[i] - 2)
    {
      std::cout << "Part Two: " << ids[i] << std::endl;
      break;
    }
  }
}
