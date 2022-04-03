from functools import reduce

def stem(word: str):
   return word.lower().rstrip(",.!:;'-\"").lstrip("'\"")
def read_file():
   with open("quote.txt", "r") as quote_f:
      quote = quote_f.read()
   return quote

def frequencies(List, word):
   print(reduce(lambda frequency, word_to_compare: frequency+1 if word == word_to_compare else frequency, List, 0))
   
text = read_file()
my_list = list(map(stem, text.split(' ')))
print(my_list)
frequencies(my_list,"is")
