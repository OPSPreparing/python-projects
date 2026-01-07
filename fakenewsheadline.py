import random
subjects = ["Shahrukh khan", 
            "Virat Kohli", "CAT", 
            "DOG", "DRIVER"]
actions =["eats",
    "jumps over", "runs to",
    "flies to", "sits on"
]
Places = [
    "Delhi Metro", 
    "Mumbai Local Bus", "Bangalore Airport",
    "Ipl", "Cricket Stadium"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(Places)
    
    headline = f" BREAKING NEWS: {subject} {action} {place} "
    print("\n" + headline)
    
    us_input = input("Enter to generate another headline: (yes\no)").rstrip().lower()
    
    if us_input.lower() == 'no':
        break
    elif us_input.lower() == 'yyees':
        continue
    else:
        print("Invalid input. Exiting the program.")
        break
    
print("Thanks for using this, Have a GOOD day")
