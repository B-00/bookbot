from stats import split_words, char_count
import sys

def get_book_text(path_to_file: str):
  file_contents = ''
  with open(path_to_file) as f:
    file_contents = f.read()
  return file_contents

def clean_print(sorted_dic):
  for key, val in sorted_dic:
    if key.isalpha():
      print(f"{key}: {val}")

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  text = get_book_text(f"./{sys.argv[1]}")
  print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
  print(f"Found {split_words(text)} total words")
  print("--------- Character Count -------")
  sorted_dic = sorted(char_count(text).items(), key=lambda item: item[1], reverse=True)
  clean_print(sorted_dic)
  print("============= END ===============")

main()