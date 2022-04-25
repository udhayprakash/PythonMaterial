from threading import Thread

# Callable function forming the thread body for the Prime Number Producer


def get_prime_numbers():
    print("Prime number thread started")
    # 2 is a prime number
    print(2)
    for each_num in range(2, 20):
        is_prime = False
        for divisor in range(2, each_num):
            # Skip the Composite Number
            if each_num % divisor == 0:
                is_prime = False
                break
            else:
                # Mark the Prime Number
                is_prime = True
        # Print the Prime Number
        if is_prime == True:
            print(each_num)

    print("Prime number thread exiting")


print("Main thread started")
primes_thread = Thread(target=get_prime_numbers)

# Start the prime number thread
primes_thread.start()

# Let the Main thread wait for the prime thread to complete
primes_thread.join()

print("Main thread resumed")
print("Main thread exiting")
