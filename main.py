def main():
  book_path = "books/frankenstein.txt"
  text = get_text(book_path)
  words_count = count_words(text)
  character_occurences = count_chars(text) #This is a dict
  characters_list = turn_to_list(character_occurences)
  print_report(book_path, words_count, characters_list)


def get_text(path):
  with open(path) as file:
    return file.read()


def count_words(text):
  words = text.split()
  return len(words)


def count_chars(text):
  character_occurences = {}
  for c in text:
    lowered = c.lower()
    if lowered in character_occurences:
      character_occurences[lowered] += 1
    else:
      character_occurences[lowered] = 1
  return character_occurences


def print_report(book_path, words_count, characters_list):
  print(f"--- Begin report of {book_path} ---")
  print(f"{words_count} words found in the document \n")

  for character in characters_list:
    print(f"""The '{character["name"]}' character was found {character["num"]} times""")

  print("--- End report ---")


def turn_to_list(char_dict):
  characters_list = []
  for key in char_dict:
    if key.isalpha():
      characters_list.append({"name":key, "num":char_dict[key]})
  characters_list.sort(reverse=True ,key=lambda dict: dict["num"])
  return characters_list


main()