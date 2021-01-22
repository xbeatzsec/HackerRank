n = int(input())


k = n % 2

if k != 0:
    print("Weird")

if k == 0 and 2 < n < 5:
    print("Not Weird")
if k == 0 and 6 < n <= 20:
    print("Weird")
if k == 0 and n > 20:
    print("Not Weird")
