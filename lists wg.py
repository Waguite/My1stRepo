name="Ware"
subjects=["English","math","chinese","history"]
print("Hello "+name)
for i in subjects:
    print("One of my subjects is "+ i)
characters = ["Harry Potter","Hermoine","voldemort","Hagrid"]
for i in characters:
    print("one of my favorite characters in Harry Potter is "+i)
    if i == "voldemort":
        print(i+" is the villain!")
    elif i == "Harry Potter":
        print(i+" is the protagonist.")
    elif i=="Hagrid" or i=="Hermione":
        print (i+" is Harry's friend.")


movies = []
while True:
    print("what's your favorite movie? Type 'end' to quit")
    answer = input()
    if answer == "end":
        break
    else:
        movies.append(answer)
for i in movies:
    print("one of your favorite movies "+i)
