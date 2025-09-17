import random

# Generate 10 random numbers between 1 and 100
for i in range(10):
    num = random.randint(1, 100)
    print(f"Random number {i+1}: {num}")

    # Check conditions with if
    if num % 2 == 0:
        print("  → It is even")
    else:
        print("  → It is odd")

    if num > 50:
        print("  → Greater than 50")
    else:
        print("  → Less than or equal to 50")
