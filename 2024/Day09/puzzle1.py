import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    # Read files
    line = lines[0]
    index = 0
    file_id = 0
    is_file = True
    files = deque() # (file_id, start_pos, length)
    for ch in line:
        value = int(ch)
        if is_file:
            files.append((file_id, index, value))
            file_id += 1
        index += value
        is_file = not is_file

    # Begin the compression
    checksum = 0
    pos = 0
    while len(files):
        first_file = files[0] # Peek the first file
        first_file_id, first_start_pos, first_length = first_file
        # print(pos, first_file, files)
        if pos < first_start_pos:
            last_file = files.pop()
            last_file_id, last_start_pos, last_length = last_file
            spaces_remaining = first_start_pos - pos
            if spaces_remaining >= last_length:
                # This will be enough to consume the entire last file
                for i in range(pos, pos + last_length):
                    checksum += i * last_file_id
                pos += last_length
            else:
                # This will not be enough to consume the entire last file
                for i in range(pos, first_start_pos):
                    checksum += i * last_file_id
                pos += spaces_remaining
                files.append((last_file_id, last_start_pos, last_length - spaces_remaining))
        else:
            # Remove the first file
            files.popleft()
            # Now we have arrived at the end, and can progress the current block
            for i in range(pos, pos + first_length):
                checksum += i * first_file_id
            pos += first_length
    print(checksum)

if __name__ == "__main__":
    main()