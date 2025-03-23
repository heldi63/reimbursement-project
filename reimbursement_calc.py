# Heldi reimbursement_calc 

from datetime import datetime, timedelta
from collections import defaultdict
from operator import itemgetter

#parse project dates in the right format
def parse_date(date_str):
    return datetime.strptime(date_str, "%m/%d/%y").date()


#determine the reimbursement rate 
#depending on the city type and travel/full day
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
        
#merge overlapping projects into one single project
def merge_projects(projects):
    if not projects:
        return []
    
    projects.sort(key=itemgetter("start"))

    merged_projects = [projects[0]]

    for project in projects[1:]:
        last_project = merged_projects[-1]
        if project["start"] <= last_project["end"] + timedelta(days=1):  
            last_project["end"] = max(last_project["end"], project["end"]) 
        else:
            merged_projects.append(project)
    
    return merged_projects
    




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

    #TODO
    #loop through scenarios and implement funciton to calculate the reimbursement
    #return cost


if __name__ == "__main__":
    main()