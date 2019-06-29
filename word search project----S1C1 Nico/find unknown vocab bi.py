# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:07:57 2019

@author: jiang
"""

import word_search, bi_sequential, simplification, time


bigger_vocab = load_words_from_file("Alice in Wonderland.txt")

bigger_vocab.sort()

bigger_vocab=simplify(bigger_vocab)


print("There are {0} words in the vocab, starting with\n {1} "
              .format(len(bigger_vocab), bigger_vocab[:10]))

vocab_list=load_words_from_file("vocabulary file.txt")
print("There are {0} words in the vocab, starting with\n {1} "
              .format(len(vocab_list), vocab_list[:10]))

missing_words=[]
t0=time.process_time()
for target in bigger_vocab:
    bi_search(vocab_list, target)
t1=time.process_time()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))