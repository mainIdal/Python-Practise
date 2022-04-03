from functools import reduce

def stem(word: str):
   return word.lower().rstrip(",.!:;'-\"").lstrip("'\"")
def read_file():
   with open("quote.txt", "r") as quote_f:
      quote = quote_f.read()
   return quote

def frequencies(List, word):
   frequency = 0
   
   def increase_frequency(word1,word2):
      nonlocal frequency
      #If both words are the same with the searching word, frequency will be increased by 2
      if word1 == word and word2 == word:
         frequency += 2
      #If one of them is the same with the searching word,  frequency will be increased by 1
      elif word1 == word or word2 == word:
         frequency += 1
         
      return frequency
   
   print(reduce(lambda word1,word2 : frequency if (word1 != word and word2 != word) else increase_frequency(word1,word2), List))
   
text = read_file()
my_list = list(map(stem, text.split(' ')))
print(my_list)
frequencies(my_list,"is")
