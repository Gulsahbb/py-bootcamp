x = "-----------------------------------------------------------------"

message = "Hello, my name is Amir! Nice to meet you. What is yours?"
print(message)

print(x)
answer = "Hello, my name is Elena" 
print(answer)
print(x)
his_age = 20
his_height = 1.76
his_hair_color = "brunette"
his_hometown = "Iran"
where_he_lives = "Turkey"

print(f'I am {str(his_age)} years old, {str(his_height)} tall boy from {his_hometown} but I currently live in {where_he_lives}.')

print("What about you? Tell me about yourself.")
print(x)

my_age = 22
my_height = 1.65
my_hair_color = "black"
my_hometown = "America"
where_i_live = "London"


print(type(my_age))
print(type(my_height))
print(type(my_hometown))
print(type(where_i_live))
print(x)

print(f'I am {str(my_age)} years old, {str(my_height)} tall girl from {my_hometown} but I currently live in {where_i_live}.')
print(x)
favourite_places_foods = ["Paris", "Milan", "Barcelona", "Berlin", "Vegas", "Croissant", "Pasta", "Pizza", "Hamburger", "Steak"]

print(favourite_places_foods)

favourite_places = favourite_places_foods[0:5] #select all the places (Another option [:5])
favourite_food = favourite_places_foods[5:10] #select all the foods (Another option [5:])

#Select the first and last three from place and food lists
first_three_places=favourite_places[0:3]
last_three_foods =favourite_food[2:5]

#Print both lists
print(first_three_places)
print(last_three_foods)

print(x)

#Please import the random module and generate two random numbers between 0 and 2
import random
a = random.randint(0,2)
b = random.randint(0,2)

#Use the generated numbers as indexes of randomely chosen items from place and food lists

meeting_place = first_three_places[a]
meeting_food = last_three_foods[b]
print(meeting_place)
print(meeting_food)

print(x)

first_activity = "lets play chess in the park"
second_activiy = "lets play a game of tennis"
third_activity = "lets go to the museum"

#Write your and Amir's preference for each activity either as "True" or "False"

#First activity
first_activity_your = True
first_activity_friend = False

#Example statement
print("We are going to play chess in the park! Answer:" ,first_activity_your and first_activity_friend)
 
#Second activity
second_activity_your = True
second_activity_friend = True
 
#Your turn to write the statement
print("We are going to play a game of tennis. Answer:" ,second_activity_your and second_activity_friend)
 
#Third activity
second_activity_your = False
second_activity_friend = False
 
print("At least one of us is going to the museum. Answer:" ,second_activity_your or second_activity_friend)

print(x)

#Create a variable for your trip date that asks Amir for an input
meeting_date = input('In which month do you want to do on our fun adventure?: ')

#Print the date for the trip by using it in a sentence
print("We are going to",meeting_place, "and we will eat", meeting_food, "in", meeting_date)