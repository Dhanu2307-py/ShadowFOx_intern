# Initial list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Calculate the number of members
num_members = len(justice_league)
print(f"Number of members in the Justice League: {num_members}")

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("Justice League after adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Justice League after moving Wonder Woman to the beginning:", justice_league)

# 4. Separate Aquaman and Flash by moving Green Lantern between them
justice_league.remove("Green Lantern")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")
print("Justice League after separating Aquaman and Flash:", justice_league)

# 5. Replace the existing list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("Justice League after replacing with new members:", justice_league)

# 6. Sort the list alphabetically and identify the new leader
justice_league.sort()
print("Justice League sorted alphabetically:", justice_league)
new_leader = justice_league[0]
print(f"The new leader of the Justice League is: {new_leader}")
4