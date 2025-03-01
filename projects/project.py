import datetime
from helpers import load_database, save_database

class Project:
    def __init__(self, title, details, target, start_date, end_date, owner_email):
        self.title = title
        self.details = details
        self.target = target
        self.start_date = self.validate_date(start_date)
        self.end_date = self.validate_date(end_date)
        self.owner_email = owner_email
        
        if self.start_date >= self.end_date:
            raise ValueError("Start date must be before end date.")
    
    @staticmethod
    def validate_date(date_str):
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
    
    def to_dict(self):
        return {
            "title": self.title,
            "details": self.details,
            "target": self.target,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "owner_email": self.owner_email
        }

# ====================================================

def add_project():
    print("\nAdd a New Project ")
    title = input("Enter project title: ").strip()
    details = input("Enter project details: ").strip()
    target = input("Enter funding target (EGP): ").strip()
    start_date = input("Enter start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter end date (YYYY-MM-DD): ").strip()
    owner_email = input("Enter your email: ").strip()
    
    try:
        project = Project(title, details, float(target), start_date, end_date, owner_email)
        data = load_database()
        data["projects"].append(project.to_dict())
        save_database(data)
        print("Project added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

 # ====================================================


def view_projects():
    data = load_database()
    projects = data["projects"]
    if not projects:
        print("No projects available.")
        return
    
    print("\nList of Projects")
    for i in range(len(projects)):
        project = projects[i]
        print(f"{i+1}. {project['title']} - Target: {project['target']} EGP")

# ====================================================


def edit_project():
    email = input("Enter your email: ").strip()
    data = load_database()
    projects = data["projects"]
    
    user_projects = [p for p in projects if p["owner_email"] == email]
    if not user_projects:
        print("No projects found under this email.")
        return
    
    print("\nYour Projects")
    for i in range(len(user_projects)):
        project = user_projects[i]
        print(f"{i+1}. {project['title']}")
    
    choice = int(input("Enter project number to edit: ")) - 1
    if 0 <= choice < len(user_projects):
        project = user_projects[choice]
        print("Leave fields blank to keep current values.")
        project["title"] = input(f"Enter new title ({project['title']}): ").strip() or project["title"]
        project["details"] = input(f"Enter new details ({project['details']}): ").strip() or project["details"]
        project["target"] = input(f"Enter new target ({project['target']}): ").strip() or project["target"]
        project["start_date"] = input(f"Enter new start date ({project['start_date']}): ").strip() or project["start_date"]
        project["end_date"] = input(f"Enter new end date ({project['end_date']}): ").strip() or project["end_date"]
        save_database(data)
        print("Project updated successfully!")
    else:
        print("Invalid choice.")

# ====================================================


def delete_project():
    email = input("Enter your email: ").strip()
    data = load_database()
    projects = data["projects"]
    
    user_projects = [p for p in projects if p["owner_email"] == email]
    if not user_projects:
        print("No projects found under this email.")
        return
    
    print("\nYour Projects")
    for i in range(len(user_projects)):
        project = user_projects[i]
        print(f"{i+1}. {project['title']}")
    
    choice = int(input("Enter project number to delete: ")) - 1
    if 0 <= choice < len(user_projects):
        projects.remove(user_projects[choice])
        save_database(data)
        print("Project deleted successfully!")
    else:
        print("Invalid choice.")
