import re
from collections import Counter


def removeNonChars():
    with open("two_cities_ascii.txt", 'r+') as f:
        f = f.read()

        new_string = re.sub('[^a-zA-Z]+', ' ', f)

    return new_string.lower()


def main():

    array = removeNonChars().split()
    co = Counter(array)
    print("10 most common words: ", co.most_common(10))


    co = co.most_common(40)
    combinationsFor2Letters = []
    combinationsFor3Letters = []
    for word in co:
        word = word[0]
        if len(word) > 1:
            for word2 in co:
                word2 = word2[0]
                if len(word2) > 1:
                    if word[:2] == word2[:2] and word is not word2 and word not in combinationsFor2Letters and word2 not in combinationsFor2Letters:
                        combinationsFor2Letters.append([word, word2])
                    if word[:3] == word2[:3] and word is not word2 and word not in combinationsFor3Letters and word2 not in combinationsFor3Letters:
                        combinationsFor3Letters.append([word, word2])

    print("2 letters combinations: ", combinationsFor2Letters)
    print("3 letters combinations: ", combinationsFor3Letters)


if __name__ == "__main__":
    main()