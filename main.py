from users.login import sign_in
from users.register import register
from projects.project import add_project, view_projects, edit_project, delete_project

if __name__ == "__main__":
    while True:
        print("\n1. Sign In\n2. Register\n3. View Projects\n4. Add Project\n5. Edit Project\n6. Delete Project\n7. Exit")
        option = input("Choose an option: ").strip()
        
        if option == "1":
            user = sign_in()
            if user:
                while True:
                    print("\n1. View Projects\n2. Add Project\n3. Edit Project\n4. Delete Project\n5. Sign Out")
                    sub_option = input("Choose an option: ").strip()
                    if sub_option == "1":
                        view_projects()
                    elif sub_option == "2":
                        add_project()
                    elif sub_option == "3":
                        edit_project()
                    elif sub_option == "4":
                        delete_project()
                    elif sub_option == "5":
                        break
                    else:
                        print("Invalid option, try again.")
        elif option == "2":
            user = register()
            if user:
                print("Registration successful!")
        elif option == "3":
            view_projects()
        elif option == "7":
            break
        else:
            print("Invalid option, try again.")
