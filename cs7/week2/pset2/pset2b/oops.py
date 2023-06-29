# Outputs number of TAs necessary for input students (1 TA per 15 students).

def main():
    studs = int(input("How many students are enrolled? "))
    print ("We need", studs // 15, "teaching assistants")

main()