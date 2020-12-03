#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <algorithm>
#include "timing.hpp"

using report = std::vector<int>;

// int part_one(report entries)
// Post: The return value is the product of a pair of entries whose sum is 2020.
//       If there is no such pair, the return value is -1.

// int part_two(report entries)
// Post: The return value is the product of a triple of entries whose sum is 2020.
//       If there is no such triple, the return value is -1.

// int prob_one(report entries, size_t n, int target)
// Post: The return value is the product of an n-tuple of entries whose sum is target.
//       If there is no such n-tuple, the return value is -1.

int part_one(const report& entries);
int part_two(const report& entries);
int prob_one(const report& entries, size_t n, int target, int cumulative);

int main()
{
  ///////// GET INPUT /////////
  std::ifstream ifs;
  ifs.open("input1");
  report entries;
  int holder;
  while (ifs >> holder)
    entries.push_back(holder);
  ifs.close();

  ///////// COMPUTE ANSWERS WITH ITERATION AND TIMING /////////
  dwr::Clock cl;

  auto start1 = cl.now();
  auto p1 = part_one(entries);
  auto end1 = cl.now();
  dwr::Duration elapsed1 = end1 - start1;

  auto start2 = cl.now();
  auto p2 = part_two(entries);
  auto end2 = cl.now();
  dwr::Duration elapsed2 = end2 - start2;

  ///////// PRINT RESULTS
  std::cout << "Part One: " << p1 << " (" << elapsed1.count() << " µsec)" << std::endl;
  std::cout << "Part Two: " << p2 << " (" << elapsed2.count() << " µsec)" << std::endl;

  ///////// COMPUTE ANSWERS WITH ITERATION AND TIMING /////////
  std::cout << "-- Using recursive solution --" << std::endl;

  start1 = cl.now();
  p1 = prob_one(entries, 2, 2020, 1);
  end1 = cl.now();
  elapsed1 = end1 - start1;

  start2 = cl.now();
  p2 = prob_one(entries, 3, 2020, 1);
  end2 = cl.now();
  elapsed2 = end2 - start2;

  ///////// PRINT RESULTS
  std::cout << "Part One: " << p1 << " (" << elapsed1.count() << " µsec)" << std::endl;
  std::cout << "Part Two: " << p2 << " (" << elapsed2.count() << " µsec)" << std::endl;
}

int part_one(const report& entries)
{
  size_t entries_len = entries.size();
  // Check every pair of entries to see if the sum is right.
  // If it is, return the product of the pair of entries.
  // If we run out of pairs, return the "error" value -1.
  for (size_t i = 0; i < entries_len; ++i)
    for (size_t j = 0; j < entries_len; ++j)
      if (entries[i] + entries[j] == 2020)
        return entries[i] * entries[j];
  return -1;
}

int part_two(const report& entries)
{
  size_t entries_len = entries.size();
  // Check every triple of entries to see if the sum is right.
  // If it is, return the product of the three entries.
  // If we run out of triples, return the "error" value -1.
  for (size_t i = 0; i < entries_len; ++i)
    for (size_t j = 0; j < entries_len; ++j)
      for (size_t k = 0; k < entries_len; ++k)
        if (entries[i] + entries[j] + entries[k] == 2020)
          return entries[i] * entries[j] * entries[k];
  return -1;
}

// This is the tail-recursive implementation of my original
// idea. Classic trick, use a function argument to serve as
// "accumulator" and track the running product.

int prob_one(const report& entries, size_t n, int target, int acc)
{
  size_t entries_len = entries.size();

  if (n == 0 || entries_len == 0)
    return -1; // not found since empty

  if (n == 1)
  {
    for (int i : entries)
      if (i == target) { return i * acc; }
    return -1; // only because all the inputs are positive
  }

  for (size_t i = 0; i < entries_len; ++i)
  {
    report subproblem; // one fewer entry

    //build sublist with item i omitted
    for (size_t j = 0; j < entries_len; ++j)
    {
      if (j != i)
      {
        subproblem.push_back(entries[j]);
      }
    }
    int subsol = prob_one(subproblem, n - 1, target - entries[i],
      entries[i] * acc);
    if (subsol != -1) { return subsol; }
  }

  return -1;
}
