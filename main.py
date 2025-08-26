from stats import get_num_words
from stats import create_dictionary
from stats import titled_dictionary



def main(book_path):
	c = get_book_text(book_path)
	n = get_num_words(c)
	d = create_dictionary(c)
	e = titled_dictionary(d)

	print ("============ BOOKBOT ============")
	print (f"Analyzing book found at {book_path}...")
	print ("----------- Word Count ----------")
	print (f"Found {n} total words")
	print ("--------- Character Count -------")
	for a in e:
		char= a["char"]
		num = a["num"]
		print (f"{char}: {num}")
	print ("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
        import sys
        if len(sys.argv) != 2:
                print ("Usage: python3 main.py <path_to_book>")
                sys.exit(1)
        book_path = sys.argv[1]
        main(book_path)




def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents


