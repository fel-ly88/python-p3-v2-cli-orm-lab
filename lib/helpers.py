from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    """List all employees"""
    for emp in Employee.all():
        print(emp)


def find_employee_by_name():
    """Find employee by name"""
    name = input("Enter the employee's name: ")
    emp = Employee.find_by_name(name)
    if emp:
        print(emp)
    else:
        print(f"Employee {name} not found")


def find_employee_by_id():
    """Find employee by id"""
    emp_id = input("Enter the employee's id: ")
    emp = Employee.find_by_id(emp_id)
    if emp:
        print(emp)
    else:
        print(f"Employee {emp_id} not found")


def create_employee():
    """Create a new employee"""
    try:
        name = input("Enter the employee's name: ")
        job_title = input("Enter the employee's job title: ")
        dept_id = input("Enter the employee's department id: ")

        dept = Department.find_by_id(dept_id)
        if not dept:
            raise ValueError("department_id must reference a department in the database")

        emp = Employee(name=name, job_title=job_title, department_id=dept_id)
        emp.save()
        print(f"Success: {emp}")
    except Exception as e:
        print(f"Error creating employee: {e}")


def update_employee():
    """Update an existing employee"""
    emp_id = input("Enter the employee's id: ")
    emp = Employee.find_by_id(emp_id)
    if not emp:
        print(f"Employee {emp_id} not found")
        return

    try:
        new_name = input("Enter the employee's new name: ")
        if new_name:
            emp.name = new_name

        new_job_title = input("Enter the employee's new job title: ")
        if new_job_title:
            emp.job_title = new_job_title

        new_dept_id = input("Enter the employee's new department id: ")
        if new_dept_id:
            dept = Department.find_by_id(new_dept_id)
            if not dept:
                raise ValueError("department_id must reference a department in the database")
            emp.department_id = new_dept_id

        emp.save()
        print(f"Success: {emp}")
    except Exception as e:
        print(f"Error updating employee: {e}")


def delete_employee():
    """Delete an employee"""
    emp_id = input("Enter the employee's id: ")
    emp = Employee.find_by_id(emp_id)
    if not emp:
        print(f"Employee {emp_id} not found")
        return

    emp.delete()
    print(f"Employee {emp_id} deleted")


def list_department_employees():
    """List all employees in a department"""
    dept_id = input("Enter the department's id: ")
    dept = Department.find_by_id(dept_id)
    if not dept:
        print(f"Department {dept_id} not found")
        return

    for emp in dept.employees():
        print(emp)