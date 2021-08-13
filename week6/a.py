'''
6a. Write a program to sort words in a file and put them in another file. The output file should have only lower case words, so any upper case words from source must be lowered (handle exceptions)
'''

def copy_and_sort_file():
    try:
        with open('./week6/input.txt') as source_file, open('./week6/output.txt', 'w') as destination_file:
            list_of_words = []
            for line in source_file:
                for word in line.split():
                    list_of_words.append(word.lower())
            list_of_words.sort()

            for word in list_of_words:
                destination_file.write(word)
                destination_file.write(" ")
    except FileNotFoundError:
        print('The source file and/or destination file is not present')

copy_and_sort_file()