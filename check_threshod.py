with open("accuracy.txt", "r") as f:
    accuracy = float(f.read().strip())

print("Accuracy:", accuracy)

if accuracy < 0.85:
    print(" Failed")
    exit(1)
else:
    print(" Passed")