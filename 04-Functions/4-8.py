def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02}:{minutes:02}"
    elif time_format == '12':
        if hours == 0:
            hour_12 = 12
            period = 'am'
        elif hours == 12:
            hour_12 = 12
            period = 'pm'
        elif hours > 12:
            hour_12 = hours - 12
            period = 'pm'
        else:
            hour_12 = hours
            period = 'am'

        return f"{hour_12}:{minutes:02}{period}"
    else:
        return "Invalid format"

# Program to test the function:
test_cases = [
    (15, 38, '24'),
    (8, 3, '24'),
    (0, 5, '24'),
    (11, 15, '12'),
    (0, 7, '12'),
    (7, 30, '12'),
    (12, 46, '12'),
    (13, 10, '12'),
    (19, 2, '12'),
]

for hours, minutes, format_type in test_cases:
    result = time_string(hours, minutes, format_type)
    print(f"this:({hours}, {minutes}, '{format_type}') returns this: '{result}'")