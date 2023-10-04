import itertools as itr

words = sorted([word for word in list(itr.product('deikstra', repeat=5))
                if word.count('i') == 1 and word.index('i') != 4 and
                word[word.index('i')+1] in ('d', 'k', 's', 't', 'r')])

print(len(words))