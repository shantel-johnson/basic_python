try:
    score=float(input("Enter score: "))
except:
    score=-1
if score > 1.0:
    print("Error: score is out of range, enter numeric value between 0.0 and 1.0")
elif score >= 0.9:
    print("Grade: A")
elif score >= 0.8:
    print("Grade: B")
elif score >= 0.7:
    print("Grade: C")
elif score >= 0.6:
    print("Grade: D")
elif score >= 0:
    print("Grade: F")
else:
    print("Error: score is out of range, enter numeric value between 0.0 and 1.0")
