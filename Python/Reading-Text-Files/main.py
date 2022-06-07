# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    
    with open(filename) as file:
        text = file.read()
    
    return text


def count_words():
    text = read_file_content("./story.txt")
    
    #create an empty dictionary
    counts = dict()
    words = text.split()
    
    #Loop through each line of the text file
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
    
print(read_file_content("./story.txt"))
print(count_words())