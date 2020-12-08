#include <iostream>
#include <fstream>
#include <sstream>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <utility>
#include <cctype>
#include "timing.hpp"

std::vector<std::string> needed_keys = { "byr", "iyr", "hgt", "ecl", "hcl", "pid", "eyr" };
using Passport = std::unordered_map<std::string, std::string>;

bool byr(std::string byrv)
{
  auto i = stoi(byrv);
  return (i >= 1920 and i <= 2002);
}

bool iyr(std::string iyrv)
{
  auto i = stoi(iyrv);
  return (i >= 2010 and i <= 2020);
}

bool eyr(std::string eyrv)
{
  auto i = stoi(eyrv);
  return (i >= 2020 and i <= 2030);
}

bool hgt(std::string hgtv)
{
  auto len = hgtv.length();
  auto val = hgtv.substr(0, len - 2);
  if (not (all_of(begin(val), end(val), [](char ch){isdigit(ch);})))
  {
    return false;
  }
  else
  {
    auto val_i = stoi(val);
    auto unit = hgtv.substr(len - 2);
    if (unit == "cm") { return ((val_i >= 150) and (val_i <= 193)); }
    else if (unit == "in") { return (val_i >= 59) and (val_i <= 76); }
    else { return false; }
  }
}

bool ecl(std::string eclv)
{
  static std::vector<std::string> ecl_valid = {
    "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
  };
  for (const auto& st : ecl_valid)
  {
    if (eclv == st) { return true; }
  }
  return false;
}

bool ishexdigit(char ch)
{
  switch (ch)
  {
    case '0':
    case '1':
    case '2':
    case '3':
    case '4':
    case '5':
    case '6':
    case '7':
    case '8':
    case '9':
    case 'a':
    case 'b':
    case 'c':
    case 'd':
    case 'e':
    case 'f': return true;
    default : return false;
  }
}

bool hcl(std::string hclv)
{
  auto it = begin(hclv);
  return ((hclv.length() == 7) and (hclv[0] == '#')
    and all_of(++it, end(hclv), ishexdigit));
}

bool pid(std::string pidv)
{
  return (pidv.length() == 9) and all_of(begin(pidv), end(pidv), isdigit);
}

std::vector<bool (*)(std::string)> validators_v = {
  &byr, &iyr, &hgt, &ecl, &hcl, &pid, &eyr // same order as needed_keys
};

bool is_valid(Passport pp)
{
  if (pp.size() < 7) { return false; }
  for (size_t i = 0; i < validators_v.size(); ++i)
  {
    if (!(validators_v[i](needed_keys[i]))) { return false; }
  }
  return true;
}

int main()
{
  std::ifstream ifs;
  ifs.open("input");
  bool first = true;
  Passport pp;
  for(std::string line; getline(ifs, line); )
  {
    if (line != "")
    {
      if (first)
      {
        pp = Passport();
        first = false;
      }
      std::ostringstream iss;
      iss << line;
    }
  }
}
