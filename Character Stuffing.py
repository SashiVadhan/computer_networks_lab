'''
Write a program to implement the data link layer framing method such as character stuffing
'''

def char_stuffing(data, flag='F', esc='E'):
    stuffed_data = flag
    for char in data:
        if char == flag or char == esc:
            stuffed_data += esc
        stuffed_data += char
    stuffed_data += flag

    return stuffed_data


def char_unstuffing(data, flag='F', esc='E'):
    unstuffed_data = ''
    i = 1
    while i < len(data) - 1:
        if data[i] == esc:
            i += 1
        unstuffed_data += data[i]
        i += 1

    return unstuffed_data


data = input("Enter data: ")
stuffed = char_stuffing(data)
unstuffed = char_unstuffing(stuffed)

print("Original Data:   ", data)
print("Stuffed Data:    ", stuffed)
print("Unstuffed Data:  ", unstuffed)