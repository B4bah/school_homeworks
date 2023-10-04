import itertools as itr

words = list(reversed(sorted(itr.product('aoy', repeat=5))))

print(''.join(words[100+1]))