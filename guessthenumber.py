import random  # You need to import the module

print('Welcome to the Guessing Game!')
print('Try to guess the number I chose between 1 and 100.')

n = random.randint(1, 100)  # Use random.randint, not random()
while True:
 num= int(input("Enter your guessed number: "))

 if num > n:
    print("❌ Guessed number is greater than the correct number.")
 elif num < n:
    print("❌ Guessed number is lesser than the correct number.")
 else:
    print("✅ Correct! You guessed the number.")
    break

