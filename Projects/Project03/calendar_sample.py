import calendar
import random

def generate_schedule(people, year, month):
    # Define shifts
    shifts = ["7:00AM - 1:00PM", "1:00PM - 7:00PM"]

    # Get the number of days in the specified month
    num_days = calendar.monthrange(year, month)[1]
    
    # Randomly assign people to shifts for each day of the month
    schedule = {}
    for day in range(1, num_days + 1):
        schedule[day] = {
            shifts[0]: random.choice(people),  # Assign someone to the morning shift
            shifts[1]: random.choice(people)   # Assign someone to the afternoon shift
        }

    return schedule

def display_schedule_as_html(schedule, year, month):
    # Create the HTML structure
    html_schedule = f"""
    <html>
    <head>
        <title>Work Schedule for {calendar.month_name[month]} {year}</title>
        <style>
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid black;
                padding: 10px;
                text-align: center;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            td {{
                height: 100px;
                vertical-align: top;
            }}
        </style>
    </head>
    <body>
        <h1>Work Schedule for {calendar.month_name[month]} {year}</h1>
        <table>
            <tr>
                <th>Mon</th>
                <th>Tue</th>
                <th>Wed</th>
                <th>Thu</th>
                <th>Fri</th>
                <th>Sat</th>
                <th>Sun</th>
            </tr>
    """
    
    # Get the first weekday of the month and the total days
    first_weekday, num_days = calendar.monthrange(year, month)

    # Fill in the days of the month
    current_day = 1
    for week in range((num_days + first_weekday) // 7 + 1):
        html_schedule += "<tr>"
        for day in range(7):
            if (week == 0 and day < first_weekday) or current_day > num_days:
                html_schedule += "<td></td>"  # Empty cell for days outside the month
            else:
                # Add the day and the assigned shifts
                shifts_for_day = schedule.get(current_day, {})
                morning_shift = shifts_for_day.get("7:00AM - 1:00PM", "N/A")
                afternoon_shift = shifts_for_day.get("1:00PM - 7:00PM", "N/A")

                html_schedule += f"<td>{current_day}<br><b>AM:</b> {morning_shift}<br><b>PM:</b> {afternoon_shift}</td>"
                current_day += 1
        html_schedule += "</tr>"

    # Close the table and HTML
    html_schedule += """
        </table>
    </body>
    </html>
    """
    
    # Write the HTML content to a file
    with open(f"work_schedule_{year}_{month}.html", "w") as file:
        file.write(html_schedule)

    print(f"HTML work schedule for {calendar.month_name[month]} {year} generated successfully!")

# Sample list of people to assign
people = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]

# Get user input for the year and month
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Generate the work schedule
schedule = generate_schedule(people, year, month)

# Display the schedule as an HTML calendar
display_schedule_as_html(schedule, year, month)
