class Employee:
    employee_ids = set()  # Set to store unique employee IDs

    def __init__(self, employee_id, name, department):
        if employee_id in Employee.employee_ids:
            raise ValueError("Employee ID must be unique.")
        self.employee_id = employee_id
        self.name = name
        self.department = department
        Employee.employee_ids.add(employee_id)

    def display_employee(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Department: {self.department}"
