# inporting needed modules
import string
import getpass

# getting imput(password) from user
def check_pass():
    password = getpass.getpass("Enter the password: ")
    strength=0
    remarks=''
    lower_count =0
    upper_count = 0
    num_count =0
    wspace_count = 0
    special_count = 0

    #checking all the charecter in the password
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count+=1
        elif char in string.ascii_uppercase:
            upper_count+=1
        elif char in string.digits:
            num_count+=1
        elif char == " ":
            wspace_count+=1
        else:
            special_count+=1
           
    if lower_count>=1:
        strength+=1 
    if upper_count>=1:
        strength+=1
    if num_count>=1:
        strength+=1
    if wspace_count>=1:
        strength+=1
    if special_count>=1:
        strength+=1
        
    if strength == 1:
        remarks="Not a very strong password!!! please take a look"
    elif strength == 2:
        remarks="Not a good password"
    elif strength == 3:
        remarks="Not good enough"
    elif strength == 4:
        remarks="yes its good but can be better"
    elif strength == 5:
        remarks="good and very strong  password"
        
    print(f"{lower_count} lowercase charecters")
    print(f"{upper_count} uppercase charecters")
    print(f"{num_count} numeric charecters")
    print(f"{wspace_count} whitespace charecters")
    print(f"{special_count} special charecters")
    
    print(f"Pasword strength: {strength}")
    print(f"reason: {remarks}")

def ask_pwd(another_pwd=False):
    valid=False
    if another_pwd:
        choice=input("Do you want to enter another password (y/n):")
    else:
        choice=input("Do you want to check password (y/n): ")
    
    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == "n":
            return False
        else:
            print("Invalid , Try again")
# main function
if __name__ == '__main__':
    print("+++ welcome to pwd checker +++ ")
    ask_pw = ask_pwd()
    while check_pass():
        check_pass()
        ask_pw= ask_pwd(True)
        
        
            
        
      

    
