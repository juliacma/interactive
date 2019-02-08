# coding=utf-8

text = open("writing.txt", "r")

wordList = []

for line in text:
	for word in line.split():
		word=word.strip()
		wordList.append(word)

text.close()

finalText = open("writing-final.txt", "w")

for i in range(0, len(wordList)):
	finalText.write('<a href="#'+str(i+1)+'"><div id="'+str(i)+'">'+wordList[i]+'</div></a>\n')

finalText.close()
