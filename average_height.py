heights = input("Enter heights: ").split()
summation = 0
height_count = 0
for i in range(len(heights)):
    summation += int(heights[i])
    height_count += 1

result = round(summation / height_count)

print(result)
