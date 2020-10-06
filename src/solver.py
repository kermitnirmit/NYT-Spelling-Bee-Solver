from tqdm import tqdm
import read_words

def letters_match(word, golden, other_letters):
  all_letters = [golden] + other_letters
  for letter in word:
    if letter not in all_letters:
      return False
  return golden in word

def solve(golden, other_letters, words):
  ret = []
  for word in tqdm(words):
    if letters_match(word, golden, other_letters) and len(word) >= 4:
      ret.append(word)
  return ret
  # if current in words and current not in wordSet and len(current) >= 4 and golden in current:
  #   wordSet.add(current)
  #   return
  # while (len(current) < 15):
  #   all_letters = other_letters + [golden]
  #   for letter in all_letters:
  #     current = current + letter
  #     # print(current)
  #     solve(golden, other_letters, words, wordSet, current)
  #     current = current[:-1]
  #   return

if __name__ == "__main__":
    golden = ""
    while len(golden) != 1:
      golden = str(input("Enter the golden letter: "))
    letString = input("enter the remaining letters: ")
    other_letters = list(letString)
    # MORE ERROR HANDLING

    words = read_words.load_words()
    wordList = solve(golden, other_letters, words)
    wordList.sort(key = lambda x : len(x), reverse=True)
    print(wordList)



