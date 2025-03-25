from datetime import datetime, timedelta
from operator import itemgetter

# parse date to a desired format
def parse_date(date_str):
    return datetime.strptime(date_str, "%m/%d/%y").date()

# determine reimbursement rate 
# for travel/full day and city type
def determine_reimbursement_rate(cost_type, is_travel):
    if is_travel:
        if cost_type=="low":
            return 45
        else:
            return 55
    else:
        if cost_type=="low":
            return 75
        else:
            return 85

# calculate reimbursement total for each project/set
def calculate_reimbursement(projects):
    sorted_projects = sorted(projects, key=itemgetter("start"))

    if not sorted_projects:
        return []
    
    timeline = {}
    
    def update_day(date, cost_type, is_travel):
        rate = determine_reimbursement_rate(cost_type, is_travel)

        # update the daily rate if its different
        if date not in timeline or rate > timeline[date]['rate']:
            timeline[date] = {
                'rate': rate,
                'cost_type': cost_type,
                'is_travel': is_travel
            }
    
    # loop through projects
    for i, project in enumerate(sorted_projects):
        start, end, cost_type = project["start"], project["end"], project["cost"]
        
        # iterate through all days of the project
        days = list(start + timedelta(days=j) for j in range((end - start).days + 1))
        
        for j, current_date in enumerate(days):
            # check if its travel day or not
            is_travel = (j == 0 or j == len(days) - 1)
            
            #update day
            update_day(current_date, cost_type, is_travel)
    
    # sum up the daily rates together
    return sum(day['rate'] for day in timeline.values())

def main():
    scenarios = [
        [
            {"start": parse_date("10/1/24"), "end": parse_date("10/4/24"), "cost": "low"},
        ],
        [
            {"start": parse_date("10/1/24"), "end": parse_date("10/1/24"), "cost": "low"},
            {"start": parse_date("10/2/24"), "end": parse_date("10/6/24"), "cost": "high"},
            {"start": parse_date("10/6/24"), "end": parse_date("10/9/24"), "cost": "low"},
        ],
        [
            {"start": parse_date("9/30/24"), "end": parse_date("10/3/24"), "cost": "low"},
            {"start": parse_date("10/5/24"), "end": parse_date("10/7/24"), "cost": "high"},
            {"start": parse_date("10/8/24"), "end": parse_date("10/8/24"), "cost": "high"},
        ],
        [
            {"start": parse_date("10/1/24"), "end": parse_date("10/1/24"), "cost": "low"},
            {"start": parse_date("10/1/24"), "end": parse_date("10/1/24"), "cost": "low"},
            {"start": parse_date("10/2/24"), "end": parse_date("10/3/24"), "cost": "high"},
            {"start": parse_date("10/2/24"), "end": parse_date("10/6/24"), "cost": "high"},
        ],
    ]

    # calculate and print the reimbursement total for each set
    # expected_results = [240, 605, 490, 410]
        # from my own calculations
    for i, scenario in enumerate(scenarios, 1):
        reimbursement = calculate_reimbursement(scenario)
        print(f"Set {i}: Reimbursement = ${reimbursement}")
      

if __name__ == "__main__":
    main()