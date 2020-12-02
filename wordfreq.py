"""************pseudo code**************
#
#
# """


def tokenize(lines):
    """
    split list or words into separate words and characters

    :param list of lines:
    :return list of separated words, characters and numbers:
    """
    # processing lines
    words = []  # list to save words in
    # print(len(lines)) # a line = set of words. The ex below is 2 lines
    # i.e. a line = 'you are 5year older, than him', 'but that is ok'
    for line in lines:
        start = 0
        #print(len(line))
        while start < len(line):
            while line[start].isspace():
                start += 1
                if start == len(line):
                    break
            if start != len(line) and line[start].isalpha():
                # print(f'{line[start]} is a letter')
                end = start
                while line[end].isalpha():
                    end += 1
                    if end == len(line):
                        break
                words.append(line[start:end].lower())
                start = end

            elif start != len(line) and line[start].isdigit():
                # print(f'{line[start]} is a letter')
                end = start
                while line[end].isdigit():
                    end += 1
                    if end == len(line):
                        break
                words.append(line[start:end].lower())
                start = end

            elif start != len(line):
                # print(f'{line[start]} is a char')
                words.append(line[start])
                start += 1
                # start = end
            else:
                break
    return words


def countWords(words, stopWords):
    frequencies = {}
    if stopWords:
        for word1 in words:
            for word2 in stopWords:
                if word1 == word2:
                    pass
                elif word1 in frequencies:
                    frequencies[word1] = frequencies[word1] + 1
                else:
                    frequencies[word1] = 1
    else:
        for word in words:
            if word in frequencies:
                frequencies[word] = frequencies[word] + 1
            else:
                frequencies[word] = 1

    return frequencies


# hi = ["He he he in the room, she said."]
# du = tokenize(hi)
# han = [(["clean", "water"], [])]
countWords(["clean", "water"], [])
