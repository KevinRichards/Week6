word_diction = {}
text = input("TEXT: ")

for word in text.split():
    if word in word_diction:
        word_diction[word.lower()] += 1
    else:
        word_diction[word.lower()] = 1
sort_dictionary_word_length = sorted(word_diction,key=len)
longest_word_length = len(sort_dictionary_word_length[-1])
for key,value in sorted(word_diction.items()):
    print("{:>{}} : {}".format(key,int(longest_word_length),value))


