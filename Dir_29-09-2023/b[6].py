import itertools as itr

words = sorted([word for word in list(itr.product('пятьдней', repeat=4))])

for i in range(len(words)-1, 0, -1):
    if len(set(words[i])) == 4 and 'е' not in words[i] and 'я' not in words[i]:
        print(i+1)
        break