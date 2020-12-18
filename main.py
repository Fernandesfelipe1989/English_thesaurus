import json
data = json.load(open("data.json"))


def translate(word):
    return data[word]


def main():
    word = input("Enter a word: ")
    print(translate(word))



if __name__ == '__main__':
    main()


