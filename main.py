def main():
    print("--- Begin report of books/frankenstein.txt ---")

    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        wordCount = countWords(file_contents)

        print(f"{wordCount} words found in the document")
        print()

        charCount = countChar(file_contents)
        sortedCharCount = charCount.sort(reverse=True, key=sort_on)

        
        for char in charCount:
            print(f"The '{char['key']}' character was found {char['num']} times")

        f.close()

def countWords(content):
    wordList = content.split()
    return len(wordList)

def countChar(content):
    charList = list(content)
    charCount = []
    charCountDict = {}

    for c in charList:
        c = c.lower()

        if c.isalpha() == False:
            continue

        if c not in charCountDict:
            charCount.append({c: 1})
            charCountDict[c] = 1
            continue

        i = charCount.index({c: charCountDict[c]})
        charCount[i] = {c: charCountDict[c] + 1}
        charCountDict[c] += 1

    for i in range(0, len(charCount)):
        key = list(charCount[i].items())[0][0]
        count = list(charCount[i].items())[0][1]
        charCount[i] = {"key": key, "num": count}

    return charCount

def sort_on(dict):
    return dict["num"]

main()
