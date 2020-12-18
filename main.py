import json
data = json.load(open("data.json"))


def translate(word):
    if word in data:
        return data[word]
    return "Couldn't find the word. Please doble check it"


def main():
    word = input("Enter a word: ")
    print(translate(word.lower()))



if __name__ == '__main__':
    main()


