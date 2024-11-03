def main():
  book_path = "books/frankenstein.txt"
  text = get_text(book_path)
  words_count = count_words(text)
  character_occurences = count_chars(text)
  print(character_occurences)


def get_text(path):
  with open(path) as file:
    return file.read()


def count_words(text):
  words = text.split()
  return len(words)


def count_chars(text):
  char_occurences = {}
  for c in text:
    lowered = c.lower()
    if lowered in char_occurences:
      char_occurences[lowered] += 1
    else:
      char_occurences[lowered] = 1
  return char_occurences

  
main()