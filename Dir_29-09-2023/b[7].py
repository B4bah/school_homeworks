import itertools as itr

words = sorted([word for word in list(itr.product('gerasim', repeat=7)) if len(set(word)) == 7])

print(''.join(words[1899+1]))