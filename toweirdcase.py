def toWeirdCase(string):
    string = list(string)
    for i in range(len(string)):
        if i// 2 == 0:
            string[i] = string[i].upper()
        else:
            string[i] = string[i].lower()

    return ''.join(string)
print(toWeirdCase('biscuit'))