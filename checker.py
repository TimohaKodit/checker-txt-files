with open("F:\\tt.txt", "r") as file:
    lines = [i.strip() for i in file]

with open("F:\\bb.txt", "r") as file:
    line = [i.strip() for i in file]

count = []

for i in lines:
    if i in line:
        count.append(i)
    else:
        continue 
if len(count) > 0:
    print("Совпадения найдены: ",', '.join(count))
