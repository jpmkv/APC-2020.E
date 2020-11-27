from random import randrange

words = str(input("Digite as palavras: "))
words = words.split(" ")

word_first = words[randrange(0, len(words))]
cut_word = ["_" for c in word_first]

time = 1

while time < 7 and cut_word.count("_") != 0:
    letter = str(input("Digite uma letra: "))

    if letter in word_first:
        print("A palavra é: ", end=" ")

        for y in range(len(word_first)):
            if letter == word_first[y]:
                del cut_word[y]
                cut_word.insert(y, letter)
        print(" ".join(cut_word))

    else:
        print(f"-> Você errou pela {str(time)}a vez. Tente de novo!")
        time = time + 1

print()

if cut_word.count("_") == 0:
    print("Parabéns! Você acertou a palavra.")

else:
    print("Forca! Fim de jogo.")