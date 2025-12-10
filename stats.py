def get_num_words(file_content):
    words = file_content.split()
    return len(words)

def get_character_count(file_content):
    file_content = file_content.lower()
    char_counts = dict()
    for c in file_content:
        count = char_counts.get(c)
        if count:
            char_counts[c] = count + 1
        else:
            char_counts[c] = 1
    return char_counts


