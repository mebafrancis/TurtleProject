import pandas

squirreldata = pandas.read_csv("SquirrelData_2018.csv")
black_Count = len(squirreldata[squirreldata["Primary Fur Color"] == "Black"])
gray_Count = len(squirreldata[squirreldata["Primary Fur Color"] == "Gray"])
cinnamon_Count = len(squirreldata[squirreldata["Primary Fur Color"] == "Cinnamon"])
data_dict = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [black_Count, gray_Count, cinnamon_Count]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("color_data.csv")