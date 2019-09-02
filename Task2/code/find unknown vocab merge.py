# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 11:10:44 2019

@author: jiang
"""
import word_search, simplification, merge, time
import matplotlib.pyplot as plt


bigger_vocab = load_words_from_file("Alice in Wonderland.txt")

bigger_vocab.sort()

bigger_vocab=simplify(bigger_vocab)


print("There are {0} words in the vocab, starting with\n {1} "
              .format(len(bigger_vocab), bigger_vocab[:10]))

vocab_list=load_words_from_file("vocabulary file.txt")
print("There are {0} words in the vocab, starting with\n {1} "
              .format(len(vocab_list), vocab_list[:10]))
t0=time.process_time()
missing_words=Merge(vocab_list,bigger_vocab)
t1=time.process_time()
plt.figure(dpi=128, figsize=(10, 6))
plt.title("unknown words",size=24)
plt.xlabel("num of words tested",size=14)
plt.ylabel("num of unknown words",size=14)
plt.scatter(x, y, c=y, cmap='jet', edgecolor='none',s=1)
plt.show()
print("There are {0} unknown words, the percentage is {1}."\
      .format(len(missing_words), str(round(100/len(bigger_vocab)*len(missing_words),1))+'%'))
print("That took {0:.4f} seconds.".format(t1-t0))