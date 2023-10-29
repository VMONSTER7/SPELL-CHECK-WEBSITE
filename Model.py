from textblob import TextBlob

class SpellCheckerModule:
    def correct_spell(self, text):
        words = text.split()
        corrected_words = []
        incorrect_words = []

        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)

            if corrected_word.lower() != word.lower():
                incorrect_words.append(word)

        corrected_words_count = len(incorrect_words)
        corrected_sentence = " ".join(corrected_words)

        return incorrect_words, corrected_words_count, corrected_sentence

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "mashine hello learnjng . i loke mashine learjing . appple"
    incorrect_words, corrected_words_count, corrected_sentence = obj.correct_spell(message)

    print("Incorrect Words:")
    print(incorrect_words)
    print("Corrected Words Count:", corrected_words_count)
    print("Corrected Sentence:")
    print(corrected_sentence)
