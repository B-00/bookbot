def split_words(text):
  return len(text.split())

def char_count(text):
  count_dic = {}

  for c in text:
    c = c.lower()
    if c in count_dic:
      count_dic[c] = count_dic[c] + 1
    else:
      count_dic[c] = 1
      
  return count_dic