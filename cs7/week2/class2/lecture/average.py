# # Naive approach

# day1 = int(input("Price on Day 1: "))
# day2 = int(input("Price on Day 2: "))
# day3 = int(input("Price on Day 3: "))
# day4 = int(input("Price on Day 4: "))
# day5 = int(input("Price on Day 5: "))

# sum = day1 + day2 + day3+ day4 + day5
# avg = sum / N
# print(avg)
# or something


N = 4

# Initialize sum variable as float
sum = 0.0

for i in range(N):
    sum += float(input("Type the stock price on day #" + str(i + 1) + ": "))
avg = sum / N
