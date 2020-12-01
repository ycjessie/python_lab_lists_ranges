# Python Containers and Ranges - Lab

#### Exercise 1 ------------------------------------------------
# - Create a list named `students` containing some student names (strings).
students = ['Jessie', 'Tina', 'Sofia','Peter','Sam']

# - Print out the second student's name.
students[1]

# - Print out the last student's name.

students[-1]

#### Exercise 2 ------------------------------------------------
# - Create a tuple named `foods` containing the same number of foods (strings) as there are names in the `students` list.

foods=('dumplings','fried rice','beef noodles','tofu')

# - Use a `for` loop to print out the string "_food goes here_ is a good food"
foods=('dumplings','fried rice','beef noodles','tofu')
for food in foods:
    print(food+" is a good food ")


#### Exercise 3 ------------------------------------------------
# - Using a `for` loop, print just the last two food strings from `foods`.
foods=('dumplings','fried rice','beef noodles','tofu')
for food in foods:
    print(food[2:])
   
foods=('dumplings','fried rice','beef noodles','tofu')
for index,food in enumerate(foods):
    print(f"{food} is a good food and it is on the index=>{index}")

foods=('dumplings','fried rice','beef noodles','tofu')
for food in foods[2:]:
    print(food)
foods=('dumplings','fried rice','beef noodles','tofu')
for food in foods[-2:]:
    print(food)
#### Exercise 4 ------------------------------------------------
# - Create a dictionary named `home_town` containing the keys of `city`, `state` and `population`.
home_town = [
    {
        "state": "Alabama",
        "city": "Montgomery",
        "population":191216
    }, {
        "state": "Alaska",
        "city": "Juneau",
        "population": 193217
    }, {
        "state": "Arizona",
        "city": "Phoenix",
        "population": 199219
    }, {
        "state": "Arkansas",
        "city": "Little Rock",
        "population": 11121
    }, {
        "state": "California",
        "city": "Sacramento",
        "population": 100218
    }]



# - Print a string with this format:<br>"I was born in _city_, _state_ - population of _population_"
for home in home_town:
    city=home["city"]
    state=home["state"]
    population=home["population"]
    # option1
    print("I was born in "+ home["city"]+","+home["state"]+" population of "+str(home["population"]))
    # option2
    print("I was born in {},{} population of {}".format(city,state,population))
    # option3
    print(f'{city}{state}')

#### Exercise 5 ------------------------------------------------
# - Iterate over the _key: value_ pairs in `home_town` and print a string for each item, for example:<br>"city = Arcadia"<br>"state = California"<br>"population = 58000"



#### Exercise 6 ------------------------------------------------
# - Create an empty list named `cohort`.



# - Using a `for` loop, add one dictionary to the `cohort` list for each student name. Each dictionary should have this shape:

# 	{
# 		'student': 'Tina',
# 		'fav_food' 'Cheeseburger'
# 	}



# - Iterate over `cohort` printing out each element.



#### Exercise 7 ------------------------------------------------
# - Using the list of `students` and list comprehension, assign to a variable named `awesome_students` a new list containing strings similar to this:<br>["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]



# - Iterate over `awesome_students` printing out each string.




#### Exercise 8 ------------------------------------------------
# - Using the tuple `foods` and list comprehension within a `for` loop, print each food string that contains the letter `a`.
