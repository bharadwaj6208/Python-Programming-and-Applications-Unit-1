battery = 100
minutes = 0
while battery > 20:
    battery -= 7
    minutes += 1
print(f"Low battery alert after {minutes} minutes ({battery}%)")

batt = 100
mins = 0
while batt > 20:
    batt -= 7
    mins += 1
    print(f"minute {mins:2d} -> battery {batt}%")
print("alert")

# bat = 100
# min = 0
# while bat > 20:
#     min += 1
#     print(f"minute {min:2d} -> battery {bat}%")
# print("alert")
# the above line of code is commented out because it will create an infinite loop since the battery percentage is never decreased.
