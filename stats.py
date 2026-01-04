def count_words(text):
        words = text.split()
        num_words = len(words)

        return num_words

def count_characters(text):
	char_count = {}
	lower_case = text.lower()
	for char in lower_case:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return (char_count)

def sort_on(char_dict):
	return char_dict["num"]

def sort_characters(char_count):
	sorted_dicts = []

	for char, num in char_count.items():
		sorted_dicts.append({"char":char, "num": num})

	sorted_dicts.sort(reverse = True, key = sort_on)

	return (sorted_dicts)
