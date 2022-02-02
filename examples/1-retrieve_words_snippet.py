from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []

for line in story:
    # line_words = line.split()  # returns bytes over the web
    line_words = line.decode('utf8').split()    # converts to string
    for word in line_words:
        story_words.append(word)

story.close()
print(story_words)
