import itertools as itr

words = [word for word in list(itr.product('magistr', repeat=5))
         if len(set(word)) == 5 and (word.count('a') ^ word.count('i'))]

print(len(words))