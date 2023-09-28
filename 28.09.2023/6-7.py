import itertools as itr

words = sorted(itr.product('aoy', repeat=5))

print(words[170+1])
print(words.index(('y', 'a', 'y', 'a', 'y'))+1)