# not a highly optimized solution..

def rot13(message):
    message = list(message)
    for i in range(len(message)):
        if 64 < ord(message[i]) < 91:
            if ord(message[i]) - 64 <= 13:
                message[i] = chr(ord(message[i]) + 13)
            else:
                message[i] = chr(ord(message[i]) - 13)
        elif 96 < ord(message[i]) < 123:
            if ord(message[i]) - 96 <= 13:
                message[i] = chr(ord(message[i]) + 13)
            else:
                message[i] = chr(ord(message[i]) - 13)

    return "".join(message)
