#Import
import random

#Global Variable
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ASCII = [chr(i) for i in range (256)]
#Basic Function
def alpha_to_number(alpha) :
    return(alphabet.index(alpha))

def number_to_alpha(number) :
    return(alphabet[number])
	
def ASCII_to_number(no_ASCII) :
	return(ASCII.index(no_ASCII))

def number_to_ASCII(number) :
	return(ASCII[number])
	
def check_char_in_list(char,list):
	checker = False
	i = 0
	
	while (checker == False and i <= len(list)-1):
		if (char == list[i]) :
			checker = True
		else :
			i+=1
	return checker

def delete_elementlist_not_in_list (list,source) :
	newList = []
	for element in list :
		if check_char_in_list(element,source) :
			newList.append(element)
	
	return newList

def separate_by_5 (text) :
	list_of_text = list(text)
	new_text = []
	for i in range(len(text)) :
		new_text.append(text[i])
		if i%5 == 4 :
			new_text.append(" ")
	
	return "".join(new_text)

def index_element_not_in_list(list, source) :
	index_of_element = []
	for i in range(len(list)) :
		if not(check_char_in_list(list[i],source)) :
			index_of_element.append(i)
	
	return (index_of_element)
	
def original_separation(str_to_be_edit,str_original) :
	changed_list = list(str_to_be_edit)
	original_text = list(str_original)
	index_separator = index_element_not_in_list(original_text,alphabet)
	
	for index in index_separator :
		changed_list.insert(index, original_text[index])
	
	return ("".join(changed_list))
	
#Vigenere Cipher Standard
def vigenere_encrypt(plain_text,key):
    #Asumption : plain text in lowercase
    
    #Convert to list
	split_plain_text = delete_elementlist_not_in_list(list(plain_text),alphabet)
	split_key = delete_elementlist_not_in_list(list(key),alphabet)

    #Make variable for result
	cipher_text = []

    #Encrypt
	for i in range(len(split_plain_text)):
		number_of_char = (alpha_to_number(split_plain_text[i]) + alpha_to_number(split_key[i%len(key)])) % len(alphabet)
		cipher_text.append(number_to_alpha(number_of_char))

	return ("".join(cipher_text))

def vigenere_decrypt(cipher_text,key):
    #Asumption : cipher text in lowercase

    #Convert to List
	split_cipher_text = delete_elementlist_not_in_list(list(cipher_text),alphabet)
	split_key = delete_elementlist_not_in_list(list(key),alphabet)

    #Make variable for result
	plain_text = []

    #Decrypt
	for i in range(len(split_cipher_text)):
		number_of_char = (alpha_to_number(split_cipher_text[i]) - alpha_to_number(split_key[i%len(key)])) % len(alphabet)
		plain_text.append(number_to_alpha(number_of_char))

	return ("".join(plain_text))

#Full Vigenere Cipher
def random_table():
	random_table = []
	for i in range(len(alphabet)) :
		random_row = random.sample(range(len(alphabet)),len(alphabet))
		random_table.append(random_row)
		
	return random_table
	
def print_rand_rable(table):
	print('  ',end = '')
	for char in alphabet:
		print((char).upper() + '  ',end='')
	print('')
		
	for row in range(len(table)) :
		print(alphabet[row].upper() + ' ',end='')
		for column in range(len(table[row])) :
			if column == 0 :
				print(number_to_alpha(table[row][column]) + '|',end = '')
			else :
				print('|' + number_to_alpha(table[row][column]) + '|', end = '')
		print('')

def rand_table_to_str(table):
	txt = '  '
	for char in alphabet:
		txt = txt + (char).upper() + '  '
	txt = txt + "\n"
		
	for row in range(len(table)) :
		txt = txt + alphabet[row].upper() + ' '
		for column in range(len(table[row])) :
			if column == 0 :
				txt = txt + number_to_alpha(table[row][column]) + '|'
			else :
				txt = txt + '|' + number_to_alpha(table[row][column]) + '|'
		txt = txt + "\n"
	return txt

def full_vigenere_encrypt(plain_text,key,table):
	#Asumption : plain text in lowercase
    
	#Convert to list
	split_plain_text = delete_elementlist_not_in_list(list(plain_text),alphabet)
	split_key = list(key)
	
	#Make variable for result
	cipher_text = []

	#Encrypt
	for i in range(len(split_plain_text)) :
		number_of_char = table[alpha_to_number(split_key[i%len(key)])][alpha_to_number(split_plain_text[i])]
		cipher_text.append(number_to_alpha(number_of_char))

	return (''.join(cipher_text))

