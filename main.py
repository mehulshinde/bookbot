from stats import get_num_words, get_character_count
def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

def main():
    file_content = get_book_text('books/frankenstein.txt')
    num_words = get_num_words(file_content)
    print("Found" ,num_words, "total words")
    char_count = get_character_count(file_content)
    print(char_count)

main()

