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
print(text[0:30])

words = nltk.word_tokenize(text)
print(words[0:10])
if "The" != "the":
    print("Case matters!")

clean_words = clean_tokens(words)
print(clean_words[0:30])
word_counts = nltk.FreqDist(clean_words)
print(word_counts.most_common(10))
print(word_counts['she'])
nltk.Text(clean_words).dispersion_plot(['he', 'she', 'tony'])