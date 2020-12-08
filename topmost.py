from wordfreq import *
import sys


def main():
    if len(sys.argv) == 4:
        stop_words_file = open(sys.argv[1], encoding="utf-8")
        stop_words = stop_words_file.readlines()
        stop_words_file.close()
        separated_stop_words = tokenize(stop_words)

        words_file = open(sys.argv[2], encoding="utf-8")
        words = words_file.readlines()
        words_file.close()

        separated_words = tokenize(words)
        freq_words = countWords(separated_words, separated_stop_words)
        printTopMost(freq_words, int(sys.argv[3]))
    else:
        print("error, no enough parameters! ")


if __name__ == "__main__":
    main()
