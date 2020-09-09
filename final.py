def piglatin(str):
    words = []
    vowels = 'aeiouAEIOU'
    for word in str.split():
        if len(word) > 2 and word[0] not in vowels:
            words.append(word[1:]+'-'+word[0]+'ay')
        else:
            words.append(word+'-ay')
    return ' '.join(words)

string = input('Enter a word to translate to pig-latin: ')
print(piglatin(string))