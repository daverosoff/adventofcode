import itertools
import collections

def dec_to_bin(n):
    remainders = []
    while n > 0:
        remainders.append(n % 2)
        n //= 2
    result = []
    while remainders:
        result.append(remainders.pop())
    return "".join(result) 

def bin_to_dec(n):
    return sum([2 ** i * int(bit) for i, bit in enumerate(reversed(n))])

def hex_to_bin(hex_bytes):
    convert = {
        '0': "0000",
        '1': "0001",
        '2': "0010",
        '3': "0011",
        '4': "0100",
        '5': "0101",
        '6': "0110",
        '7': "0111",
        '8': "1000",
        '9': "1001",
        'A': "1010",
        'B': "1011",
        'C': "1100",
        'D': "1101",
        'E': "1110",
        'F': "1111",
    }
    return "".join([convert[b] for b in hex_bytes])


class Parser:
    def __init__(self, st):
        self.raw = st
        self.read = 0
        self.packets = []
        self.version_sum = 0

    def get_next_packet(self):
        if not self.read < len(self.raw):
            pass
        version = bin_to_dec(self.raw[self.read:3 + self.read])
        type_id = bin_to_dec(self.raw[3 + self.read:6 + self.read])
        self.read = 6 + self.read

        if type_id == 4:
            start_pos = self.read - 6
            end = next(itertools.dropwhile(
                lambda pos: self.raw[pos] == 1,
                range(self.read, len(self.raw), 5)
            ))
            raw_value = self.raw[self.read:end + 5]
            self.read = end + 5
            literal_value = raw_value[:]
            nybbles = [literal_value[5*i+1 : 5*i+5] for i in
                range(len(literal_value) // 5)]
            value = bin_to_dec("".join(nybbles))
            new_packet = LiteralPacket(version, value)
            self.packets.append(new_packet)
            self.version_sum += version
            while (self.read - start_pos) % 16 != 0:
                self.read += 1
            return new_packet
        else:
            if not self.read < len(self.raw):
                raise IndexError(f"whut {self.read}")
            length_type_id = bin_to_dec(self.raw[self.read])
            self.read += 1
            self.version_sum += version
            if length_type_id == 0:
                bit_length = bin_to_dec(self.raw[self.read:self.read + 15])
                self.read += 15
                subpackets_pos = self.read
                subpackets = collections.deque()
                while self.read < subpackets_pos + bit_length:
                    subpackets.appendleft(self.get_next_packet())
            elif length_type_id == 1:
                number_of_subpackets = bin_to_dec(self.raw[self.read:self.read + 11])
                self.read += 11
                subpackets = collections.deque()
                for _ in range(number_of_subpackets):
                    subpackets.appendleft(self.get_next_packet())
                while (self.read < len(self.raw)
                        and self.raw[self.read] == '0'):
                    self.read += 1
            else:
                raise NotImplementedError("expected length_type_id to be"
                                          f"0 or 1, not {length_type_id}")
            self.packets.append(OperatorPacket(version, type_id, length_type_id,
                                                subpackets))

class Packet:
    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id

class LiteralPacket(Packet):
    def __init__(self, version, val):
        super().__init__(version, 4)
        self.value = val

    def __str__(self):
        return f"Literal: {self.value}"

class OperatorPacket(Packet):
    def __init__(self, version, type_id, length_type_id, subpackets):
        super().__init__(version, type_id)
        self.length_type_id = length_type_id
        self.subpackets = subpackets

    def __str__(self):
        return (f"Operator: type {self.type_id} "
                f"{len(self.subpackets)} subpackets")

sample = '8A004A801A8002F478'
sample2 = '620080001611562C8802118E34'
sample3 = 'C0015000016115A2E0802F182340'
sample4 = 'A0016C880162017C3686B18A3D4780'

puzz15 = """C20D7900A012FB9DA43BA00B080310CE3643A0004362BC1B856E0144D234F43590698FF31D249F87B8BF1AD402389D29BA6ED6DCDEE59E6515880258E0040A7136712672454401A84CE65023D004E6A35E914BF744E4026BF006AA0008742985717440188AD0CE334D7700A4012D4D3AE002532F2349469100708010E8AD1020A10021B0623144A20042E18C5D88E6009CF42D972B004A633A6398CE9848039893F0650048D231EFE71E09CB4B4D4A00643E200816507A48D244A2659880C3F602E2080ADA700340099D0023AC400C30038C00C50025C00C6015AD004B95002C400A10038C00A30039C0086002B256294E0124FC47A0FC88ACE953802F2936C965D3005AC01792A2A4AC69C8C8CA49625B92B1D980553EE5287B3C9338D13C74402770803D06216C2A100760944D8200008545C8FB1EC80185945D9868913097CAB90010D382CA00E4739EDF7A2935FEB68802525D1794299199E100647253CE53A8017C9CF6B8573AB24008148804BB8100AA760088803F04E244480004323BC5C88F29C96318A2EA00829319856AD328C5394F599E7612789BC1DB000B90A480371993EA0090A4E35D45F24E35D45E8402E9D87FFE0D9C97ED2AF6C0D281F2CAF22F60014CC9F7B71098DFD025A3059200C8F801F094AB74D72FD870DE616A2E9802F800FACACA68B270A7F01F2B8A6FD6035004E054B1310064F28F1C00F9CFC775E87CF52ADC600AE003E32965D98A52969AF48F9E0C0179C8FE25D40149CC46C4F2FB97BF5A62ECE6008D0066A200D4538D911C401A87304E0B4E321005033A77800AB4EC1227609508A5F188691E3047830053401600043E2044E8AE0008443F84F1CE6B3F133005300101924B924899D1C0804B3B61D9AB479387651209AA7F3BC4A77DA6C519B9F2D75100017E1AB803F257895CBE3E2F3FDE014ABC"""

p = Parser(hex_to_bin(sample4))
while p.read < len(p.raw):
    p.get_next_packet()

print(f"part one: {p.version_sum}")



