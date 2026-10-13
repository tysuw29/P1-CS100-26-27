# Quick Try 1
n = 1
count = 0
while n <= 1000:
    n = n * 2
    count += 1
print(count, n)


# # Infinite Loop
# Something inside the loop must change what the condition checks.
# n = 1
# while n < 5:
#     print(n)


# Quick Try 2 - Sentinel
total = 0
num = int(input("Number (0 to stop): "))

while num != 0:
    total += num
    num = int(input("Number (0 to stop): "))
    
print(f"Total:", total)