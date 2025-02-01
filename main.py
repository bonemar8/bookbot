
def main():
  FRANK_BOOK_PATH = "books/frankenstein.txt"
  
  book_content = read_text(FRANK_BOOK_PATH)

  word_count = count_words(book_content)
  
  character_count_dict = count_characters(book_content)
  
  print_report(character_count_dict, word_count)


def read_text(path):
  try:
    with open(path, 'r') as text_object:
      text_content = text_object.read()
      return text_content
  except FileNotFoundError as ferr:
    print("file or directory given, does not exist")
    return ""


def count_words(text):
  words = text.split()
  return len(words)


def count_characters(text):
  character_dict = {}
  for c in text:
    lower_case = c.lower()
    if lower_case not in character_dict:
      character_dict[lower_case] = 1
    else:
      character_dict[lower_case] += 1
  return character_dict


def print_report(character_dict, word_count):
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{word_count} words found in the document\n")

  for character in dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True)):
    if character.isalpha():
      print(f"The '{character}' character was found {character_dict[character]} times")

  print("--- End report ---")

main()