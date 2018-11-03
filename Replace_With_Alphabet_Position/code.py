def alphabet_position(text):
    return " ".join([str(ord(l)-ord('a')+1)
                     for w in text.lower() for l in w if l.isalpha() == True])
