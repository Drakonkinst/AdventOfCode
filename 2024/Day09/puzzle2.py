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
    files_to_compress = [] # (file_id, start_pos, length)
    for ch in line:
        value = int(ch)
        if is_file:
            files_to_compress.append((file_id, index, value))
            file_id += 1
        index += value
        is_file = not is_file

    # Begin the compression, starting with the highest file and moving each once
    # For optimization, keep track of the completely filled space
    compressed_files = []
    for file_id_to_move in range(len(files_to_compress) - 1, -1, -1):
        leading_space, leading_space_amount = update_compressed_files(get_last_pos(compressed_files), files_to_compress, compressed_files)
        file = find_file_with_id(file_id_to_move, files_to_compress)
        if not file:
            # File with this ID must be in the compressed block, which means we're done
            break
        insert_file(leading_space, leading_space_amount, files_to_compress, file)

    # Calculate checksum
    checksum = get_checksum(compressed_files + files_to_compress)
    print(checksum)

def find_file_with_id(file_id, files):
    for file in files:
        if file[0] == file_id:
            return file
    return None

def get_last_pos(compressed_files):
    if len(compressed_files):
        _, last_index, last_length = compressed_files[-1]
        return last_index + last_length
    return 0

def update_compressed_files(start_pos, files, compressed_files):
    for i in range(len(files)):
        _, index, length = files[i]
        if index + length <= start_pos:
            # File is definitely behind
            continue
        if index <= start_pos:
            # start_pos is within this file, move to end
            start_pos = index + length
        else:
            # File is definitely after. If we've reached here, we know we've found a free space
            # More importantly, we know how large the free space is
            break
    # start_pos is now the index of the first space
    # Move all files before that to compressed_files, so we don't have to look at them again
    compressed_files.extend(files[:i])
    del files[:i]
    leading_space = files[0][1] - start_pos
    return start_pos, leading_space

def insert_file(leading_space, leading_space_amount, files, file_to_move):
    file_id, index, length_needed = file_to_move
    placement_index = -1 # What index the file is in the file system
    file_pos = -1 # The position of the file in the files_to_move_list
    if length_needed <= leading_space_amount:
        # Already fits in the first one
        placement_index = leading_space
        file_pos = 0
    else:
        # Go through remaining files and see where there is space
        for file_pos in range(len(files) - 1):
            curr_file = files[file_pos]
            curr_file_id, curr_index, curr_length = curr_file
            if curr_file_id == file_id:
                placement_index = curr_index
                break
            next_file = files[file_pos + 1]
            _, next_index, _ = next_file
            space_between_files = next_index - (curr_index + curr_length)
            if space_between_files >= length_needed:
                placement_index = curr_index + curr_length
                file_pos += 1
                break
    # If nothing found, place it in its original position
    if placement_index < 0:
        placement_index = index
        file_pos = len(files)

    # Insert the new file in the correct spot in the array
    new_file = (file_id, placement_index, length_needed)
    files.remove(file_to_move)
    files.insert(file_pos, new_file)

def get_checksum(files):
    checksum = 0
    for file in files:
        file_id, index, length = file
        for i in range(index, index + length):
            checksum += i * file_id
    return checksum

if __name__ == "__main__":
    main()