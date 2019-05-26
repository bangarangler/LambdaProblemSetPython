print("Hello World")

#LIST
# create it
my_colors = ["red", "orange", "yellow"]

# add vs. insert
# my_colors.append("green") # add to end
# my_colors.insert(2, "blue") # insert at i

# remove vs. pop vs. del
# my_colors.remove("orange") # removes item
# my_colors.pop() #removes last item
# del my_colors[1] # removes item at i

# traverse
# for i in range(0, len(my_colors)):
    #access an item
    # print(my_colors[i])

# 1st item you want: 1st irem you DON'T want
# primary_colors = my_colors[0:2]

# 1st item you want: #(goes to end)
# primary_colors = my_colors[1:]

# 1st item you DON'T want #(starts at beginning)
# primary_colors = my_colors[:2]

# returns new list of colors with less # than 5 chars
# new_colors = [c for c in my_colors if len(c) < 5]

# print(my_colors)
# print(primary_colors)
# print(new_colors)

#Tuples can not mutate no add no change no remove
# my_animals = ("dog","cat","fish")
# length
# print(len(my_animals))
#traverse
# for animal in my_animals:
    #access an item
    # print( animal )

# SET
# create it
# my_cities = {"Dallas","Houston","Austin"}
# print(my_cities)

#add
# my_cities.add("San Antonio")
# print(my_cities)
# my_cities.update(["Boerne","Galveston"])
# print(my_cities)

# remove vs. pop
# my_cities.remove("Houston")
# print(my_cities)
# my_cities.pop()
# print(my_cities)

#length
# print(len(my_cities))

# change is not allowed
# my_cities[2] = "El Paso" # NOT ALLOWED!

#Dictionaries

#create it
# my_grades = {
    # #"key":"value",
    # "Math":88,
    # "Science":85,
    # "English":91,
    # "History":92
# }
# print(my_grades)

# # access
# print(my_grades.get("History"))

# #add
# my_grades["Art"]=81 # use new key
# print(my_grades)
# print(my_grades.get("Art"))

# # change
# my_grades["English"]=93
# print(my_grades.get("English"))

# # remove vs. pop
# my_grades.pop("Science") #remove specific item
# my_grades.popitem() # remove last item
# print(my_grades)

# #length
# print(len(my_grades))

# # traverse
# for grade in my_grades:
    # print(grade + ":" + my_grades[grade])

# Polya's Problem Solving Techniques
# steps 1. Understand the problem 2. Devise a plan 3. Implement it 4. Reflect
# Dining Philosophers
# def feed_philosophers():
    # eating=[True, False, True, False, False]
    # i=0
    # while i < len(eating):
        # if eating[4]:
            # eating[4] = False
            # eating[i] = True
        # else:
            # if eating[i-1]:
                # eating[i-1]=False
                # eating[i] = True
        # i = (i+1) % 5
# Rock Paper Scissors
# Rules two players, 3 choices rock, paper, scissors
#results win, lose, tie
# display message @ start of game
# load persistent game stats from .txt file
# prompt user to choose: rock, paper, scissors, or quit game
# compare with computer choice
# display message that choice was invalid
# save new game data into .txt file
