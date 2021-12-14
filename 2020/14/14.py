from collections import defaultdict

def get_puzzle(st):
    with open(st, 'r') as file:
        lines = file.readlines()
    return lines

# class
def parse(inst):
    if inst[:3] == 'mem':
        open_ = 3
        close = inst.find(']', 4)
        assert(close >= 0)
        location = int(inst[4:close])
        value = int(inst.split()[-1])
        return 'mem', location, value
    elif inst[:4] == 'mask':
        return 'mask', inst.split()[-1]
    else:
        raise NotImplementedError(f"Bad instruction: {inst}")

class Part1:
    def __init__(self, st):
        self.program = get_puzzle(st)
        # static analysis
        # need : max of all mem locations (for length of list)
        # max_mem = 0
        # mem_locs = []
        # for inst in self.program:
        #     ip = parse(inst)
        #     if ip[0] == 'mask':
        #         self.mask = list(ip[1])
        #     if ip[0] == 'mem':
        #         if ip[1] > max_mem:
        #             max_mem = ip[1]
        #         mem_locs.append(ip[1])
        # max_mem = max(mem_locs) + 1
        # for inst in self.program:
        #     ip = parse(inst)
        #     if ip[0] == 'mask':
        #         self.mask = list(ip[1])
        #     elif ip[0] == 'mem':
        #         locations = self.generate_locations(self.to_big_endian(ip[1]))
        #         newmax = max(locations)
        #         if newmax > max_mem:
        #             max_mem = newmax + 1
        self.memory = defaultdict(int)
        self.mask = list(parse(self.program[0])[1])

    def to_big_endian(self, value):
        value_stack = []
        while value > 0:
            value_stack.append(value % 2)
            value //= 2
        while len(value_stack) < 36:
            value_stack.append(0)
        value_lst = []
        while len(value_stack) > 0:
            value_lst.append(value_stack.pop())
        return value_lst

    def from_big_endian(self, bits):
        value = 0
        bits = bits[::-1]
        for i, ch in enumerate(bits):
            value += int(ch) * 2**i
        return value

    def apply_mask_one(self, bits):
        for i, ch in enumerate(self.mask):
            if ch != 'X':
                bits[i] = int(ch)
        return bits

    def generate_locations(self, location):
        # location has already been big-endianified
        template = []
        floating_positions = []
        # generate template with some 'X' bits
        for i, ch in enumerate(self.mask):
            if ch == '0':
                template.append(location[i])
            elif ch == '1':
                template.append(1)
            else:
                template.append('X')
                floating_positions.append(i)
        num_floats = len(floating_positions)
        bit_patterns = []
        for i in range(2 ** num_floats):
            bp = list(f"{i:b}")[::-1]
            while len(bp) < (num_floats):
               bp.append('0')
            bp = bp[::-1]
            bit_patterns.append(bp)
        addresses = []
        for bp in bit_patterns:
            address = template[:]
            for i, j in enumerate(floating_positions):
                address[j] = int(bp[i])
            addresses.append(self.from_big_endian(address))
        return addresses

    def apply_mask_two(self, main_loc_bits, bits):

        for i, ch in enumerate(self.mask):
            if ch == '0':
                if bits[i] != main_loc_bits[i]:
                    return False
            elif ch == '1':
                if bits[i] != 1:
                    return False
        return True

    def execute_part_one(self):
        for inst in self.program:
            ip = parse(inst)
            if ip[0] == 'mem':
                self.memory[ip[1]] = self.from_big_endian(self.apply_mask_one(self.to_big_endian(ip[2])))
            else:
                self.mask = list(ip[1])

    def answer_part_one(self):
        self.execute_part_one()
        return sum([int(val) for val in self.memory])

    def execute_part_two(self):
        for i, inst in enumerate(self.program):
            # print(f"Executing instruction {i} of {len(self.program)}")
            ip = parse(inst)
            if ip[0] == 'mem':
                locations = self.generate_locations(self.to_big_endian(ip[1]))
                for location in locations:
                    self.memory[location] = ip[2]
                    # print(f"... writing {ip[2]} to location {location} ...")
            else:
                self.mask = list(ip[1])
                # print(f"... changing mask to {ip[1]} ...")
            # print(f"Executed instruction {i} successfully.")

    def answer_part_two(self):
        self.execute_part_two()
        return sum([int(val) for val in self.memory.values()])

p = Part1("puzzle")
# x = p.generate_locations(p.to_big_endian(42))
# for y in x:
#     print(p.from_big_endian(y))
# print(p.answer_part_one())
print(p.answer_part_two())

