import time

def brute_force(password):
    length = len(password)
    max_attempts = 10**length

    print(f" Starting brute force attack on {length}-digit password. ")

    start_time = time.time()


    for i in range(max_attempts):
        guess = str(i).zfill(length)

        if guess == password:
            end_time = time.time()
            print("Password cracked: ", guess)
            print("Total attempts: ", i+1)
            print("Time taken: ", (end_time - start_time), "seconds")
    print("Password not found.")

pwd= input("Enter numeric password(4, 6, 8 digit): ")

if pwd.isdigiit() and len(pwd) in [ 4, 6,8]:
    brute_force(pwd)

else:
    print("Invalid input")