def full_vigenere_decrypt(cipher_text,key,table):
	#Asumption : cipher text in lowercase

    #Convert to List
	split_cipher_text = delete_elementlist_not_in_list(list(cipher_text),alphabet)
	split_key = list(key)

    #Make variable for result
	plain_text = []

    #Decrypt
	for i in range(len(split_cipher_text)):
		number_of_char = table[alpha_to_number(split_key[i%len(key)])].index(alpha_to_number(split_cipher_text[i]))
		plain_text.append(number_to_alpha(number_of_char))

	return ("".join(plain_text))

#Auto-Key Vigenere Cipher
def auto_key_vigenere_encrypt(plain_text,key):
	#Asumption : cipher text in lowercase
	
	#Convert to List and edit List
	split_plain_text = delete_elementlist_not_in_list(list(plain_text),alphabet)
	split_key = list(key) + split_plain_text
	
	#Make variable for result
	cipher_text = []
	
	#Encrypt
	for i in range(len(split_plain_text)):
		number_of_char = (alpha_to_number(split_plain_text[i]) + alpha_to_number(split_key[i%len(split_key)])) % len(alphabet)
		cipher_text.append(number_to_alpha(number_of_char))

	return ("".join(cipher_text))
	
def auto_key_vigenere_decrypt(cipher_text,key):

	#Asumption : plain text in lowercase
	
	#Convert to List and edit List
	split_cipher_text = delete_elementlist_not_in_list(list(cipher_text),alphabet)
	split_key = list(key)
	
	#Make variable for result
	plain_text = []
	
	#Encrypt
	for i in range(len(split_cipher_text)):
		number_of_char = (alpha_to_number(split_cipher_text[i]) - alpha_to_number(split_key[i%len(split_key)])) % len(alphabet)
		plain_text.append(number_to_alpha(number_of_char))
		split_key.append(number_to_alpha(number_of_char))

	return ("".join(plain_text))

#Running_Key Vigenere Cipher
def running_key_vigenere_encrypt(plain_text,key):
	return vigenere_encrypt(plain_text,key)

def running_key_vigenere_decrypt(cipher_text,key):
	return vigenere_decrypt(cipher_text,key)
	
#Extended Vigenere Cipher
def extended_vigenere_encrypt(plain_text,key):
    #Asumption : plain text in lowercase
    
    #Convert to list
	split_plain_text = list(plain_text)
	split_key = list(key)

    #Make variable for result
	cipher_text = []

    #Encrypt
	for i in range(len(split_plain_text)):
		number_of_char = (ASCII_to_number(split_plain_text[i]) + ASCII_to_number(split_key[i%len(key)])) % len(ASCII)
		cipher_text.append(number_to_ASCII(number_of_char))

	return ("".join(cipher_text))

def extended_vigenere_decrypt(cipher_text,key):
    #Asumption : cipher text in lowercase

    #Convert to List
	split_cipher_text = list(cipher_text)
	split_key = list(key)

    #Make variable for result
	plain_text = []

    #Decrypt
	for i in range(len(split_cipher_text)):
		number_of_char = (ASCII_to_number(split_cipher_text[i]) - ASCII_to_number(split_key[i%len(key)])) % len(ASCII)
		plain_text.append(number_to_ASCII(number_of_char))

	return ("".join(plain_text))
	
#Playfair Cipher
def random_playfair_table() :
	playfair_randomize_list = random.sample(range(len(alphabet)),len(alphabet))
	playfair_randomize_list.remove(9)
	
	playfair_table = []
	playfair_rows = []
	for i in range(len(playfair_randomize_list)):
		playfair_rows.append(playfair_randomize_list[i])
		
		if i%5 == 4 :
			playfair_table.append(playfair_rows)
			playfair_rows = []
			
	return playfair_table
	
def print_playfair_table(random_playfair_table) :
	for row in range(len(random_playfair_table)):
		for column in range(len(random_playfair_table[0])):
			print(number_to_alpha(random_playfair_table[row][column]) + "|",end="")
		print("")

def playfair_table_to_str(random_playfair_table) :
	txt = ''
	for row in range(len(random_playfair_table)):
		for column in range(len(random_playfair_table[0])):
			txt = txt + number_to_alpha(random_playfair_table[row][column]) + "|"
		txt = txt + "\n"
	return txt
		
