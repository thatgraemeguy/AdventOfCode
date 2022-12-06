#!/usr/bin/env python3

with open('data/06.txt') as f:
    data = f.read().splitlines()[0]

#data = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

packet_markers = [data[a:a+4] for a in range(0, len(data)-3)]
message_markers = [data[a:a+14] for a in range(0, len(data)-13)]

packet_indices = [len(set(a)) for a in packet_markers]
message_indices = [len(set(a)) for a in message_markers]

print(f"Part 1: {packet_indices.index(4)+4}")
print(f"Part 2: {message_indices.index(14)+14}")
