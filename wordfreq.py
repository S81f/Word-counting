def tokenize(lines):
    """
    split lines of words into separate words and characters

    :param list of lines:
    :return list of separated words, characters and numbers:
    """
    words = []
    # print(len(lines)) # a line = set of words. The ex below is 2 lines
    # i.e. a line = 'you are 5 year older, than him', 'but that is ok'
    for line in lines:
        start = 0
        # print(len(line))
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
    """
    Counts the number of how often a word in the list words is repeated.
    If the word in words can be found in stopWords then the word is skipped.
    :param words:
    :param stopWords:
    :return: dictionary frequencies where the value is the word and the key is
    a number of how often the word is  repeated.
    """

    frequencies = {}
    if stopWords:
        for word1 in words:
            if word1 in stopWords:
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


def printTopMost(frequencies, n):
    """
    print n number of the most repeated words in dictionary frequencies
    :param frequencies:
    :param n:
    :return:
    """
    if len(frequencies) < n:
        # print('n cant be larger')
        pass
    else:
        sort_orders = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

        # f = lambda x: "".join(map(str, x))
        # print(" ".join(f(x) for x in sort_orders))

        for i in range(n):
            print(str(sort_orders[i][0]).ljust(20) + str(sort_orders[i][1]).rjust(5))