import random

#1 create list with 10 random nums between -25 and 25
num = []
n = int(10)
for j in range(n):
    num.append(random.randint(-25,25))
print('Randomised list: ', num)

#2 utilizing list comprehension to create new list with negs
negNum = [ n for n in num if n < 0]
print(negNum)

#3 create a tuple with 2  fav foods loop through tuple and print all
fav_food = ('Chinease', 'Hibachi', 'Eggs')
for food in fav_food: print(food)

#4 create a set of 10 random numbers between 1 and 100, search set for value 50
# and print out a statement indicating wheter or not the set contains 50
random_set = set()
numb = int(10)
for i in range(numb):
    random_set.add(random.randint(1,100))
print(random_set)
if 50 in random_set:
    print("has 50")
else:
    print("no 50")

#5 create dictionary containing some fav books or movies and numerical rating
# from 1-5

favMovies = {
    "Boondock Saints": 4,
    "Pepperment": 4,
    "Supernatural": 5,
    "Lucifer": 5,
    "Shanara Chronicals": 5,
    "Titanic": 2
}
print(favMovies)

#6 remove on entrie and add a new one
del favMovies["Titanic"]
print(favMovies)

favMovies["10 Things I hate about you"]=5
print(favMovies)

