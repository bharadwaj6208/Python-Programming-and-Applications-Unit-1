position = (4.2, 7.8)
print(position, type(position))
x, y = position
print(f"x = {x} and y = {y}")
single = (5, )
print(single, type(single))

visited = {(0,0), (0,1)}
print(type(visited))
visited.add((1,1))
visited.add((0,0))
print(visited)
print(f"count : {len(visited)}")
print(f"(1,1) in visited? {(1,1) in visited}")
print(f"(9,9) in visited? {(9,9) in visited}")

codes = ["e2", "e7", "e2", "e1", "e7"]
print(f"raw = {codes}")
print(f"unique = {set(codes)}")
print(f"unique count = {len(set(codes))}")

#Write a program to simulate a robot visiting grid cells, start with an empty set, add 9 coordinates of which 3 repeates
#then print how many distinct cells were visited and test whether (2,2) was among them

coords = set()
coords.add((0,0))
coords.add((0,1))
coords.add((0,2))
coords.add((0,3))
coords.add((0,3))
coords.add((0,2))
coords.add((1,2))
coords.add((1,1))
coords.add((0,1))
print(f"coords = {coords}")
print(f"distinct coords visited = {len(coords)}")
print(f"(2,2) visited? {(2,2) in coords}")

robot = {"name" : "Alpha", "battery" : 78, "mode" : "auto"}
print(robot)
print(robot["name"])
robot["battery"] -= 5
robot["speed"] = 0.4
print(robot)
print(f"list : {list(robot.keys())}")
print(f"values : {list(robot.values())}")
#you cannot printout a key's value for they do not exist in the dictionary
print("speed" in robot)
# "in" will check the wheather it's exist or not

r= {"name" : "Alpha", "battery" : 78}
print(r.get("speed"))
print(r.get("speed",0.0))
#get is used to prevent errors
print("speed" in r)

log =["e2", "e7", "e2", "e1", "e7", "e2"]
freq = {}
for code in log:
    freq[code] = freq.get(code, 0) + 1
print(freq)
for code in sorted(freq, key = freq.get, reverse = True):
    print(f"{code} occured {freq[code]} time(s)")

#write a program that counts the frequency of characters in your own name, prints each letter with its count
#and then prints the most frequent letter

name = "Bharadwaj"
dictName = {}
for char in name:
    dictName[char] = dictName.get(char, 0) + 1
print(dictName)
for char in dictName:
    print(f"{char} is repeated {dictName[char]} time(s)")

