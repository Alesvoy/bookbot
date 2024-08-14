book_path = 'books/frankenstein.txt'

def count_chars(words):
  text = "".join(words)
  characters = list(text)
  dict = {}
  for char in characters:
    if char.isalpha() == False:
      continue
    if char in dict:
      dict[char] += 1
    else:
      dict[char] = 1
  return dict

def create_sorted_list(dict):
  dict_list = []
  for char in dict:
    dict_list.append({'name': char, "num": dict[char]})
  
  def sort_on(dict):
    return dict['num']
  
  dict_list.sort(reverse=True, key=sort_on)
  return dict_list

def print_report(total_words, char_count):
  print(f"--- Begin report of {book_path} ---")
  print(f"{total_words} words found in the document")
  print("\nCharacter count:")
  
  dict_list = create_sorted_list(char_count)
  for item in dict_list:
    print(f"The '{item['name']}' character was found {item['num']} times")
  print("--- End of report of ---")

with open(book_path) as f:
  file_contents = f.read()
  lower_case = file_contents.lower()
  words = lower_case.split()
  char_count = count_chars(words)
  print_report(len(words), char_count)