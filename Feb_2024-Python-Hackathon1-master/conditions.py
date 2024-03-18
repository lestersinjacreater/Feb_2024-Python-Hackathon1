# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



# Create a Python program that:


# - Prompts a user to enter their age.
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."

def check_voting_eligibility(age):
  """
  This function determines voting eligibility based on age, handling invalid and unrealistic inputs.
  """
  voting_age = 18
  max_age_limit = 130  # handle unrealisticly huge age numbers

  if age <= 0:
    return "Age cannot be negative. Please enter a valid age."
  elif age >= max_age_limit:
    return "That age seems a bit unrealistic. Please enter a valid age."
  elif age >= voting_age:
    return "You are eligible to vote. Make your voice heard!"
  else:
    return "Not yet eligible to vote. Keep being patriotic!"

# Get user input with error handling
while True:
  try:
    user_age = int(input("Enter your age: "))
    break  # Exit loop if input is valid
  except ValueError:
    print("Invalid input. Please enter a whole number for your age.")

# Call the function and print the result
print(check_voting_eligibility(user_age))
