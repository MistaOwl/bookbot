import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
	with open (filepath, encoding="utf-8", errors="ignore") as f:
		return f.read()
	
def main():

	
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_path = sys.argv[1]

	text = get_book_text(book_path)

	final_count = count_words(text)
	print(f"Found {final_count} total words")
	

	char_count = count_characters(text)
	
	sorted_list =  sort_characters(char_count)
	for item in sorted_list:
		if item["char"].isalpha():
			print(f"{item['char']}: {item['num']}")
 
main()

