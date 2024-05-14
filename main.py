
def get_book(path, open_mode='r'):
    try:
        with open(path, open_mode) as f:
            return f.read()
    except FileNotFoundError:
        print("Book not found")
    except Exception as e:
        raise e

def get_words(open_book):
    words = open_book.split()
    return words

def count_letters(word_list):
    letters = {}

    for word in word_list:
        for letter in word.lower():
            if letter.isalpha():
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
    return dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))

def generate_stats(path):
    book = get_book(path)
    word_count = len(get_words(book))
    letter_counts = count_letters(get_words(book))

    print(f"--- {path} report ---")
    print(f"\nThe total word count is: {word_count}\n")
    print(f"\nThe total numbers of each character are:")
    for letter in letter_counts:
        print(f"{letter}: {letter_counts[letter]}")
    print("--- end of report ---")





def main():
    print("Enter the book path:")
    try:
        path = input()
        assert type(path) == str
    except KeykoardInterrupt:
        print("Canceled by user")
    except expression as identifier:
        raise identifier
    except:
        Print("Must input a string")
    else:
        generate_stats(path)

main()
