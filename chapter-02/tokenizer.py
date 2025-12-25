import re
from simpletokenizer1 import SimpleTokenizer1

def run():

    with open("../resources/the-verdict-edith-wharton.txt", "r", encoding="utf-8") as textfile:
        raw = textfile.read()
        words = re.split(SimpleTokenizer1.regex, raw)
        # remove non alpha characters?
        # words = [word for word in words if re.search(r'[a-zA-Z]{1,}', word)]
        words = sorted(set(words))
        words.extend(["<|endoftext|>", "<|unknown|>"])
        # map sorted words to integer id
        dictionary = {word:index for index,word in enumerate(words)}

        # for (word,val) in dictionary.items():
        #    print(f"{word} -> {val}")

        print(len(words))

        simtok = SimpleTokenizer1(dictionary)

        text = """"It's the last he painted, you know,"
                   Mrs. Gisburn said with pardonable pride"""

        print(simtok.encode(text))

        values = simtok.encode("Hello how are you?")
        print(values)
        print(simtok.decode(values))




if __name__ == '__main__':
    run()

