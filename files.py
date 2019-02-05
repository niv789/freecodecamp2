
employee_file = open("employees.txt", "r")


for employee in employee_file.readlines():

    print(employee)

# print(employee_file.read()) #prints the whole document

print(employee_file.readline())

print(employee_file.readlines()[1])



employee_file.close()




workers = open("employees.txt", "w") #it overwrite the file/ can also be used to create a new file / html too

workers.write("\n kelly - customer service") 

workers.close()


workers = open("employees.txt", "a")#it appends to the file