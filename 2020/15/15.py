import collections
import itertools
import numpy as np
import time

sample1 = [0, 3, 6]
sample2 = [1, 3, 2]
puzzle = [6,19,0,5,7,13,1]

# class LimitedQueue(type(np.zeros(1000000, int))):
#     def __init__(self, max_size=1_000_000, items=None):
#         self.max_size = max_size
#         self.num_dropped = 0
#         self.num_done = 0
#         if items:
#             for i, it in enumerate(items):
#                 self.enqueue(it)

#     def enqueue(self, item):
#         if len(self) == self.max_size:
#             self.pop() # bye bye
#             self.num_dropped += 1
#             print(f"Dropped: value {self.num_done}")
#         self.insert(0, item)
#         self.num_done += 1
# dct = lambda:dict()
# class LimitedQueue(dct):
#     def __init__(self, items):
#         super().__init__(self)
#         self.num_done = 0
#         if items is not None:
#             for item in items:
#                 self.enqueue(item)
#         self.recent = items[-1]

    # def enqueue(self, item):
    #     if len(self[item]) >= 2:
    #         self[item].pop()
    #     self[item].insert(0, item)
    #     self.num_done += 1
    #     self.recent = item

def part_one(puzzle):
    lst = lambda:collections.deque()
    num_list = collections.defaultdict(lst)
    num_done = 0
    recent = puzzle[-1]
    for it in puzzle:
        # if len(num_list[it]) == 2:
        #     num_list[it].pop()
        num_done += 1
        num_list[it].appendleft(num_done)
    reps = 2020
    start = time.time()
    t = time.time()
    diff = None
    while num_done < reps:
        if num_done % 100_000 == 0:
            u = time.time()
            print(f"{100 * num_done / reps:0.2f}% done ({num_done}"
                    + f" of {reps}); {u - t:0.3f} seconds, {u - start:0.3f} seconds")
            t = time.time()
        num_done += 1
        if not num_list[recent][0]:
            recent = 0
            num_list[recent].appendleft(num_done)
        else: # len(num_list[recent]) >= 1:
            recent = num_done - num_list[recent][0]
            if len(num_list[recent]) == 2:
                num_list[recent].pop()
            num_list[recent].appendleft(num_done)
    # print(f"Dropped {num_list.num_dropped} values")
    return recent

# print(part_one(sample1))
# print(part_one(sample2))

# print(part_one(puzzle))

class PartOne:
    def __init__(self, starting):
        lst = lambda:collections.deque()
        self.num_list = collections.defaultdict(lst)
        self.num_done = 0
        self.recent = starting[-1]
        for it in starting:
            self.num_done += 1
            self.num_list[it].appendleft(self.num_done)

    def next_val(self):
        if self.recent in self.num_list.keys() and len(self.num_list[self.recent]) > 1:
                diff = self.num_list[self.recent][0] - self.num_list[self.recent][1]
                self.recent = diff
                self.num_done += 1
                if len(self.num_list[diff]) >= 2:
                    self.num_list[diff].pop()
                self.num_list[diff].appendleft(self.num_done)
        else:
            self.recent = 0
            self.num_done += 1
            self.num_list[0].appendleft(self.num_done)

p = PartOne(puzzle)
while p.num_done < 30_000_000:
    p.next_val()
print(p.recent)




