def count_words(filename):
    """ open and count the approximate number of words in a file """
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"sorry the file {filename} does not exist.")
        
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"the file {filename} has about {num_words} words")

filenames = ['the_prophet.txt','sherlock.txt','alice_in_wonderland.txt','moby_dick.txt','war_and_peace.txt']

for filename in filenames:
    count_words(filename)

