// Input parsing utilities for AoC 2020.
// Dave Rosoff, 2020.

#ifndef DWR_PUZZLE_INPUT_H
#define DWR_PUZZLE_INPUT_H

#include <fstream>
#include <string>
#include <vector>

namespace dwr
{
  std::ifstream& get_puzzle_input(std::string filename)
  {
    std::ifstream ifs;
    ifs.open(filename);

    return ifs;
  }

  std::vector<std::string> parse_into_lines(std::ifstream& puzzle_input)
  {
    std::vector<std::string> result;
    std::string cursor;
    while (std::getline(puzzle_input, cursor))
    {
      result.push_back(cursor);
    }

    return result;
  }

  std::vector<std::string> parse_into_words(std::ifstream& puzzle_input)
  {
    std::vector<std::string> result;
    std::string cursor;
    while (puzzle_input >> cursor)
    {
      result.push_back(cursor);
    }

    return result;
  }

  std::vector<int> parse_into_ints(std::ifstream& puzzle_input)
  {
    std::vector<int> result;
    int cursor;
    while (puzzle_input >> cursor)
    {
      result.push_back(cursor);
    }

    return result;
  }
}

#endif
