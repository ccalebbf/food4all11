# -- Function that deals with all things maps related --

# Purple - no record
# Blue - within 1 week
# Green - 1 to 2 weeks
# Orange - 2 to 4 weeks
# Red - more than 4 weeks

def time_to_colour(time):
    if time == "No Record" or time < 0:
        return 'purple'
    elif time <= 7:
        return 'blue'
    elif time <= 14:
        return 'green'
    elif time <= 28:
        return 'orange'
    else:
        return 'red'