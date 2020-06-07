"""
dataset preprocessor 
"""

import os

readDir = [r"valid.txt", r"test.txt", r"train.txt"]
writeWordsDir = [r"testa.words.txt", r"testb.words.txt", r"train.words.txt"]
writeTagsDir = [r"testa.tags.txt", r"testb.tags.txt", r"train.tags.txt"]


def write2File(dir, mode, content):
    with open(dir, mode=mode) as f:
        f.write(content)


for idx in range(len(readDir)):
    if os.path.exists(writeWordsDir[idx]):  # if the file exists
        os.remove(writeWordsDir[idx])  # then delete it
    if os.path.exists(writeTagsDir[idx]):  # if the file exists
        os.remove(writeTagsDir[idx])  # then delete it

    with open(readDir[idx]) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if i % 100 == 0: print(i)
            lineEnd = ''
            if len(lines[i].strip()) != 0:  # not blank line
                if '-DOCSTART-' in lines[i].split(' ')[0]: lineEnd = '\n'
                write2File(writeWordsDir[idx], 'a+', lineEnd + lines[i].strip('\n').strip().split(' ')[0] + ' ')
                write2File(writeTagsDir[idx], 'a+', lineEnd + lines[i].strip('\n').strip().split(' ')[-1] + ' ')
        print('write success')

