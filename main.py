import sys
from stats import get_num_words, get_character_count
from report import print_report
def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    file_content = get_book_text(file_path)
    num_words = get_num_words(file_content)
    char_count = get_character_count(file_content)
    print_report(file_path, num_words, char_count)


main()

