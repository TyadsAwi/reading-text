# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content (filename):
    a = open(filename, "r")
    return a.read()

def count_words():
    text = read_file_content("./story.txt")
    d = dict()
    a = open("./story.txt", "r")
    for line in a:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        for word in words:
                if word in d:
                        d[word] = d[word] + 1
                else:
                        d[word] = 1
    return d

