#
import os
# initialize lists
wordlist=[]
sentlist=[]
# select source file
txtfile = os.path.join(".","raw_data","paragraph_2.txt")
# get and clean data
with open(txtfile, 'r') as file:
    for line in file:
        line = line.rstrip()
        wordlist += line.split()
        sentlist += line.split(". ")
        while("" in sentlist) : 
            sentlist.remove("") 
# set values for avg calc later
    wordlistlen = len(wordlist)
    sentlistlen = len(sentlist)
    # Approximate letter count (per word)
    avgwordlen = round(sum(len(word) for word in wordlist) / wordlistlen,1)
    # Approximate word count per sentence
    sentlen = 0
    for i in range(0,len(sentlist)):
        templist = sentlist[i]
        sentlen = sentlen+len(templist.split())
    avgsentlen = round(sentlen/sentlistlen,1)
#Print Results
print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {len(wordlist)}")
print(f"Approximate Sentence Count: {len(sentlist)}")
print(f"Average Letter Count per word: {avgwordlen}")
print(f"Average Sentence Length: {avgsentlen}")
print("-----------------")