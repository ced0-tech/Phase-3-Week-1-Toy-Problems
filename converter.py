def convert_to_24_hour(hour, minute, period):
    if hour not in range(1, 13):
        raise ValueError("Hour should be between 1 and 12")
    if minute not in range(60):
        raise ValueError("Minute should be between 0 and 59")
    
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    return f"{hour:02d}{minute:02d}"

