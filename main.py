import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        match_word = get_close_matches(word, data.keys(), n=1)
        answer = input(f"Couldn't find the word {word}, Did you mean {match_word[0]} instead? Yes or No? ").lower()
        if answer == "yes" or answer == "y":
            return data[match_word[0]]
    return "Couldn't find the word. Please doble check it"


def main():
    word = input("Enter a word: ")
    meaning = translate(word.lower())
    if type(meaning) == list:
        for i in meaning:
            print(i)
    else:
        print(meaning)


if __name__ == '__main__':
    main()
