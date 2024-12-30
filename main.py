
# with open ("weather.csv") as file:
    # contents = file.readlines()
    # print(contents)
    
# import csv

    
# so instead of the previous code we are going to write:
#with open("weather.csv") as file:
 #   contents = csv.reader(file)
    #temperatures = []
   # for row in contents:
        # print(row)
    #    if row[1] != "temp":
    #        temperatures.append(int(row[1]))
    #print(temperatures)
# now instead for all that code we are going to use pandas library   
''' import pandas
contents = pandas.read_csv("weather.csv")

# I can convert the file to a dictionary
file_dict = contents.to_dict()
print(file_dict)

# put the temp column in a list
temp_list = contents["temp"].to_list()
print(len(temp_list))

# Get the average
average = sum(temp_list)/len(temp_list)
print(average)

# Get the max
max_index = contents["temp"].argmax()
max_temp = contents["temp"][max_index]

# Get row
# when a particular column is equal to a value we get the row of that value
print(contents[contents["temp"] == max_temp])

#convert Monday's data temp to Fahrenheight
monday = contents[contents["day"] == "Monday"]
Fahrenheit = (contents["temp"][0] * 9/5) + 32
print(Fahrenheit)

# Create a dataframe from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)

# We can convert the data frame to a csv file
data.to_csv("new_data.csv") '''

import pandas

# Read data
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241007.csv")

gray_count = 0
cinnamon_count = 0
black_count = 0
white_count = 0

# Create color list 
color_list = data["Primary Fur Color"].to_list()

for color in color_list:
    if color == "Gray":
        gray_count += 1
    elif color == "Cinnamon":
        cinnamon_count += 1
    elif color == "White":
        white_count += 1
    elif color == "Black":
        black_count += 1
        
# Alternatively: 
''' data = pandas.read_csv("...")
    grey_count = len(data[data["Primary Fur Color"] == "Grey"])
    cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
    black_count = len(data[data["Primary Fur Color"] == "Black"])
    white_count = len(data[data["Primary Fur Color"] ==  "White"])
'''
# Create csv file 
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black", "White"],
    "Count" : [gray_count, cinnamon_count, black_count, white_count]
    
}

file = pandas.DataFrame(data_dict)
file.to_csv("squirrel_count.csv")