from math import exp, log


def language_frequency(c):
    frequencies = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772,
                   0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978,
                   0.02360, 0.00150, 0.01974, 0.00074]
    i = ord(c)
    if 65 <= i <= 90:
        q = frequencies[(i - 65)]
    elif 97 <= i <= 122:
        q = frequencies[(i - 97)]
    else:
        q = exp(1)
    return q


def frequency(c, text):
    absolute_frequency = 0
    relative_frequency = 0
    cases = 0
    ascii_value = ord(c)
    if 65 <= ascii_value <= 90 or 97 <= ascii_value <= 122:
        for i in range(len(text)):
            if text[i] == c:
                absolute_frequency = absolute_frequency + 1
            cases = cases + 1
        relative_frequency = absolute_frequency / cases
    return relative_frequency


def crossentropy(text):
    s = 0
    for i in range(len(text)):
        c = text[i]
        p = frequency(c, text)
        q = language_frequency(c)
        s = s + (p * log(q))
    h = 0 - s
    return h


def main():
    alphabet_length = 26
    encrypted_string = input("Encrypted string:")
    string_length = len(encrypted_string)
    decrypted_strings = [[0 for x in range(string_length)] for y in range(alphabet_length)]
    entropies = [0 for x in range(alphabet_length)]

    s=""

    for j in range(string_length):
        ascii_value = ord(encrypted_string[j])
        for i in range(alphabet_length):
            if 65 <= ascii_value <= 90:
                new_ascii = ascii_value + i
                if new_ascii > 90:
                    new_ascii = new_ascii - 90 + 65 - 1
                decrypted_strings[i][j] = chr(new_ascii)
            elif 97 <= ascii_value <= 122:
                new_ascii = ascii_value + i
                if new_ascii > 122:
                    new_ascii = new_ascii - 122 + 97 - 1
                decrypted_strings[i][j] = chr(new_ascii)
            else:
                decrypted_strings[i][j] = chr(ascii_value)
    min_entropy = 0
    for k in range(alphabet_length):
        entropies[k] = crossentropy(decrypted_strings[k][:])
        if entropies[k] < entropies[min_entropy]:
            min_entropy = k

    print("\nPossible combinations (entropy):")
    for i in range(alphabet_length):
        for j in range(string_length):
            s = s + decrypted_strings[i][j]
        print(s + " ("+str(entropies[i])+")")
        s = ''
    print("\nDecrypted string:")
    print(''.join(decrypted_strings[min_entropy][:]))


if __name__ == "__main__":
    main()
