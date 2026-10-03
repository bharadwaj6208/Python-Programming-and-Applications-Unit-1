waypoints = [(0, 0), (2, 3), (5, 1)]
for wp in waypoints:
    print(f"heading to {wp}")

for i in range(3):
    print(f"Scan {i}")
print("---")

for i in range(1, 6):
    print(i, end = " ")
print()

for i in range(10, 0, -2):
    print(i, end = " ")
print()

for i in range(5, 1, -1):
    print(f"scan {i}")
print("-----")

#The Accumulator Pattern

readings = [22.5, 23.1, 21.8, 24.0, 22.9]
total = 0
for r in readings:
    total += r
print(f"sum : {total:.2f}")
print(f"count : {len(readings)}")
print(f"mean : {total/len(readings)}")

#Nested Loops

obstacles = [(1,2), (3,3), (0,4)]
for row in range(5):
    for col in range(5):
        if (row, col) in obstacles:
            print("#", end = "")
        else:
            print(".", end = "")
    print()

# Write a python program to generate a grid of (8 x 8) and place atleast 3 obstacles at positions of your choice
# Then add a start marker "S", at (0, 0) and a goal "G" at (7,7)

obs = [(6,7), (6,6), (4,2), (0,1)]
for r in range(8):
    for c in range(8):
        if (r, c) == (0, 0):
            print("S", end = " ")
        elif (r, c) == (7, 7):
            print("G", end = " ")
        elif (r, c) in obs:
            print("#", end = " ")
        else:
            print(".", end = " ")
    print(" ")


raw= "   Alpha Rover   "
print(f"[{raw}]")
print(f"[{raw.strip()}]")
print(raw.strip().lower())
print(raw.strip().upper())
print(raw.strip().replace("","_"))
print("Rover" in raw)