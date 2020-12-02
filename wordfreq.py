"""************pesudo code**************
#
#  def tokensize(lines):
#       #processing lines
#       words[] #list to save words in
#       for line in lines:
#           start =0
#           while start < len(line):
#               print(line[star])
#               start = start+1
#
# """

def tokenize(lines):
    """
    split list or words into separate words and char

    :param list of lines:
    :return list of separated words, characters and numbers:
    """
    # processing lines
    words = []  # list to save words in
    # print(len(lines)) # a line = set of words. The ex below is 2 lines
    # i.e. a line = 'you are 5year older, than him', 'but that is ok'
    for line in lines:
        start = 0
        print(len(line))
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
