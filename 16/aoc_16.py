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

# NOTE: assume packet_data is given in binary form
def decode_packet(packet_data, level=0, debug=False):
    if packet_data == "":
        print(f"[{level}] - Found empty packet.")
        return (0, 0, 0)
    
    packet_version = int(packet_data[:3], 2)
    packet_type = int(packet_data[3:3 + 3], 2)

    if debug:
        print(f"[{level}] - Packet version: {packet_version}")
        print(f"[{level}] - Packet type: {packet_type}")

    if packet_type == 4:        
        literal_value = ""
        i = 6
        done = False
        while not done:
            continuation_bit = packet_data[i]
            literal_value += packet_data[i + 1: i + 5]
            i += 5

            if continuation_bit == '0':
                done = True

        literal_value = int(literal_value, 2)

        if debug:
            print(f"[{level}] - We have a literal value packet")
            print(f"[{level}] - literal_value = {literal_value}")
            
        return (i, packet_version, literal_value)
        
    else:
        sum_of_packet_versions = packet_version
        length_type_ID = int(packet_data[6], 2)
        sub_packets_values = []
        packet_value = 0
        total_bit_read = 0

        if debug:
            print(f"[{level}] - We have an operator packet")
            print(f"[{level}] - Length type ID: {length_type_ID}")

        # -- compute values recursively on all sub-packets
        if length_type_ID == 0:
            total_length_in_bits = int(packet_data[7: 7 + 15], 2)

            if debug:
                print(f"[{level}] - Total length in bits = {total_length_in_bits}")

            total_bit_read = 0
            while total_bit_read < total_length_in_bits:
                bit_read, sub_packet_version_sum, sub_packet_value = decode_packet(packet_data[22 + total_bit_read:], level + 1, debug=debug)
                total_bit_read += bit_read
                sum_of_packet_versions += sub_packet_version_sum
                sub_packets_values.append(sub_packet_value)
            total_bit_read = 22 + total_bit_read
            
        elif length_type_ID == 1:
            number_of_sub_packets = int(packet_data[7: 7 + 11], 2)

            if debug:
                print(f"[{level}] - Number of sub packets = {number_of_sub_packets}")

            number_of_sub_packets_read = 0
            total_bit_read = 0
            while number_of_sub_packets_read < number_of_sub_packets:
                bit_read, sub_packet_version_sum, sub_packet_value = decode_packet(packet_data[18 + total_bit_read:], level + 1, debug=debug)
                total_bit_read += bit_read
                sum_of_packet_versions += sub_packet_version_sum
                number_of_sub_packets_read += 1
                sub_packets_values.append(sub_packet_value)
            total_bit_read = 18 + total_bit_read

        else:
            print(f"[ERROR ({level})] - Unkown value for length type ID: {length_type_ID}!")
            return (0, 0, 0)

        # -- compute value of packet
        if packet_type == 0:
            # -- sum packets
            packet_value = sum(sub_packets_values)
        elif packet_type == 1:
            # -- product packets
            packet_value = 1
            for x in sub_packets_values:
                packet_value *= x
        elif packet_type == 2:
            # -- minimum packets
            packet_value = min(sub_packets_values)
        elif packet_type == 3:
            # -- maximum packets
            packet_value = max(sub_packets_values)
        elif packet_type == 5:
            # -- greater than packets
            packet_value = sub_packets_values[0] > sub_packets_values[1]
        elif packet_type == 6:
            # -- less than packets
            packet_value = sub_packets_values[0] < sub_packets_values[1]
        elif packet_type == 7:
            # -- equal to packets
            packet_value = sub_packets_values[0] == sub_packets_values[1]

        return (total_bit_read, sum_of_packet_versions, packet_value)

def part_one():
    with open("input.txt", "r") as f:
        packet_data = "".join([f"{(int(x, 16)):04b}" for x in f.read().strip()])
        _, version_number_sum, _ = decode_packet(packet_data)
        print(f"Solution to part one: {version_number_sum}")
        
# ------
    
def part_two():
    with open("input.txt", "r") as f:
        packet_data = "".join([f"{(int(x, 16)):04b}" for x in f.read().strip()])
        _, _, value = decode_packet(packet_data)
        print(f"Solution to part two: {value}")

# ------
    
if __name__ == "__main__":
    part_one()
    part_two()
