#Default values indicate that the function argument will 
#take that value if no argument value is passed during the function call. 
def student(firstname, lastname ='Mark', standard ='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Standard')
    
student('John')