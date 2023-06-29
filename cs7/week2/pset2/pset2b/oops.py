# Calculates necessary number of teaching assistants for input number of students.

def main():
    studs = int(input("How many students are enrolled? "))
    print ("We need," studs % 15, 'teaching assistants')

main()