try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Answer 1
# when input no the integor
# Answer 2
# When I enter a 0 into denominator
# Answer 3
# I think you want me to make the function continue instead of finishing it