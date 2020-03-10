option = input("Do you want to convert english to morse (a) to morse to english (b)?\n")

def english_to_morse(word):
	new_morse = ""
	print ("\nMorse code:")
	for letter in word:
		if letter == "a":
			new_morse = new_morse + "._ "
			# print ("._ ")
		elif letter == "b":
			new_morse = new_morse + "_... "
			# print("_... ")
		elif letter == "c":
			new_morse = new_morse + "_._. "
			# print ("_._. ")
		elif letter == "d":
			new_morse = new_morse + "_.. "
			# print ("_.. ")
		elif letter == "e":
			new_morse = new_morse + ". "
			# print (". ")
		elif letter == "f":
			new_morse = new_morse + ".._. "
			# print (".._. ")
		elif letter == "g":
			new_morse = new_morse + "__. "
			# print ("__. ")
		elif letter == "h":
			new_morse = new_morse + ".... "
			# print (".... ")
		elif letter == "i":
			new_morse = new_morse + ".. "
			# print (".. ")
		elif letter == "j":
			new_morse = new_morse + ".___ "
			# print (".___ ")
		elif letter == "k":
			new_morse = new_morse + "_._ "
			# print ("_._ ")
		elif letter == "l":
			new_morse = new_morse + "._.. "
			# print ("._.. ")
		elif letter == "m":
			new_morse = new_morse + "__ "
			# print ("__ ")
		elif letter == "n":
			new_morse = new_morse + "_. "
			# print ("_. ")
		elif letter == "o":
			new_morse = new_morse + "___ "
			# print ("___ ")
		elif letter == "p":
			new_morse = new_morse + ".__. "
			# print (".__. ")
		elif letter == "q":
			new_morse = new_morse + "__._ "
			# print ("__._ ")
		elif letter == "r":
			new_morse = new_morse + "._. "
			# print ("._. ")
		elif letter == "s":
			new_morse = new_morse + "... "
			# print ("... ")
		elif letter == "t":
			new_morse = new_morse + "_ "
			# print ("_ ")
		elif letter == "u":
			new_morse = new_morse + ".._ "
			# print (".._ ")
		elif letter == "v":
			new_morse = new_morse + "..._ "
			# print ("..._ ")
		elif letter == "w":
			new_morse = new_morse + ".__ "
			# print (".__ ")
		elif letter == "x":
			new_morse = new_morse + "_.._ "
			# print ("_.._ ")
		elif letter == "y":
			new_morse = new_morse + "_.__ "
			# print ("_.__ ")
		elif letter == "z":
			new_morse = new_morse + "__.. "
			# print ("__.. ")
		else:
			print ("This only accepts letters right now")
			return

	return new_morse

def morse_to_english(english_word, morse_letter):
	if morse_letter == "._ ":
		english_word = english_word + "a"
		# print ("._ ")
	elif morse_letter == "_... ":
		english_word = english_word + "b"
		# print("_... ")
	elif morse_letter == "_._. ":
		english_word = english_word + "c"
		# print ("_._. ")
	elif morse_letter == "_.. ":
		english_word = english_word + "d"
		# print ("_.. ")
	elif morse_letter == ". ":
		english_word = english_word + "e"
		# print (". ")
	elif morse_letter == ".._. ":
		english_word = english_word + "f"
		# print (".._. ")
	elif morse_letter == "__. ":
		english_word = english_word + "g"
		# print ("__. ")
	elif morse_letter == ".... ":
		english_word = english_word + "h"
		# print (".... ")
	elif morse_letter == ".. ":
		english_word = english_word + "i"
		# print (".. ")
	elif morse_letter == ".___ ":
		english_word = english_word + "j"
		# print (".___ ")
	elif morse_letter == "_._ ":
		english_word = english_word + "k"
		# print ("_._ ")
	elif morse_letter == "._.. ":
		english_word = english_word + "l"
		# print ("._.. ")
	elif morse_letter == "__ ":
		english_word = english_word + "m"
		# print ("__ ")
	elif morse_letter == "_. ":
		english_word = english_word + "n"
		# print ("_. ")
	elif morse_letter == "___ ":
		english_word = english_word + "o"
		# print ("___ ")
	elif morse_letter == ".__. ":
		english_word = english_word + "p"
		# print (".__. ")
	elif morse_letter == "__._ ":
		english_word = english_word + "q"
		# print ("__._ ")
	elif morse_letter == "._. ":
		english_word = english_word + "r"
		# print ("._. ")
	elif morse_letter == "... ":
		english_word = english_word + "s"
		# print ("... ")
	elif morse_letter == "_ ":
		english_word = english_word + "t"
		# print ("_ ")
	elif morse_letter == ".._ ":
		english_word = english_word + "u"
		# print (".._ ")
	elif morse_letter == "..._ ":
		english_word = english_word + "v"
		# print ("..._ ")
	elif morse_letter == ".__ ":
		english_word = english_word + "w"
		# print (".__ ")
	elif morse_letter == "_.._ ":
		english_word = english_word + "x"
		# print ("_.._ ")
	elif morse_letter == "_.__ ":
		english_word = english_word + "y"
		# print ("_.__ ")
	elif morse_letter == "__.. ":
		english_word = english_word + "z"
		# print ("__.. ")
	else:
		print ("This only accepts letters right now")
		return

	return english_word

