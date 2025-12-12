def print_report(file_path, words, counts):
    print("============ BOOKBOT ============")
    print("Analyzing book found at ",file_path,"...", sep="")
    print("----------- Word Count ----------")
    print("Found", words, "total words")
    print("----------- Character Count ----------")
    for key in counts.keys():
        print(key,": ",counts[key], sep="")

