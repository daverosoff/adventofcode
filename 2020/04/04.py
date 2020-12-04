import time

with open("input", 'r') as f:
  lines = f.readlines()

validPassports = 0
passportsProcessed = 0
first = True
needed_keys = ["byr", "iyr", "hgt", "ecl", "hcl", "pid", "eyr"]

def validate_byr(byr_v):
  i = int(byr_v)
  return (i >= 1920) and (i <= 2002)

def validate_iyr(iyr_v):
  i = int(iyr_v)
  return (i >= 2010) and (i <= 2020)

def validate_eyr(eyr_v):
  i = int(eyr_v)
  return (i >= 2020) and (i <= 2030)

def validate_hgt(hgt_v):
  try:
    val = int(hgt_v[:-2])
  except ValueError:
    return False
  unit = hgt_v[-2:]
  if unit == "cm":
    return (val >= 150) and (val <= 193)
  elif unit == "in":
    return (val >= 59) and (val <= 76)
  else:
    return False

def validate_ecl(ecl_v):
  return ecl_v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validate_hcl(hcl_v):
  return ((len(hcl_v) == 7)
    and (hcl_v[0] == '#')
    and (all([hcl_v[i] in "0123456789abcdef"
      for i in range(1,7)])))

def validate_pid(pid_v):
  return ((len(pid_v) == 9)
    and all([ch in "0123456789" for ch in pid_v]))

validator_d = {
  'byr': validate_byr,
  'eyr': validate_eyr,
  'iyr': validate_iyr,
  'hgt': validate_hgt,
  'hcl': validate_hcl,
  'ecl': validate_ecl,
  'pid': validate_pid,
}

def is_valid(pp):
  if len(pp) < 7:
    return False
  if all([key in pp.keys() for key in needed_keys]):
    return all([validator_d[key](passport[key]) for key in needed_keys])
  return False

t0 = time.perf_counter()

for line in lines:
  if line != '\n':
    if first:
      passport = {}
      first = False
    line = line[:-1]
    kvpairs = line.split(' ')
    for kv in kvpairs:
      k, v = kv.split(':')
      passport[k] = v
  else:
    if (is_valid(passport)):
      validPassports += 1
    first = True
    passportsProcessed += 1

if (is_valid(passport)):
  validPassports += 1

t1 = time.perf_counter()
elapsed = t1 - t0

print(f"Part one: {validPassports} of {passportsProcessed} ({1000 * elapsed:0.3f} usec)")
