import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database='ardit700_pm1database'
)


def translate(word):
    cursor = con.cursor()
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = %s", [str(word)])
    results = cursor.fetchall()
    if results:
        return results

    else:
        wrong_word = word
        if len(word) > 4:
            wrong_word = word[:3]
        query = cursor.execute("SELECT Expression FROM Dictionary WHERE Expression LIKE '%s%%'" % wrong_word)
        results = cursor.fetchall()
        match_list = []
        for i in results:
            match_list.append(i[0])
        if match_list:
            word_match = get_close_matches(word, match_list, n=1, cutoff=0.8)
            yn = input(f"Did you mean any {word_match[0]} instead? Yes or No? ")
            if yn.lower() == "yes" or yn.lower() == "y":
                query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word_match[0])
                return cursor.fetchall()
    return "Couldn't find the word. Please doble check it"


def main():
    word = input("Enter a word: ")
    answer = translate(word)
    if type(answer) == list:
        for i in answer:
            print(i[1])
    else:
        print(answer)


if __name__ == '__main__':
    main()
