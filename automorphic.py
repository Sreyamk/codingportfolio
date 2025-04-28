def is_automorphic(num):
    square = num * num

    temp = num
    while temp > 0:
        if (square % 10) != (temp % 10):
            return False
        square = square // 10
        temp = temp // 10
    return True

# Input from user
n = int(input("Enter a number: "))

if is_automorphic(n):
    print(f"{n} is an Automorphic number ✅")
else:
    print(f"{n} is NOT an Automorphic number ❌")