def get_morse_letters(morse):
	english_word = ""
	morse_letter = ""
	print("\nEnglish word: ")

	for character in morse:
		if character != " ":
			morse_letter = morse_letter + character
			# print (morse_letter)
		elif character == " ":
			morse_letter = morse_letter + character

			# print (morse_letter)

			# english_word = morse_to_english(english_word, morse_letter)

			if morse_letter == "._ ":
				english_word = english_word + "a"
				# print ("._ ")
			elif morse_letter == "_... ":
				english_word = english_word + "b"
				# print("_... ")
			elif morse_letter == "_._. ":
				english_word = english_word + "c"
				# print ("_._. ")
			elif morse_letter == "_.. ":
				english_word = english_word + "d"
				# print ("_.. ")
			elif morse_letter == ". ":
				english_word = english_word + "e"
				# print (". ")
			elif morse_letter == ".._. ":
				english_word = english_word + "f"
				# print (".._. ")
			elif morse_letter == "__. ":
				english_word = english_word + "g"
				# print ("__. ")
			elif morse_letter == ".... ":
				english_word = english_word + "h"
				# print (".... ")
			elif morse_letter == ".. ":
				english_word = english_word + "i"
				# print (".. ")
			elif morse_letter == ".___ ":
				english_word = english_word + "j"
				# print (".___ ")
			elif morse_letter == "_._ ":
				english_word = english_word + "k"
				# print ("_._ ")
			elif morse_letter == "._.. ":
				english_word = english_word + "l"
				# print ("._.. ")
			elif morse_letter == "__ ":
				english_word = english_word + "m"
				# print ("__ ")
			elif morse_letter == "_. ":
				english_word = english_word + "n"
				# print ("_. ")
			elif morse_letter == "___ ":
				english_word = english_word + "o"
				# print ("___ ")
			elif morse_letter == ".__. ":
				english_word = english_word + "p"
				# print (".__. ")
			elif morse_letter == "__._ ":
				english_word = english_word + "q"
				# print ("__._ ")
			elif morse_letter == "._. ":
				english_word = english_word + "r"
				# print ("._. ")
			elif morse_letter == "... ":
				english_word = english_word + "s"
				# print ("... ")
			elif morse_letter == "_ ":
				english_word = english_word + "t"
				# print ("_ ")
			elif morse_letter == ".._ ":
				english_word = english_word + "u"
				# print (".._ ")
			elif morse_letter == "..._ ":
				english_word = english_word + "v"
				# print ("..._ ")
			elif morse_letter == ".__ ":
				english_word = english_word + "w"
				# print (".__ ")
			elif morse_letter == "_.._ ":
				english_word = english_word + "x"
				# print ("_.._ ")
			elif morse_letter == "_.__ ":
				english_word = english_word + "y"
				# print ("_.__ ")
			elif morse_letter == "__.. ":
				english_word = english_word + "z"
				# print ("__.. ")
			else:
				print ("This only accepts letters right now")
				return

			morse_letter = ""

	return english_word


if option == "a":
	# Convert english word to morse code

	word = str.lower(input("What word would you like to convert to morse code?\n"))

	print (english_to_morse(word))

elif option == "b":
	# Convert morse word to english

	morse = str.lower(input("What morse code word would you like to convert to english? All letters must have a space after them. Use period (.) and underscore (_) characters.\n"))

	practice_morse = "_. ._ _ .... ._ _. "

	print(get_morse_letters(morse))