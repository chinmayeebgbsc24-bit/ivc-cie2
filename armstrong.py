n = int(input("Enter number: "))
order = len(str(n))
temp = n
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** order
    temp //= 10

if sum_val == n:
    print("Armstrong Number")
else:
    print("Not Armstrong")