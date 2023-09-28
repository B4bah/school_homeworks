import itertools as itr

words = sorted(itr.product('dkmo', repeat=5))

print(words.index(('k', 'o', 'm', 'o', 'd')) - words.index(('d', 'o', 'm', 'o', 'k')) + 2)