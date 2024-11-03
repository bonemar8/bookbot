def main():
  book_path = "books/frankenstein.txt"
  text = get_text(book_path)
  print(text)


def get_text(path):
  with open(path) as file:
    return file.read()


main()