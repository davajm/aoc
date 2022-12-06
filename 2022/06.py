def start_of_message(message, marker):
    for i in range(0, len(message)-marker+1):
        if len(set(message[i:i+marker])) == len(message[i:i+marker]):
            return len(message[i:i+marker])+i

with open('inputs/06') as f:
    data_stream = f.readline()

print(f'Part 1: {start_of_message(data_stream, 4)}')
print(f'Part 2: {start_of_message(data_stream, 14)}')
