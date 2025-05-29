"""Module to represent a student and their grades."""

class Student:
    """Class representing a student."""

    def __init__(self, student_id, name):
        """Initialize the student with ID and name."""
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"

    def add_grade(self, grade):
        """Add a single grade to the student's record."""
        self.grades.append(grade)

    def calculate_average(self):
        """Calculate and return the average grade."""
        if not self.grades:
            return 0
        total = sum(self.grades)
        return total / len(self.grades)

    def check_honor(self):
        """Check if student is in honor group."""
        if self.calculate_average() > 90:
            self.honor = "Yes"
        else:
            self.honor = "No"

    def delete_grade(self, index):
        """Delete grade at specified index."""
        if 0 <= index < len(self.grades):
            del self.grades[index]

    def report(self):
        """Print a report of the student's performance."""
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.calculate_average()}")
        print(f"Honor: {self.honor}")

def start_run():
    """Run a demo of student functionality."""
    student_a = Student("x001", "Alice")
    student_a.add_grade(100)
    student_a.add_grade(50)  # Changed from string "Fifty" to numeric 50
    student_a.check_honor()
    student_a.delete_grade(1)  # Valid index now
    student_a.report()

start_run()
