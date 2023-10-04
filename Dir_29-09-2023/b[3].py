import itertools as itr

words = sorted(set([word for word in list(itr.product('kabala', repeat=6)) if not 'aa' in ''.join(word)]))

print(len(words))