# counting number of words in a given text.

# str1 = input("Please enter your string: ")
# total =1

# for i in range(len(str1)):
#     if(str1[i]==' ' or str1=='\n' or str1=='\t'):
#         total=total+1

# print('The total number of words in the string you entered is: ', total)

# counting number of words in a file

# file = open("E:\Zuri Learning\Python\pyme.txt")
# data = file.read()
# words=data.split()

# print('The total number of words in the file is: ', len(words))

word_count = 0

file_name = "E:\Zuri Learning\Python\pyme.txt"

with open(file_name,'r') as file:
	for line in file:
		word_count += len(line.split())


print ("Number of words : ",word_count)

