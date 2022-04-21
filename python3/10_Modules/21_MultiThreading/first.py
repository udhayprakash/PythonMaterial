from threading import Thread

# Callable function forming the thread body for the Prime Number Producer


def ProducePrimeNumbers():
    print("Prime number thread started")
    # 2 is a prime number
    print(2)
    for PrimeNumberCandidate in range(2, 20):
        IsPrime = False
        for divisor in range(2, PrimeNumberCandidate):
            # Skip the Composite Number
            if PrimeNumberCandidate % divisor == 0:
                IsPrime = False
                break
            else:
                # Mark the Prime Number
                IsPrime = True
        # Print the Prime Number
        if IsPrime == True:
            print(PrimeNumberCandidate)

    print("Prime number thread exiting")


print("Main thread started")
PrimeNumberThread = Thread(target=ProducePrimeNumbers)

# Start the prime number thread
PrimeNumberThread.start()

# Let the Main thread wait for the prime thread to complete
PrimeNumberThread.join()

print("Main thread resumed")
print("Main thread exiting")
