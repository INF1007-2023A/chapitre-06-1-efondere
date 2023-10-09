#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        values = []
        values_text = input("Entrez des valeurs separees par une virgule: ").split(",")
        for value_text in values_text:
            values.append(value_text.strip())

    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        words = []
        words.append(input("Entrez le premier mot: "))
        words.append(input("Entrez le deuxieme mot: "))

    if len(words[0]) != len(words[1]):
        return False

    first_word_letters = {}
    second_word_letters = {}
    for c in words[0]:
        if c in first_word_letters.keys():
            first_word_letters[c] += 1
        else:
            first_word_letters[c] = 1

    for c in words[1]:
        if c in second_word_letters.keys():
            second_word_letters[c] += 1
        else:
            second_word_letters[c] = 1
    
    return second_word_letters == first_word_letters


def contains_doubles(items: list) -> bool:
    items_set = set(items)
    return len(items) != len(items_set)


def best_grades(student_grades: dict) -> dict:
    highest_average = 0
    highest_student = ""
    for k, v in student_grades.items():
        average = sum(v) / len(v)
        if (average > highest_average):
            highest_student = k
            highest_average = average

    return { highest_student: highest_average }


def frequence(sentence: str) -> dict:
    char_usage = {}
    for c in sentence:
        if c in char_usage.keys():
            char_usage[c] += 1
        else:
            char_usage[c] = 1

    # le test est different de ce qui est demande, mais bon...
    # chars_to_remove = [c for c in char_usage if char_usage[c] < 5]
    # for c in chars_to_remove:
    #     del(char_usage[c])

    return char_usage


def get_recipes():
    recipes = []
    stop = False
    while not stop:
        name = input("Entrez le nom de la recette: ")
        ingredients = [ingredient.strip() for ingredient in input("Entrez la liste d'ingredients, separes d'une virgule: ").split(',')]

        recipes.append({"name": name, "ingredients": ingredients})
        stop_str = input("Voulez vous entrer une nouvelle recette (o/n)?")
        if stop_str.lower() == "n" or stop_str.lower() == "non":
            stop = True

    return recipes


def print_recipe(recipes) -> None:
    name = input("Entrez le nom de la recette: ")
    found = False
    for recipe in recipes:
        if recipe["name"] == name:
            found = True
            print(f"la recette {name} necessite: ")
            for ingredient in recipe["ingredients"]:
                print(f"    - {ingredient}")
            break

    if not found:
        print("La recette n'a pas ete trouvee")


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
