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
