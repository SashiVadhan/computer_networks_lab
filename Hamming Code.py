'''
Write a program for Hamming Code generation for error detection and correction. 
'''

def calculate_parity_bits(data_bits):
    m = len(data_bits)
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    n = m + r
    hamming_code = ['x'] * (n + 1)  #hamming_code = [0] * (n + 1)  
    j = 0
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:
            hamming_code[i] = int(data_bits[j])
            j += 1
    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for k in range(1, n + 1):
            if k & parity_pos and k != parity_pos:
                if hamming_code[k] != 'x':
                    parity ^= hamming_code[k]
        hamming_code[parity_pos] = parity

    return hamming_code[1:]


def introduce_error(code, position):
    if 1 <= position <= len(code):
        code[position - 1] ^= 1
    return code


def detect_error(received_code):
    n = len(received_code)
    r = 0
    while (2 ** r) < (n + 1):
        r += 1
    error_position = 0
    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for k in range(1, n + 1):
            if k & parity_pos:
                parity ^= received_code[k - 1]
        if parity != 0:
            error_position += parity_pos

    return error_position


data = input("Enter data bits (e.g., 1011): ")
hamming = calculate_parity_bits(data)
print("Generated Hamming Code:", ''.join(map(str, hamming)))
error_pos = int(input("Enter position to introduce error (0 for none): "))

if error_pos != 0:
    hamming = introduce_error(hamming, error_pos)
    print("Hamming Code with error introduced:", ''.join(map(str, hamming)))

detected_pos = detect_error(hamming)

if detected_pos == 0:
    print("No error detected.")
else:
    print(f"Error detected at position: {detected_pos}")
