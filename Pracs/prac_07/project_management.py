"""CP1404/CP5632 Practical project management"""
from Pracs.prac_07.project import Project

MENU = "- (L)oad projects \n" \
       "- (S)ave projects \n" \
       "- (D)isplay Projects \n" \
       "- (F)ilter objects \n" \
       "- (A)dd new project \n" \
       "- (U)pdate project \n" \
       "- (Q)uit"

FILENAME = "projects.txt"


def main():
    """Project manager."""
    projects = get_data(FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("L")
        elif choice == "S":
            print("S")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            print("F")
        elif choice == "A":
            print("A")
        elif choice == "U":
            print("U")
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def get_data(filename):
    """Get data from file formatted like 'Name	Start Date	Priority	Cost Estimate	Completion Percentage'."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def display_projects(projects):
    """Display projects from the projects list"""
    print("Incomplete projects:")
    for project in projects:
        if project.is_complete():
            print(f"  {project}")
    print("Complete projects:")
    for project in projects:
        if not project.is_complete():
            print(f"  {project}")


if __name__ == '__main__':
    main()
