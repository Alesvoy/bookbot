path_to_file = "books/frankenstein.txt"

def count_words(text):
  words = text.split()
  i = 0
  for word in words:
    i += 1
  
  return i

def count_letters(text):
  chars = list(text)
  valid_chars = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y", "z")
  my_dict = {}
  
  for i in range(0, len(chars)):
    if(chars[i].lower() in valid_chars):
      if(chars[i].lower() in my_dict):
        my_dict[chars[i].lower()] += 1
      else:
        my_dict[chars[i].lower()] = 1
  
  return my_dict

def create_report(total_words, total_letters):
  report = f"--- Begin report of {path_to_file} ---\n"
  report += f"{total_words} words found in the document\n\n"
  
  for letter in total_letters:
    report += f"The '{letter}' character was found {total_letters[letter]} times\n"
    
  report += "--- End report ---"
  
  return report

with open(path_to_file) as f:
  file_contents = f.read()
  total_words = count_words(file_contents)
  total_letters = count_letters(file_contents)
  print(create_report(total_words, total_letters))