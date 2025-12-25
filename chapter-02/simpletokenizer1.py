import re

class SimpleTokenizer1:

    regex = r'([,.:;?_!"()\']|--|\s)'

    def __init__(self,dictionary):
        self.tokensToValues = dictionary
        self.valuesToTokens = {v:t for t,v in dictionary.items()}

    def text2tokens(self, text):

        tokens = re.split(self.regex, text)
        return [token for token in tokens if token.strip()]

    def encode(self, text):

        tokens = self.text2tokens(text)

        tokens = [
            token if token in self.tokensToValues
            else "<|unknown|>"
            for token in tokens
        ]

        values = [self.tokensToValues[token] for token in tokens]

        return values

    def decode(self, values):

        text = [self.valuesToTokens[value] for value in values]
        text = " ".join(text)
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text