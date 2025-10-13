# import csv
#
# temperature = []
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data)
#     for row in data:
#      print(row)
#      temperature.append(int(row[1]))
#
# print(temperature)
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)
# sum =0
# for temp in temp_list:
#     sum+=int(temp)
# avg= sum/len(temp_list)
# print(f"Average is {avg}")
print(data["temp"].mean())
print(data["temp"].max())
print(data.condition)

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 +32
print(monday_temp_F)

#Create  a data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")


