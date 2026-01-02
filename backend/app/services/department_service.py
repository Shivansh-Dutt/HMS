from app.models import Department

def get_all_departments():
    departments = Department.query.all()
    
    return [
        {
            "id" : d.id,
            "name" : d.name
        }
        for d in departments
    ]

def get_department(dept_id):
    department = Department.query.get(dept_id)
    print(department)
    
    return {
        "name": department.name,
        "overview": department.description
    }