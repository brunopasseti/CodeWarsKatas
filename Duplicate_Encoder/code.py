def duplicate_encode(word):
    word = word.upper()
    wordDict = {key: 0 for key in word}
    for index1, l1 in enumerate(word):
        for index2, l2 in enumerate(word):
            if l1 == l2:
                wordDict[l1] += 1

    result = []
    for l in word:
        if wordDict[l] > 1:
            result.append(')')
        else:
            result.append('(')
    return ''.join(result)
