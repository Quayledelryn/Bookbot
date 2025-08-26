def get_num_words(text):
	words = text.split()
	return len(words)


def create_dictionary(text_to_dict):
	dictionary = {}
	for i in text_to_dict:
		low_i = i.lower()
		if low_i in dictionary:
			dictionary[low_i] +=1
 
		else:
			dictionary[low_i] = 1
	return dictionary



def titled_dictionary(dict_to_title):
	titled_dictionary = []
	for a in dict_to_title:
		if a.isalpha():
			b = dict_to_title[a]
			titled_entry = {"char":a, "num":b}
			titled_dictionary.append(titled_entry)
	titled_dictionary.sort(reverse=True, key=sort_on)
	return titled_dictionary

def sort_on(items):
	return items["num"]

