# Heldi reimbursement_calc 

from datetime import datetime, timedelta
from collections import defaultdict

def parse_date(date_str):
    return datetime.strptime(date_str, "%m/%d/%y").date()

def determine_reimbursement_rate():
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


if __name__ == "__main__":
    main()