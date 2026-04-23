##n = int(input("Enter a no: "))
##
##sum_of_divisor = 0
##
##for i in range(1, n):
##    if n%i==0:
##        sum_of_divisor += i
##
##if (sum_of_divisor == n and n>0):
##    print(f" {n} is perfect no. ")
##else:
##    print(f"{n} is not perfect no. ")



##n = int(input("Enter a Number: "))
##
##num_str = str(n)
##power = len(num_str)
##
##sum_of_power = 0
##
##for digit in num_str:
##    sum_of_power += int(digit)**power
##
##if sum_of_power == n:
##    print("Number is Armstrong. ")
##else:
##    print(f"{n} is not a Armstrong. ")


##n = int(input("Enter a number: "))
##
##if n<=1:
##    print("Not a Prime. ")
##else:
##    for i in range(2, n):
##        if(n%i==0):
##            print("Not a Prime. ")
##    else:
##        print("Prime no.")


##def gcd(a, b):
##    while b!=0:
##        a, b = b, a%b
##    return a
##
##x = int(input("Enter First no. "))
##y = int(input("Enter Second no. "))
##
##print(gcd(x,y))


##x= int(input("Enter first no. "))
##y= int(input("Enter second no. "))
##
##def gcd(a,b):
##    while b!=0:
##        a,b = b, a%b
##    return a
##
##if gcd(x
##       ,y)==1:
##    print(f"{x} and {y} are relatively prime. ")
##else:
##    print(f"{x} and {y} are not relatively prime. ")



##def narc(n):
##    start = 10**(n-1)
##    end = 10**n
##
##    result= []
##
##    for num in range(start, end):
##        num_str = str(num)
##        sum_of_power = 0
##
##        for digit in num_str:
##            sum_of_power += int(digit) ** n
##
##        if sum_of_power == num:
##            result.append(num)
##
##    return result
##
##n = int(input("Enter value of 'n': "))
##
##numbers = narc(n)
##
##if numbers:
##    print("Narcissistic number are: ", *numbers)
##else:
##    print("Narcissistic number not found.")


##def check_power_of_two(n):
##    if n>0 and (n&(n-1))==0:
##        k=0
##        temp =n
##        while temp>1:
##            temp //= 2
##            k+=1
##        return True,k
##    return False, none
##
##num = int(input("Enter a Number: "))
##
##result, k = check_power_of_two(num)
##
##if result:
##    print(f"{num} is in the form of 2^k (for k ={k})")
##else:
##    print(f"{num} is Not in the form of 2^k ")


##
##import re
##
##def check_password_strength(password):
##
##    score = 0
##
##    common_passwords = ["123456", "password", "12345678", "qwerty", "abc123" "admin"]
##
##    if password in common_passwords:
##        return "Very Weak (Common Password)"
##
##    if len(password) >= 8:
##        score +=1
##    if len(password) >= 12:
##        score +=1
##
##
##    if re.search(r"[A-Z]", password):
##        score +=1
##    if re.search(r"[a-z]", password):
##        score +=1
##    if re.search(r"[0-9]", password):
##        score +=1
##
##    if score <= 2:
##        return "Weak password"
##    elif score <=4:
##        return "Moderate password"
##    else:
##        return "Strong Password"
##
##pwd = input("Enter your Password: ")
##
##result = check_password_strength(pwd)
##
##print("Password Strength:", result)








##import time
##
##def brute_force(password):
##    length = len(password)
##    max_attempts = 10**length
##
##    print(f" Starting brute force attack on {length}-digit password. ")
##
##    start_time = time.time()
##
##
##    for i in range(max_attempts):
##        guess = str(i).zfill(length)
##
##        if guess == password:
##            end_time = time.time()
##            print("Password cracked: ", guess)
##            print("Total attempts: ", i+1)
##            print("Time taken: ", (end_time - start_time), "seconds")
##    print("Password not found.")
##
##pwd= input("Enter numeric password(4, 6, 8 digit): ")
##
##if pwd.isdigit() and len(pwd) in [ 4, 6,8]:
##    brute_force(pwd)
##
##else:
##    print("Invalid input")






























