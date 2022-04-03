from functools import reduce

def stem(word: str):
   return word.lower().rstrip(",.!:;'-\"").lstrip("'\"")
def read_file():
   with open("quote.txt", "r") as quote_f:
      quote = quote_f.read()
   return quote

def frequencies(List, word):
   frequency = 0
   
   def cmpr_words(word1, word2):
      nonlocal frequency
      if word1 == word:
         frequency += 1
      if word2 == word:
         frequency += 1
      return frequency
   
   print(reduce(cmpr_words, List))
   
text = read_file()
my_list = list(map(stem, text.split(' ')))
print(my_list)
frequencies(my_list,"is")
