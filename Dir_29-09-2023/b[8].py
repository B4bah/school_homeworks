import itertools as itr

words = sorted(set([word for word in list(itr.product('ydaha', repeat=5)) if word[0] in ('a', 'y')]))

print(words.index(('y', 'd', 'a', 'h', 'a')) + 1)