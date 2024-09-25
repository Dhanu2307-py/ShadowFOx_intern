import random

# Initialize counters
count_6 = 0
count_1 = 0
count_6s = 0

# Simulate rolling the die 20 times
previous_roll = 0
for _ in range(20):
    roll = random.randint(1, 6)
    print(f"Rolled: {roll}")

    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            count_6s += 1
    if roll == 1:
        count_1 += 1

    previous_roll = roll

# Print the statistics
print(f"Number of times rolled a 6: {count_6}")
print(f"Number of times rolled a 1: {count_1}")
print(f"Number of times rolled two 6s in a row: {count_6s}")

#Workoutroutine

total_jumping_jacks = 100
jumping_jacks_per_set = 10
completed_jumping_jacks = 0

while completed_jumping_jacks < total_jumping_jacks:
    print(f"Perform {jumping_jacks_per_set} jumping jacks.")
    completed_jumping_jacks += jumping_jacks_per_set
    print(f"Total completed: {completed_jumping_jacks}")

    if completed_jumping_jacks >= total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed_jumping_jacks} jumping jacks.")
            break
    else:
        remaining = total_jumping_jacks - completed_jumping_jacks
        print(f"{remaining} jumping jacks remaining.")
