def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

user_temp = float(input("Enter temperature:"))
print(weather_condition(user_temp))