def create_bigram(list_of_char) :
	change = True
	while change == True :
		change = False
		for i in range(len(list_of_char)):
			if i%2 == 0 and i != len(list_of_char)-1 : #huruf ganjil
				if(list_of_char[i] == list_of_char[i+1]):
					list_of_char.insert(i+1,"x")
					change = True
					
				if(list_of_char[i] == "j") :
					list_of_char[i] = "i"
	
	if len(list_of_char) % 2 == 1 :
		list_of_char.append("x")
		
	bigram_list = []
	bigram = []
	for i in range(len(list_of_char)):
		bigram.append(list_of_char[i])
		
		if(i%2 == 1) :
			bigram_list.append(bigram)
			bigram = []
	
	return bigram_list
	
def bigram_position_in_table(bigram, table):
	x1,y1,x2,y2 = 999,999,999,999
	for rows in range(len(table)) :
		for columns in range(len(table[rows])) :
			if(alpha_to_number(bigram[0]) == table[rows][columns]) :
				x1 = columns
				y1 = rows
			if(alpha_to_number(bigram[1]) == table[rows][columns]) :
				x2 = columns
				y2 = rows
	return x1,y1,x2,y2
	
def playfair_encrypt (plain_text,table_of_key) :
	#Convert to list
	list_of_bigram = create_bigram(delete_elementlist_not_in_list(plain_text,alphabet))
	cipher_of_bigram = []
	cipher_text = []
	
	for bigram in list_of_bigram :
		bigram_cipher = []
		x1,y1,x2,y2 = bigram_position_in_table(bigram, table_of_key)
		
		if (x1 == x2) : #baris sama
			bigram_cipher.append(number_to_alpha(table_of_key[x1][(y1+1)%5]))
			bigram_cipher.append(number_to_alpha(table_of_key[x2][(y2+1)%5]))
			cipher_of_bigram.append(bigram_cipher)
			bigram_cipher = []
		elif (y1 == y2) : #kolom sama
			bigram_cipher.append(number_to_alpha(table_of_key[(x1+1)%5][y1]))
			bigram_cipher.append(number_to_alpha(table_of_key[(x2+1)%5][y2]))
			cipher_of_bigram.append(bigram_cipher)
			bigram_cipher = []
		else : #baris dan kolom tidak sama
			bigram_cipher.append(number_to_alpha(table_of_key[x1][y2]))
			bigram_cipher.append(number_to_alpha(table_of_key[x2][y1]))
			cipher_of_bigram.append(bigram_cipher)
			bigram_cipher = []
			
	for bigram in cipher_of_bigram:
		for element in bigram :
			cipher_text.append(element)
			
	return ("".join(cipher_text))

def playfair_decrypt (cipher_text,table_of_key) :
	#Convert to list
	list_of_bigram = create_bigram(delete_elementlist_not_in_list(cipher_text,alphabet))
	plain_of_bigram = []

	for bigram in list_of_bigram :
		bigram_cipher = []
		x1,y1,x2,y2 = bigram_position_in_table(bigram, table_of_key)
		
		if (x1 == x2) : #baris sama
			bigram_cipher.append(number_to_alpha(table_of_key[x1][(y1-1)%5]))
			bigram_cipher.append(number_to_alpha(table_of_key[x2][(y2-1)%5]))
			plain_of_bigram.append(bigram_cipher)
			bigram_cipher = []
		elif (y1 == y2) : #kolom sama
			bigram_cipher.append(number_to_alpha(table_of_key[(x1-1)%5][y1]))
			bigram_cipher.append(number_to_alpha(table_of_key[(x2-1)%5][y2]))
			plain_of_bigram.append(bigram_cipher)
			bigram_cipher = []
		else : #baris dan kolom tidak sama
			bigram_cipher.append(number_to_alpha(table_of_key[x2][y1]))
			bigram_cipher.append(number_to_alpha(table_of_key[x1][y2]))
			plain_of_bigram.append(bigram_cipher)
			bigram_cipher = []
		
	plain_text = []
	for bigram in plain_of_bigram :
		plain_text.append(bigram[0])
		plain_text.append(bigram[1])
		
	alpha_without_x = alphabet
	alpha_without_x.remove("x")
		
	return "".join(delete_elementlist_not_in_list(plain_text,alpha_without_x))

