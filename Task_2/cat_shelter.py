
import sys

def format_time(minutes): # to convert total minutes to hours and minutes format
    hours = minutes // 60
    minutes %= 60
    return f"{hours} Hours, {minutes} Minutes"

def analyze_cat_shelter_log(file_path):
    try:
        with open(file_path, 'r') as file: # access file for reading
            lines = file.readlines()
    except FileNotFoundError:  # handle file not found error
        print(f'Cannot open "{file_path}"!')
        return
    # Initializing the variables to analyse 
    cat_visits = 0
    other_cats = 0
    total_time_in_house = 0
    durations = []

    for line in lines: #Iterate through each line in the file
        if line.strip() == 'END':
            break
        # split the line into cat name, entery time and exit time
        cat, entry_time, exit_time = line.strip().split(',')
        entry_time, exit_time = int(entry_time), int(exit_time)
        # analyze visit based on cat type
        if cat == 'OURS':
            cat_visits += 1
            total_time_in_house += exit_time - entry_time
            durations.append(exit_time - entry_time)
        elif entry_time != exit_time:
            other_cats += 1
    # if no visits for the corect cat were recorded
    if cat_visits == 0:
        print('No visits recorded for the correct cat.')
        return
    # calculate average, longest and shortest visit durations
    average_duration = format_time(sum(durations) // len(durations))
    longest_duration = format_time(max(durations))
    shortest_duration = format_time(min(durations))
    # print the analysis result
    print('Log File Analysis')
    print('==================')
    print(f'Cat Visits: {cat_visits}')
    print(f'Other Cats: {other_cats}')
    print(f'Total Time in House: {format_time(total_time_in_house)}')
    print(f'Average Visit Length: {average_duration}')
    print(f'Longest Visit: {longest_duration}')
    print(f'Shortest Visit: {shortest_duration}')

if __name__ == "__main__":
    # check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print('Missing command line argument!')
    else:
        # Analyze the cat shelter log file specified in the command-line argument
        analyze_cat_shelter_log(sys.argv[1])
