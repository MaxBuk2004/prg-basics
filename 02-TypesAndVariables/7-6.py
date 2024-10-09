speed = float(input('Enter vehicle speed in km/h:'))
speed_good = (speed>=40 and speed<=140)
print(f'Speed is valid: {speed_good}')