
def find_first_unique_char(guys: str):
    dictionary ={}
    for i in range(len(guys)):
        if guys[i] in dictionary:
            dictionary [guys[i]] += 1
        else:
            dictionary[guys[i]] = 1

    for i in range(len(guys)):
        if dictionary[guys[i]] == 1:
            return guys[i]

    return None