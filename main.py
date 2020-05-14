import time, os, keyboard
Dict = open("dict.txt", "r")
dictLines = Dict.readlines()
valid_words = []
used_words = []
while True:
    str = input("Enter the letters the word must contain: ")
    for i in dictLines:
        i.strip()
        if str in i.lower() and i not in used_words and i not in blacklisted:
            valid_words.append(i)
    valid_words = sorted(valid_words, key=len)
    word = valid_words[len(valid_words)-1]
    used_words.append(word)
    os.system("echo %s | clip" % word.strip())
    print(word)
    time.sleep(5/3)
    for i in word:
        keyboard.write(i)
        time.sleep(.05)
    valid_words.clear()
