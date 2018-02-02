s='nzsngknf'
word=s[0]
count=0
words=[]
for letter in s:
	count+=1
	if ord(letter)>=ord(word[-1]):
		word+=letter
	else:
		words.append(word[1:])
		word='1'+letter
	if count==len(s):
		words.append(word[1:]+s[-1])
b=[len(a) for a in words]
print(words[b.index(max(b))])
