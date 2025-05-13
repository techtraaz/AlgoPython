# Recursive function
def sequence(n):
    if n == 1:
        return 1
    else:
        return sequence(n-1) + 2**(n-1)

# Initial input


# Loop until -1 is entered
while True:
    x = int(input("Enter number: "))
    if x == -1:
        break
    if x < 1:
        print("Output: Please enter a positive integer or -1 to exit.")
    else:
        print(f"Output: {sequence(x)}")
    

print("Output: Finished")
