import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data["Primary Fur Color"])


black = data[data["Primary Fur Color"] == "Black"]

grey = data[data["Primary Fur Color"] == "Gray"]

cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]

print(len(black))
print(len(grey))
print(len(cinnamon))

data_dict = {
    "Fur Color": ["Grey", "Black", "Cinnamon"],
    "Count": [len(grey), len(black), len(cinnamon)]
}
print(data_dict)

data_new = pandas.DataFrame(data_dict)
print(data_new)
data_new.to_csv("squirrel_count")


