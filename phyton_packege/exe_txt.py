# 14.1
with open('story.txt', 'w')as f:
    f.writelines("A boy is playing there.\n"
                 "There is a playground.\n"
                 "An airplane is in the sky.\n"
                 "The sky is pink.\n"
                 "Alphabets and numbers are allowed in the password.")
story_file = open('story.txt', 'r+')
print(story_file.read())

# 14.2 a פונקציה הבודקת את האות T
story_file = open('story.txt', 'r+')
count = 0
for line in story_file:
    if line[0] != 'T':
        count += 1
print(count)

# 14.2 b פונקציה הסופרת המילה The the
story_file = open('story.txt', 'r')
count = 0
for line in story_file:
    if line != 'The' or line != 'the':
        count += 1
print(count)

# 14.2 c פונקציה המחזירה את מספר המילים בקובץ
story_file = open('story.txt', 'r')
count = 0
for line in story_file:
    words=line.split()
    for word in words:
        count += 1
print(count)

# 14.3 a מדפיסה את השורות
story_file = open('story.txt', 'r')
for i in story_file:
    print(i,end="")
print()
# 14.3 b סופרת את השורות
with open('story.txt','r') as f:
    count=0
    while True:
        count+=1
        line=f.readline()
        if not line:
            break
    print(f"the number of lines is: {count-1}")