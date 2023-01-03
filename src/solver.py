from tqdm import tqdm
from collections import defaultdict
import read_words

def letters_match(word, golden, all_letters):
  for letter in word:
    if letter not in all_letters:
      return False
  return golden in word


def solve(golden, other_letters, words):
  return sorted(list(filter(lambda x: letters_match(x, golden, set([golden] + other_letters)) 
      and len(x) >= 4, tqdm(words))), 
      key = lambda x : len(set(x)), reverse=True,
  )


if __name__ == "__main__":
    golden = ""
    while len(golden) != 1:
      golden = str(input("Enter the golden letter: "))
    other_letters = []
    while len(set(other_letters)) != 6:
      letString = input("enter the remaining letters: ")
      other_letters = list(letString)
    words = read_words.load_words()
    wordList = solve(golden, other_letters, words)
    asdf = defaultdict(list)
    for word in wordList:
      asdf[len(word)].append(word)
    pangrams = [x for x in wordList if len(set(x)) == 7]
    
    print("pangrams: ", pangrams)

    for i in range(max(asdf.keys()),3,-1):
      print(i, "letter words: ", asdf[i])
