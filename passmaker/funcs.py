import random
import string

def create_pw_diff(arr):
    
    nums = string.digits
    syms = string.punctuation
    ucs = string.ascii_uppercase
    lcs = string.ascii_lowercase

    password = ''
    
    # No type chosen
    if ((len(arr) == 1)):
        return('Please select a type!')
    
    # one type chosen
    if ((len(arr) == 2) and ('uc' in arr)):
        for i in range(0, int(arr[-1])):
            a = random.choice(ucs)
            password += a
            
    if ((len(arr) == 2) and ('lc' in arr)):
        for i in range(0, int(arr[-1])):
            a = random.choice(lcs)
            password += a
    
    if ((len(arr) == 2) and ('num' in arr)):
        for i in range(0, int(arr[-1])):
            a = random.choice(nums)
            password += a
            
    if ((len(arr) == 2) and ('sym' in arr)):
        for i in range(0, int(arr[-1])):
            a = random.choice(syms)
            password += a
    
    # two types chosen
    if ((len(arr) == 3) and (('uc' in arr) and ('lc' in arr))):
        for i in range(0, int(arr[-1])):
            rand_list = [ucs, lcs]
            chosen_list  = random.choice(rand_list)
            a = random.choice(chosen_list)
            password += a
            
    if ((len(arr) == 3) and (('uc' in arr) and ('num' in arr))):
        for i in range(0, int(arr[-1])):
            rand_list = [ucs, nums]
            chosen_list  = random.choice(rand_list)
            a = random.choice(chosen_list)
            password += a
    
    if ((len(arr) == 3) and (('uc' in arr) and ('sym' in arr))):
        for i in range(0, int(arr[-1])):
            rand_list = [ucs, syms]
            chosen_list  = random.choice(rand_list)
            a = random.choice(chosen_list)
            password += a
            
    if ((len(arr) == 3) and (('lc' in arr) and ('num' in arr))):
        for i in range(0, int(arr[-1])):
            rand_list = [lcs, nums]
            chosen_list  = random.choice(rand_list)
            a = random.choice(chosen_list)
            password += a
    
    if ((len(arr) == 3) and (('lc' in arr) and ('sym' in arr))):
        for i in range(0, int(arr[-1])):
            rand_list = [lcs, syms]
            chosen_list  = random.choice(rand_list)
            a = random.choice(chosen_list)
            password += a
    
    if ((len(arr) == 3) and (('num' in arr) and ('sym' in arr))):
        for i in range(0, int(arr[-1])):
            rand_list = [nums, syms]
            chosen_list  = random.choice(rand_list)
            a = random.choice(chosen_list)
            password += a
            
    # three types chosen
    if ((len(arr) == 4) and (('num' in arr) and ('sym' in arr) and('lc' in arr))):
        for i in range(0, int(arr[-1])):
            rand_list = [nums, syms, lcs]
            chosen_list  = random.choice(rand_list)
            a = random.choice(chosen_list)
            password += a
            
    if ((len(arr) == 4) and (('num' in arr) and ('sym' in arr) and('uc' in arr))):
        for i in range(0, int(arr[-1])):
            rand_list = [nums, syms, ucs]
            chosen_list  = random.choice(rand_list)
            a = random.choice(chosen_list)
            password += a
            
    if ((len(arr) == 4) and (('num' in arr) and ('uc' in arr) and('lc' in arr))):
        for i in range(0, int(arr[-1])):
            rand_list = [nums, ucs, lcs]
            chosen_list  = random.choice(rand_list)
            a = random.choice(chosen_list)
            password += a
            
    if ((len(arr) == 4) and (('sym' in arr) and ('lc' in arr) and('uc' in arr))):
        for i in range(0, int(arr[-1])):
            rand_list = [syms, lcs, ucs]
            chosen_list  = random.choice(rand_list)
            a = random.choice(chosen_list)
            password += a
    
    # all types chosen
    if (len(arr) == 5):
        for i in range(0, int(arr[-1])):
            rand_list = [syms, lcs, ucs, nums]
            chosen_list  = random.choice(rand_list)
            a = random.choice(chosen_list)
            password += a
    
    return(password)

    
    


# nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# syms = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "{", "}", "[", "]", ":", "?"]
# ucs = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
#         "W", "X", "Y", "Z"]
# lcs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
#         "w", "x", "y", "z"]