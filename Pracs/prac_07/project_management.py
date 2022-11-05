"""CP1404/CP5632 Practical project management"""
from Pracs.prac_07.project import Project
import datetime

MENU = "- (L)oad projects \n" \
       "- (S)ave projects \n" \
       "- (D)isplay Projects \n" \
       "- (F)ilter objects \n" \
       "- (A)dd new project \n" \
       "- (U)pdate project \n" \
       "- (Q)uit"

FILENAME = "projects.txt"
NAME_INDEX = 0
START_DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_INDEX = 3
PERCENTAGE_INDEX = 4


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
            add_project(projects)
        elif choice == "U":
            update_project(projects)
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
            project = Project(parts[NAME_INDEX], parts[START_DATE_INDEX], int(parts[PRIORITY_INDEX]),
                              float(parts[COST_INDEX]), int(parts[PERCENTAGE_INDEX]))
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


def update_project(projects):
    """Update project in list with new percentage and new priority."""
    for i, project in enumerate(projects):
        print(i, project)
    index = int(input("Project choice: "))
    print(projects[index])
    new_percentage = int(input("New percentage: "))
    new_priority = int(input("New priority: "))
    projects[index] = Project(projects[index].name, projects[index].start_date, new_priority, projects[index].cost,
                              new_percentage)
    return projects


def add_project(projects):
    """Add a new project to the projects list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: "))
    percentage = int(input("Percentage complete: "))
    new_project = Project(name, start_date, priority, cost, percentage)
    projects.append(new_project)
    return projects


if __name__ == '__main__':
    main()
