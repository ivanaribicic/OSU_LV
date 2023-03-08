spam = 0
spam_words = 0
ham = 0 
ham_words = 0
exclamations = 0
fhand = open("SMSSpamCollection.txt")
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if line.startswith("spam"):
        spam += 1
        spam_words += len(words)
        if line[-1] == "!":
            exclamations += 1

    elif line.startswith ("ham"):
        ham += 1
        ham_words += len(words)

fhand.close()

print("Prosjek spam poruka: " + str(spam_words/spam))
print("Prosjek ham poruka: "+ str(ham_words/ham))
print("Broj spam poruka koje završavaju uskličnikom je: " + exclamations)