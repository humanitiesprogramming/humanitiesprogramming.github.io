import nltk


def open_file_and_get_text(filename):
    with open(filename, 'r') as our_file:
        text = our_file.read()
    return text


def clean_tokens(raw_tokens):
    clean_words = []
    for word in words:
        clean_words.append(word.lower())
    return clean_words


# the actual stuff
filename="eyre.txt"
text = open_file_and_get_text(filename)

words = nltk.word_tokenize(text)
if "The" != "the":
    print("Case matters!")

clean_words = clean_tokens(words)
word_counts = nltk.FreqDist(clean_words)
print(word_counts['the'])

nltk.Text(clean_words).dispersion_plot(['he', 'she', 'Tony'])