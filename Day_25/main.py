import pandas

data = pandas.read_csv("weather_data.csv")

temp_list = data["temp"].to_list()
print(temp_list)

average_temp = data["temp"].mean()
print(average_temp)

average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

#Get data in Colums
print(data["temp"].max())
print(data["condition"])
print(data.condition)
#data.속성값 -> 객체에 더 가깝게 데이터를 뽑는다

#Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
