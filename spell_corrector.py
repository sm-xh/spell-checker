import re
from collections import Counter
from nltk.corpus import brown

class SimpleSpellChecker:
    def __init__(self, corpus):
        self.WORDS = Counter(corpus)

    def P(self, word):
        "Probability of `word`."
        N = sum(self.WORDS.values())
        return self.WORDS[word] / N

    def correction(self, word):
        "Most probable spelling corrections for word."
        return sorted(self.candidates(word), key=self.P, reverse=True)[:3]

    def candidates(self, word):
        "Generate possible spelling corrections for word."
        return (self.known([word]) or self.known(self.edits1(word)) or self.known(self.edits2(word)) or [word])

    def known(self, words):
        "The subset of `words` that appear in the dictionary of WORDS."
        return set(w for w in words if w in self.WORDS)

    def edits1(self, word):
        "All edits that are one edit away from `word`."
        letters    = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż' if 'ą' in self.WORDS else 'abcdefghijklmnopqrstuvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(self, word):
        "All edits that are two edits away from `word`."
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))

def read_corpus(filename):
    with open(filename, 'r', encoding='utf8') as file:
        lines = file.read().split('\n')

    words = [line.split('\t')[1].lower() for line in lines if '\t' in line]
    return words

def main():
    print("Welcome to the interactive spell corrector!")
    print("Please enter the language you want to use (options: 'english' or 'polish'): ")

    lang = input().lower()
    if lang not in ['english', 'polish']:
        print("Sorry, the language you entered is not supported. Exiting...")
        exit(1)

    corpus = brown.words() if lang == 'english' else read_corpus('pl_pdb-ud-train.txt')

    spellchecker = SimpleSpellChecker(corpus)

    while True:
        print("\nPlease enter a word (or '/quit' to exit): ")
        word = input()

        if word == '/quit':
            break

        corrected_words = spellchecker.correction(word)
        if word not in corrected_words:
            print(f"Did you mean {corrected_words}?")
        else:
            print("No correction needed.")

if __name__ == "__main__":
    main()