#Super Enkripsi
def transposition_encrypt(plain_text,key):
	#Convert to list
	split_plain_text = list(delete_elementlist_not_in_list(plain_text,alphabet))
	
	matrix_of_plain_text = []
	array_of_plain_text = []
	
	for i in range(len(split_plain_text)):
		array_of_plain_text.append(split_plain_text[i])
		if i % key == key-1 or i == len(split_plain_text)-1 :
			matrix_of_plain_text.append(array_of_plain_text)
			array_of_plain_text = []
	
	while (len(matrix_of_plain_text[-1]) % key != 0) :
		matrix_of_plain_text[-1].append(' ')
	
	transpose_matrix = [list(transpose) for transpose in zip(*matrix_of_plain_text)]
	#print(transpose_matrix)
	
	cipher_text = []
	for j in range(len(transpose_matrix)):
		for k in range(len(transpose_matrix[j])):
			cipher_text.append(transpose_matrix[j][k])
	
	return ("".join(cipher_text))
	
def transposition_decrypt(cipher_text,key):
	#Convert to list
	split_cipher_text = list(cipher_text)
	
	matrix_of_cipher_text = []
	array_of_cipher_text = []
	
	for i in range(len(split_cipher_text)):
		array_of_cipher_text.append(split_cipher_text[i])
		if i % (((len(split_cipher_text)-1)//key)+1) == (len(split_cipher_text)-1)//key or i == len(split_cipher_text)-1 :
			matrix_of_cipher_text.append(array_of_cipher_text)
			array_of_cipher_text = []
		
	transpose_matrix = [list(transpose) for transpose in zip(*matrix_of_cipher_text)]
	
	plain_text = []
	for j in range(len(transpose_matrix)):
		for k in range(len(transpose_matrix[j])):
			plain_text.append(transpose_matrix[j][k])
	
	return ("".join(plain_text))
def super_encrypt(plain_text,key_vigenere,key_transposition):
	return (transposition_encrypt(vigenere_encrypt(plain_text,key_vigenere),key_transposition))
	
def super_decrypt(cipher_text,key_vigenere,key_transposition):
	return (vigenere_decrypt(transposition_decrypt(cipher_text,key_transposition),key_vigenere))

#Main
# def main() :
# 	print(alpha_to_number('a'))
# 	print(number_to_alpha(9))
    
# 	coba_split = list('coba')
# 	print("".join(coba_split))

# 	print(vigenere_encrypt("this plain text","sony"))
# 	print(vigenere_decrypt(vigenere_encrypt("this plain text","sony"),"sony"))

# 	print(number_to_alpha((alpha_to_number('l')-alpha_to_number('s')) % 26))

# 	test_table = random_table()
# 	print_rand_rable(test_table)
# 	print('')
# 	print(full_vigenere_encrypt("this plain text","sony",test_table))
# 	print(full_vigenere_decrypt(full_vigenere_encrypt("this plain text","sony",test_table),"sony",test_table))
	
# 	print(original_separation(auto_key_vigenere_decrypt(original_separation(auto_key_vigenere_encrypt("negara penghasil minyak","indo"),"negara penghasil minyak"),"indo"),"negara penghasil minyak"))
	
# 	print(running_key_vigenere_decrypt(running_key_vigenere_encrypt("indo","negara penghasil minyak"),"negara penghasil minyak"))
	
# 	print(extended_vigenere_encrypt("Apakah anda sudah makan wil?","William"))
# 	print(extended_vigenere_decrypt("Í×ÊÉ¸×ÐÍÔâ»ÊÔÖÂØ¸×ãÒÍ¬","William"))
	
# 	test2_table = random_playfair_table()
# 	print_playfair_table(test2_table)
# 	#print(index_element_not_in_list("temui ibu nanti malam",alphabet))
# 	#print(playfair_encrypt("temui ibu nanti malam",test2_table))
# 	#print(original_separation("abcdefghijkl","ai bv asd"))
# 	print(original_separation(playfair_encrypt("temui ibu nanti malam?",test2_table),"temui ibu nanti malam?"))
# 	print(original_separation(playfair_decrypt(original_separation(playfair_encrypt("temui ibu nanti malam",test2_table),"temui ibu nanti malam"),test2_table),"temui ibu nanti malam"))
	
# 	print(separate_by_5("a"))
	
# 	print(transposition_encrypt("departemen informatika",6))
# 	print(transposition_decrypt(transposition_encrypt("departemen informatika",3),3))
	
# 	print(super_decrypt(super_encrypt("lelaki tangguh","william",5),"william",5))
# main()
