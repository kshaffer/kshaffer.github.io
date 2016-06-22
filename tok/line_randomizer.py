import random
import os
import fnmatch

i = 0
line_of_poem = []
corpus = []
corpus_content = {}
corpus_poetry_by_line = {}

# import file names for all txt files in the folder
for file in os.listdir('./'):
    if fnmatch.fnmatch(file, '*.txt'):
        corpus.append(file)

# read in the text from each text file as a list of lines, with new line characters stripped
for poem in corpus:
    with open(poem, 'r') as f:
        temp_text = f.readlines()
        corpus_content[poem] = []
        for line in temp_text:
            corpus_content[poem].append(line.rstrip('\n'))

# create a dictionary in which each key is a line number (starting with zero, because Python
# and each value is a list of lines, one from each imported poem
while i < 77:
    single_line_content_all_poems = []
    for poem in corpus:
        single_line_content_all_poems.append(corpus_content[poem][i])
    corpus_poetry_by_line[i] = single_line_content_all_poems
    i += 1

# assemble a new poem that takes one random version of each line
assembled_poem = []
i = 0
while i < 77:
    assembled_poem.append(random.choice(corpus_poetry_by_line[i]))
    i += 1

# print the newly created poem
for line in assembled_poem:
    line_out = ''
    for char in line:
        if char == '|':
            line_out += '\n'
        else:
            line_out += char
    print(line_out)
