import os

wordlist=[]
sentlist=[]

# inputtext = input("Please enter the text you would like analyzed: ")
# sentlist = inputtext.split(".")
# print(sentlist)
# print(len(sentlist))


# with open("PyParaAnalyze.txt",'w+') as file:
#     file.write(inputtext)
# using pre-canned text
txtfile = os.path.join(".","raw_data","paragraph_2.txt")

with open(txtfile, 'r') as file:
    for line in file:
        wordlist += line.split()
        sentlist += line.split(".")
    print(sentlist)
    # Approximate letter count (per word)
    avgwordlen = sum(len(word) for word in wordlist) / len(wordlist)
    # Approximate word count per sentence
    sentlen = 0
    for i in range(0,len(sentlist)):
        templist = sentlist[i]
        sentlen = sentlen+len(templist.split())
    avgsentlen = sentlen/len(sentlist)

print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {len(wordlist)}")
print(f"Approximate Sentence Count: {len(sentlist)}")
print(f"Average Letter Count per word: {avgwordlen:.3}")
print(f"Average Sentence Length: {avgsentlen:.3}")
print("-----------------")