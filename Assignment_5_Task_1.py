dict_1 ={'Vaibhav':85,'Bhavana':95,'Pranay':92,'Amit':75}
input_name = input("Enter the student\'s name: ")

if input_name in dict_1:
    print(input_name +"\'s marks: ",dict_1[input_name])
else:
    print("Student not found")