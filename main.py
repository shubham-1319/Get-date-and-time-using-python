import datetime

def get_realtime_date_time():
    # Get the current date and time
    current_datetime = datetime.datetime.now()
    
    # Format the date and time
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    return formatted_datetime

# Get and print the current date and time
current_date_time = get_realtime_date_time()
print("Current Date and Time:", current_date_time)
