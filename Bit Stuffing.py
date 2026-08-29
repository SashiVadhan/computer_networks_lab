'''
Write a program to implement the data link layer framing method such as bit stuffing
'''

def bit_stuffing(data):
    stuffed_data = ''
    count = 0
    for bit in data:
        if bit == '1':
            count += 1
            stuffed_data += bit
            if count == 5:
                stuffed_data += '0'
                count = 0
        else:
            stuffed_data += bit
            count = 0

    return stuffed_data


def bit_unstuffing(data):
    unstuffed_data = ''
    count = 0
    i = 0
    while i < len(data):
        bit = data[i]
        unstuffed_data += bit
        if bit == '1':
            count += 1
            if count == 5:
                i += 1
                count = 0
        else:
            count = 0
        i += 1

    return unstuffed_data


data = input("Enter data: ")
stuffed = bit_stuffing(data)
unstuffed = bit_unstuffing(stuffed)

print("Original Data:   ", data)
print("Stuffed Data:    ", stuffed)
print("Unstuffed Data:  ", unstuffed)