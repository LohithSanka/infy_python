from urllib.request import urlopen
import sys

def fetch_word(url_name):
    story_words=[]
    story=urlopen(url_name)
    for line in story:
        decoded_line=line.decode("utf-8").split()
        for word in decoded_line:
            story_words.append(word)
    return story_words
    story.close()

def print_items(items):
    for item in items:
         print(item)
        
def main(url_name):
    words=fetch_word(url_name)
    print_items(words)

if __name__ == "__main__":
    url_name=sys.argv[1]
    main(url_name)

