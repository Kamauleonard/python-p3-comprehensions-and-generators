#!/usr/bin/env python3

def return_evens(num_list):
    return [n for n in num_list if n % 2 == 0]

def make_exclamation(sentence_list):
    return [word + '!' for word in sentence_list]

print(return_evens([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

result = make_exclamation(["hi,", "my", "name", "sound", "john"])
print(' '.join(result))
 