sentece=input("enter the sentence  ")
sentece=sentece.lower()
word=sentece.split()
word_count={}
for words in word:
    if words in word_count:
        word_count[words] +=1
    else:
        word_count[words] =1
print("word in ",word_count)           


