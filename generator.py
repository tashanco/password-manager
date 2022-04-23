import random
import array

def generate_password():

    # Maximum length of characters
    Max_Len = 16

    # Arrays to be used within password generation
    Digits = ['0', '1', '2', '3', '4', '5']
    
    Locase_Characters = ['t','a', 's', 'h', 'a', 'n']

    Upcase_Characters = ['B', 'E', 'D', 'E', 'A', 'U']

    Symbols = ['@', '£', '$', '%', '^', '&']

    # Combination of the characters above to form one array
    Combined_List = Digits + Locase_Characters + Upcase_Characters + Symbols

    # Selection of random character within each array set
    rand_digit = random.choice(Digits)
    rand_lower = random.choice(Locase_Characters)
    rand_upper = random.choice(Upcase_Characters)
    rand_symbol = random.choice(Symbols)

    # Combination of the above
    temp_pass = rand_digit + rand_lower + rand_upper + rand_symbol

    for x in range(Max_Len - 4):
        temp_pass = temp_pass + random.choice(Combined_List)

        # Convert password into and array and shuffle it
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x

    return(password)

if __name__ == "__main__":
        print(generate_password())