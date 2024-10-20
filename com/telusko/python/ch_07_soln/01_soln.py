num = int(input("Enter a number for which you want to find the multiplication table: "))
for i in range(1, 11):
    # Using f-string for formatting: f"{variable} text {expression}" allows you to embed variables directly in the string
    print(f"{num} x {i} = {num * i}")
