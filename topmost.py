from wordfreq import *
import sys
import urllib.request


def main():
    if len(sys.argv) == 4:
        try:
            stop_words_file = open(sys.argv[1], encoding="utf-8")
        except FileNotFoundError as e:
            print(e)
        else:
            stop_words = stop_words_file.readlines()
            stop_words_file.close()
            separated_stop_words = tokenize(stop_words)  # need to separate the words in eng_stopwords file

        if sys.argv[2].startswith('http://') or sys.argv[2].startswith('https://'):
            response = urllib.request.urlopen(sys.argv[2])
            words = response.read().decode('utf8').splitlines()
        else:
            try:
                words_file = open(sys.argv[2], encoding="utf-8")
            except FileNotFoundError as e:
                print(e)
            else:
                words = words_file.readlines()
                words_file.close()

        separated_words = tokenize(words)
        freq_words = countWords(separated_words, separated_stop_words)
        printTopMost(freq_words, int(sys.argv[3]))
    else:
        print("error, no enough sys.arv parameters!\n")


if __name__ == "__main__":
    main()
