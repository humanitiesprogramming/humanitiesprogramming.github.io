# there is a package called nltk. load it for this file.
import nltk

class TonyClass:
    def __init__(self, filename):
        self.filename = filename
        self.text = self.open_file_and_get_text(self.filename)
        self.tokens = nltk.word_tokenize(self.text)
        self.clean_tokens = self.clean_tokens(self.tokens)
        self.word_counts = nltk.FreqDist(self.clean_tokens)

    def make_the_plot(self, clean_tokens):
        nltk.Text(clean_words).dispersion_plot(['he', 'she', 'jane', 'tony'])

    def open_file_and_get_text(self, filename):
        # given a filename, open it.
        with open(filename, 'r') as our_file:
            # takes the the file and reads the text. Stores it.
            text = our_file.read()
        return text

    def clean_tokens(self, words):
        # given some tokens, lowercase them all.
        # create an empty list called clean_words
        clean_words = []

        # loop over every word item in the words list
        for word in words:
            # make each word lowercase and append it to the new list.
            clean_words.append(word.lower())
        return clean_words

# To actually run this, go into your python interpreter from within the same folder as this script. Import our own script
# $ python3
# >>> import eyre
# >>> our_text = TonyClass(ourfile)
# then we can access all of the stuff we've wrapped up in this package like so:
# >>> our_text.clean_tokens
# >>> our_text.tokens
