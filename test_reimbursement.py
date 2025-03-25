import unittest
from datetime import datetime
from reimbursement_calc import parse_date, calculate_reimbursement

class TestReimbursementCalculation(unittest.TestCase):
    def test_single_project_low_cost(self):
        # Test a single project in a low-cost city
        projects = [{"start": parse_date("10/1/24"), "end": parse_date("10/4/24"), "cost": "low"}]
        self.assertEqual(calculate_reimbursement(projects), 240)
    def test_single_day_project_high(self):
        # Test a single-day project in a high-cost city
        projects = [{"start": parse_date("10/11/24"), "end": parse_date("10/11/24"), "cost": "high"}]
        self.assertEqual(calculate_reimbursement(projects), 55)
    def test_multiple_overlapping_projects(self):
        # Test overlapping projects with different cost types
        projects = [
            {"start": parse_date("10/1/24"), "end": parse_date("10/1/24"), "cost": "low"},
            {"start": parse_date("10/2/24"), "end": parse_date("10/6/24"), "cost": "high"},
            {"start": parse_date("10/6/24"), "end": parse_date("10/9/24"), "cost": "low"},
        ]
        self.assertEqual(calculate_reimbursement(projects), 605)
    def test_overlapping_single_day_projects(self):
        # Test overlapping projects on the same day with different cost types, highest cost applies to the set
        projects = [
            {"start": parse_date("10/5/24"), "end": parse_date("10/5/24"), "cost": "low"},
            {"start": parse_date("10/5/24"), "end": parse_date("10/5/24"), "cost": "high"},
        ]
        self.assertEqual(calculate_reimbursement(projects), 55)
    def test_empty_project_list(self):
        # Test an empty project list, no reimbursement expected
        projects = []
        self.assertEqual(calculate_reimbursement(projects), 0)
    def test_project_with_gap_days(self):
        # Test two projects with a gap between them
        projects = [
            {"start": parse_date("10/1/24"), "end": parse_date("10/3/24"), "cost": "low"},
            {"start": parse_date("10/5/24"), "end": parse_date("10/7/24"), "cost": "high"},
        ]
        self.assertEqual(calculate_reimbursement(projects), 360)
    



if __name__ == "__main__":
    unittest.main()