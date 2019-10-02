#! /usr/bin/env python

import re


class Word(object):
    """
    Representation of a word, the sentences to which it belongs, and the number
    of times the word occurs.
    """

    def __init__(self, word):
        self.word = word
        self.sentences = []
        self.count = 0

    def set_in_sentence(self, sentence_index):
        """
        Use this method to logically place a word in a sentence. It will
        increment a counter.
        """
        self.sentences.append(sentence_index + 1)
        self.count += 1
        return self

    def __str__(self):
        return self.word


class WordCounter(object):
    """
    Class to count the frequency of a words in a corpus of text as well
    as the sentence numbers in which they appear, outputted sorted by
    most frequently occurring.
    """

    def __init__(self, source_text):
        self.source_text = source_text

        self.sentences = [sentence for sentence in re.split('[\.!\?]+\s*', source_text)]

        self.words = dict()
        for sentence_index in range(len(self.sentences)):
            words = re.findall(r"\b([\w']+)\b", self.sentences[sentence_index])

            for word in words:
                word = word.lower()
                stored = self.words.get(word, None)
                if not stored:
                    stored = Word(word)
                    self.words[word] = stored
                stored.set_in_sentence(sentence_index)

    def print_result(self):
        """
        Will print ordered set of results to standard output.
        """

        ordered_words = sorted(
            self.words.items(),
            key=lambda o: (-o[1].count, o[0])
        )

        for word, o in ordered_words:
            print
            "%s, %s, %s" % (
                str(word),
                str(o.count),
                str(o.sentences),
            )


import sys


def main(argv=None):
    if argv == None:
        argv = sys.argv
    scriptname = argv[0]
    if len(argv) < 2:
        print
        "%s: takes at least one argument (source filename)." % scriptname
        return 2
    source_filename = argv[1]

    file_o = open(source_filename, 'r')
    filecontents = file_o.read()
    file_o.close()

    counter = WordCounter(filecontents)
    counter.print_result()

    return 0


if __name__ == "__main__":
    sys.exit(main())
