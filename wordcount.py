# put your code here.

import string

# def count_words(file_name):
#     with open(file_name) as test_file:
#         word_count = {}
#         for line in test_file:
#             line = line.rstrip()
#             for word in line.split(" "):
#                 word_count[word] = word_count.get(word,0) +1
#     for key, value in word_count.items():
#         print key, value

# count_words('test.txt')


def format_words(word):
    word = word.lower()
    while word[0] in string.punctuation:
        word = word[1:]
    while word[-1] in string.punctuation:
        word = word[:-1]
    print word
    return word


def count_words(file_name):
    with open(file_name) as test_file:
        word_count = {}
        for line in test_file:
            if not line.isspace():
                line = line.rstrip()
                for word in line.split(" "):
                    if len(word) != 0 and word.isalpha():
                        word = format_words(word)
                        word_count[word] = word_count.get(word, 0) + 1
    for key, value in word_count.iteritems():
        print key, value


count_words('twain.txt')

