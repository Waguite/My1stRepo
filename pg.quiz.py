import pyautogui as pg
import time
import webbrowser

points=0

#question goes here
answer = pg.prompt(
"""
What animal are you most like?

What is your favorite passtime?
a)eating acorns
b)crawling around on your knuckles and knees
c)eating fish
""")
pg.alert("You chose " + answer + "!")
#answer
if answer == "a":
    points += 1
elif answer == "b":
    points += 0
elif answer == "c":
    points += 3
    
#question goes here
answer = pg.prompt(
"""
What is your favorite way to get around?

a)running on all fours
b)swinging through trees
c)swimming
""")
pg.alert("You chose " + answer + "!")
#answer
if answer == "a":
    points += 1
elif answer == "b":
    points += 0
elif answer == "c":
    points += 3

#question goes here
answer = pg.prompt(
"""

What is your favorite food?
a)acorns
b)bamboo chutes and termites
c)fish
""")
pg.alert("You chose " + answer + "!")
#answer
if answer == "a":
    points += 1
elif answer == "b":
    points += 0
elif answer == "c":
    points += 3
#question goes here
answer = pg.prompt(
"""

How do you get your food?
a)I find it on the ground
b)using a stick to attract termites from their nest
c)hunting under water
""")
pg.alert("You chose " + answer + "!")
#answer
if answer == "a":
    points += 1
elif answer == "b":
    points += 0
elif answer == "c":
    points += 3
#question goes here
answer = pg.prompt(
"""

Where do you like to sleep
a)in a hole in a  tree
b)in a nest in a tree
c)under water
""")
pg.alert("You chose " + answer + "!")
#answer
if answer == "a":
    points += 1
elif answer == "b":
    points += 0
elif answer == "c":
    points += 3


#end of survey
    pg.alert ("ok heres your animal...")
if points < 3:
    pg. alert ("Your animal is a squirrel!")
    webbrowser.open("https://www.google.com/search?q=squirrel&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj96P7JtO7YAhUChOAKHaLFCUoQ_AUICigB&biw=1366&bih=637#imgrc=2HknzKudHCtJAM:")
elif points >= points < 5:
    pg.alert ("Your animal is a gorilla!")
    webbrowser.open("https://www.google.com/search?q=gorilla&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwinpuaIte7YAhUlUd8KHdauCUIQ_AUICigB&biw=681&bih=612#imgrc=cPNeN7YH1SZM5M:")
elif points >= 5:
    pg.alert ("Your animal is a shark!")
    webbrowser.open("https://www.google.com/search?q=shark&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiUv_bZte7YAhWRmOAKHZhJAvEQ_AUICigB&biw=884&bih=612#imgrc=QseLcD3sf7KK6M:")
