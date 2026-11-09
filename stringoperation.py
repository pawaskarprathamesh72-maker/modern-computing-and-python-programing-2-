


text=input("enter the string")

print("*"*10+"INDEXING AND SLICING"+"*"*10)

print("first character of the string is:",text[0])

print("last charater :",text[-1])

print("first 3 character :",text[0:3])

print("from index 3 onwards:",text[3:])

print("reverce of text:",text[::-1])

print("second character:",text[::2])

print("*"*10+"CASE CONVERSION"+"*"*10)

print("upper case:",text.upper())

print("lowes case:",text.lower())

print("swapcase:",text.swapcase())

print("*"*10+"COUNT OCCURRENCES"+"*"*10)

sub=input("enter a charater of substring:")

print("'"+sub+"'occurs",text.count(sub),"time(s)")

print("*"*10+"REPLACE A WORD"+"*"*10)

old=input("enter he word to replace:")

new=input("enter the new word:")

print("after replacing:",text.replace(old,new))

print("*"*10+"SPLIT AND JOIN"+"*"*10)

words=text.split()

print("after split:",words)

print("after join:","-".join(words))

print("*"*10+"STARTS WITH AND ENDS WITH"+"*"*10)

start=input("enter a start:")

end=input("enter a end:")

print("does the string start with '"+start+"':",text.startswith(start))

print("does the string end with '"+end+"':",text.endswith(end))