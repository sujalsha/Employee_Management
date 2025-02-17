from flask import Flask, request, jsonify

app = Flask(__name__)

# Store employees in a dictionary
employees = {}

@app.route('/')
def home():
    return "Welcome to Employee Management System"

@app.route('/add_employee')
def add_employee():
    try:
        employee_id = int(request.args.get('employee_id'))
        name = request.args.get('name')
        department = request.args.get('department')

        if employee_id in employees:
            return jsonify({"error": "Employee ID already exists!"}), 400

        employee = Employee(employee_id, name, department)
        employees[employee_id] = employee

        return jsonify({"message": "Employee added successfully", "details": employee.display_employee()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
