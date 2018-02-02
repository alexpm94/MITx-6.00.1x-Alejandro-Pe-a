count=0
count2=0
word=''
s = 'azcbobobegghakl'
for letter in s:
	print(word)
	if count>0:
		word+=letter
	if word=='bob':
		count2+=1
	if letter=='b':
		word='b'
		count=1
print('Number of times bob occurs is: ',count2)

