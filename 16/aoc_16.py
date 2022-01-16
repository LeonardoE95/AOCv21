#!/usr/bin/env python3

# --- Day 16: Packet Decoder ---


# The transmission was sent using the Buoyancy Interchange
# Transmission System (BITS), a method of packing numeric expressions
# into a binary sequence. Your submarine's computer has saved the
# transmission in hexadecimal (your puzzle input).

# The first step of decoding the message is to convert the hexadecimal
# representation into binary.

# The BITS transmission contains a single packet at its outermost
# layer which itself contains many other packets.

# Every packet begins with a standard header: the first three bits
# encode the packet version, and the next three bits encode the packet
# type ID.

# Packets with type ID 4 represent a literal value. Literal value
# packets encode a single binary number.

# TODO: make sure the literal value are parsed correctly.

def decode_packet(packet_data, level=0):
    if packet_data == "":
        return (0, 0)
    
    packet_version = packet_data[:3]
    packet_type = packet_data[3:3 + 3]
    
    print(f"{level}[INFO] - Packet version: {int(packet_version, 2)}")
    print(f"{level}[INFO] - Packet type: {int(packet_type, 2)}")

    if int(packet_type, 2) == 4:
        print(f"{level}[INFO] - We have a literal value packet")
        literal_value = ""
        i = 6
        done = False
        while not done:
            continuation_bit = packet_data[i]
            literal_value += packet_data[i + 1: i + 5]
            i += 5

            if continuation_bit == '0':
                done = True

        print(f"{level}[INFO] - literal_value = {int(literal_value, 2)}")
        return (i, int(packet_version, 2)) # return number of bits read
        
    else:
        print(f"{level}[INFO] - We have an operator packet")
        length_type_ID = packet_data[6]
        print(f"{level}[INFO] - Length type ID: {length_type_ID}")

        if int(length_type_ID, 2) == 0:
            total_length_in_bits = packet_data[7: 7 + 15]
            print(f"{level}[INFO] - Total length in bits = {int(total_length_in_bits, 2)}")

            i = 0
            result = int(packet_version, 2)
            while i < int(total_length_in_bits, 2):
                bit_read, v_n = decode_packet(packet_data[22 + i:], level + 1)
                i += bit_read
                result += v_n

            return (22 + i, result)
            
        elif int(length_type_ID, 2) == 1:
            number_of_sub_packets = packet_data[7: 7 + 11]
            print(f"{level}[INFO] - Number of sub packets = {int(number_of_sub_packets, 2)}")

            n = 0
            i = 0
            result = int(packet_version, 2)
            while n < int(number_of_sub_packets, 2):
                bit_read, v_n = decode_packet(packet_data[18 + i:], level + 1)
                i += bit_read
                result += v_n
                n += 1

            return (18 + i, result)

        else:
            print(f"{level}[ERROR] - Unkown value for length type ID: {length_type_ID}!")

            return (0, 0)

def part_one():
    with open("tmp.txt", "r") as f:
        packet_data = "".join([f"{(int(x, 16)):04b}" for x in f.read().strip()])
        # 11101110000000001101010000001100100000100011000001100000
        # print(packet_data)
        print(decode_packet(packet_data))
        
# ------
    
def part_two():
    with open("input.txt", "r") as f:
        pass

# ------
    
if __name__ == "__main__":
    part_one()
    # part_two()
