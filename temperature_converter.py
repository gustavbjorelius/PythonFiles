# https://bth.instructure.com/courses/7266/assignments/66766?module_item_id=257383
# 1.16: Temperaturomvandlare 2.0 (skapa och anropa egna funktioner)
# https://m365.cloud.microsoft/chat/conversation/39f798d6-7910-4ab4-9802-141f2c9e14d8

'''
execution order 
1. temperature = get_and_validate_temp() runs first it starts the first defined function get_and_validate_temp()
2. that thing contunually runs until the user feeds in the right input 
'''

def get_and_validate_temp():
    # checks the input is correct 
    try: 
        temperature = float(input("Temperatur i Kelvin: "))
        if temperature < 0: 
            print('Ange ett tal större än 0')
            return get_and_validate_temp()
        return temperature
    except ValueError: 
        print('Du måste mata in ett tal.')
        return get_and_validate_temp() 

def kelvin_to_celsius(temperature):
    return temperature - 273.15

def kelvin_to_fahrenheit(temperature):
    return (33+(temperature-273.15) * 9/5)


def main():
    temperature = get_and_validate_temp()
    kelvin_to_celsius(temperature)
    kelvin_to_fahrenheit(temperature)
    print(f"This is celcius: {kelvin_to_celsius(temperature):.2f} degrees")
    print(f"This is farenheight: {kelvin_to_fahrenheit(temperature):.2f} degrees")

if __name__ == "__main__":
    main()
    # if you don't do this, then by simply importing the file will run it and then it will ask for input where it's not directly asked