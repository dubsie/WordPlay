
# Written for Python 3
# Add a new comment

f=open('words.txt', encoding='utf-8')


def contains_this(word,subword):
	for letter in word: # Check each letter of the parsed word
		if subword in word:
			return True
	
def has_capital(word):
	for letter in word: # Check each letter of the parsed word
		if word.islower():
			return False
	return True
		
mylist=[]

for line in f: # This reads file line at a time
	word=f.readline()
	# Use this if you what to specify
	# if contains_this(word,"q"):
	
	if has_capital(word):
		mylist.append(word.strip())  # if true append to mylist


print (mylist)
print (len(mylist))





