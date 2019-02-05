
#a function that accepts a phrase param

def translate(phrase):

#variable that stores the result

    translation = ""

#a for loop throgh the latters

    for letter in phrase:

        if letter.lower() in "aeiou":



            if letter.isupper():
                
                translation = translation + "G"

            else:

                translation = translation + "g"

        else:

            translation = translation + letter

    return translation

print(translate(input("Enter a phrase: "))) 