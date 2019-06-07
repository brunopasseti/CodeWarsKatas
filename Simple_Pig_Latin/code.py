def pig_it(text):
    words=text.split()
    a = " ".join(word.replace(word[0], "", 1) + word[0] + "ay" if word.isalnum() else word for word in words)
    return a