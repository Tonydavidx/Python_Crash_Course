def read_files(filenames):
    """ read files and give errors if found any """
    try:
        with open(filenames) as text_object:
            contents = text_object.read()
            print(contents)
    except FileNotFoundError:
        # print(f"the file {filenames} does not exist")
        pass

names = ['cats.txt','dogs.txt','sdds.txt']
for name in names:
    read_files(name)
