marks = int(input("enter your marks"))
if marks < 35:
    print("grade 'f' fail")
elif marks >= 35 and marks <= 40:
    print("grade 'd'")
elif marks >= 42 and marks <= 50:
    print("grade 'c'")
elif marks >= 55 and marks <= 60:
    print("grade 'b'")
elif marks >= 65 and marks <= 70:
    print("grade 'a'")
else:
    print("grade'a+'")
