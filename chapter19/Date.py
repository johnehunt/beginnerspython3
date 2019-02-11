class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def is_day_of_week(self):
        """Check if date is a week day"""
        # … To be defined

    def in_month(self, month_index):
        """Check if month is in month_index"""
        return self.month == month_index


date = Date(12, 2, 1998)
date.is_day_of_week()
date.in_month(12)