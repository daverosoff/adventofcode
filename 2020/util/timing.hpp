// Timing utilities for AoC 2020.
// Dave Rosoff, 2020.
#ifndef DWR_TIMING_HPP
#define DWR_TIMING_HPP

#include <chrono>

namespace dwr
{
  using Clock = std::chrono::steady_clock;
  using Duration = std::chrono::duration<double, std::micro>;
  using Seconds = std::chrono::seconds;
}

#endif
