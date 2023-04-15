# Program by Alexander Allis
# Answer to Assignment 4: Problem 1.e
from operator import xor

init_vector = [0, 1, 0, 1, 0]
ciphertext = [
    0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0,
    0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1,
    0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1,
    1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1
]
c_vector = [1, 0, 0, 1, 0]


def modulusTwo(a):
    a = a % 2
    while a < 0:
        a = a + 2
    return a


def getFeedback(stream):
    feedback = 0
    for i in range(len(stream)):
        temp = (stream[i] * c_vector[i])
        feedback = feedback + temp
    feedback = modulusTwo(feedback)
    return feedback


def getExclusiveOr(cText, stream):
    for i in range(len(cText)):
        cText[i] = int(xor(bool(cText[i]), bool(stream[i])))
    return cText


def convertIndexToChar(index):
    if index == 26:
        return ' '
    if index == 27:
        return '?'
    if index == 28:
        return '!'
    if index == 29:
        return '.'
    if index == 30:
        return '\''
    if index == 31:
        return '$'
    index = index + 65
    character = chr(index)
    return character


def main():
    stream = init_vector
    plaintext = []
    # for i in range(0, len(ciphertext), 5):
    #     cText = [ciphertext[i], ciphertext[i + 1], ciphertext[i + 2], ciphertext[i + 3], ciphertext[i + 4]]
    #     plaintext = getExclusiveOr(cText, stream)
    #     character = convertIndexToChar(int("".join(str(x) for x in plaintext), 2))
    #     print(str(character))
    #     # Feedback shift
    #     newElement = getFeedback(stream)
    #     stream.pop(0)  # remove first element from stream
    #     stream.append(newElement)

    for i in range(len(ciphertext)):
        cText = ciphertext[i]
        plaintext.append(int(xor(bool(cText), bool(stream[0]))))
        # Feedback shift
        newElement = getFeedback(stream)
        stream.pop(0)  # remove first element from stream
        stream.append(newElement)
    for i in range(0, len(plaintext), 5):
        letter = [plaintext[i], plaintext[i + 1], plaintext[i + 2], plaintext[i + 3], plaintext[i + 4]]
        print(str(convertIndexToChar(int("".join(str(x) for x in letter), 2))), end = "")


if __name__ == '__main__':
    main()
