import re

class PartOne:
    def __init__(self, st):

        self.rules = {}
        self.our_ticket = None
        self.tickets = []
        self.invalid = []
        self.valid_tickets = []

        with open(st, 'r') as file:
            puzzle = [line[:-1] for line in file.readlines()]

        def handle_line(d, tix, st):
            if st:
                p = parse_line(st)
                if type(p) is tuple:
                    d[p[0]] = p[1]
                elif p and self.our_ticket:
                    tix.append(p)
                elif p:
                    self.our_ticket = p

        def parse_line(st):
            if not st or st == 'your ticket:' or st == 'nearby tickets:':
                return None
            if len(st.split(": ")) > 1:
                field, values = st.split(": ")
                return field, extract_ranges(values)
            else:
                return [int(val) for val in st.split(",")]
            return values

        def extract_ranges(vals_st):
            r1, r2 = vals_st.split(" or ")
            r1a, r1b = r1.split("-")
            r2a, r2b = r2.split("-")
            return range(int(r1a), int(r1b) + 1), range(int(r2a), int(r2b) + 1)

        for line in puzzle:
            handle_line(self.rules, self.tickets, line)

    def is_valid(self, field, val):
        return val in self.rules[field][0] or val in self.rules[field][1]

    def validate(self, ticket):
        for val in ticket:
            if all([not self.is_valid(field, val) for field in self.rules]):
                self.invalid.append(val)
                return False
        return True

    def get_possibilities(self):
        tix_transpose = list(map(list, zip(*self.valid_tickets)))
        possibilities = {}
        for i, column in enumerate(tix_transpose):
            for field in self.rules:
                if all([self.is_valid(field, val) for val in column]):
                    if field not in possibilities:
                        possibilities[field] = [i]
                    else:
                        possibilities[field].append(i)
        # fewer_values = lambda s, t: len(possibilities[s]) < len(possibilities[t])
        # return sorted(possibilities, key=fewer_values)
        return possibilities

    def eliminate_and_assign(self, possibilities):
        matches = {}
        while len(possibilities) > 0:
            # find field with single possibility
            for field in possibilities:
                if len(possibilities[field]) == 1:
                    matched_field = field
                    break
            matched_column = possibilities[field][0]
            matches[field] = matched_column
            del possibilities[field]
            for field in possibilities:
                possibilities[field].remove(matched_column)
        return matches

    def __call__(self, part):
        if part == 1:
            for ticket in self.tickets:
                if self.validate(ticket):
                    self.valid_tickets.append(ticket)
            return sum(self.invalid)
        if part == 2:
            pos = self.get_possibilities()
            matches = self.eliminate_and_assign(pos)
            departure_fields = [field for field in self.rules if field[:9] == "departure"]
            departure_columns = [matches[field] for field in departure_fields]
            our_values = [self.our_ticket[i] for i in departure_columns]
            acc = 1
            for val in our_values:
                acc *= val
            return acc

p = PartOne("puzzle")
print(p(1))
print(p(2))