"""
Time estimate: too long (2h)
Took me: 1h

Plase note that, since it only gives 4 points, a missing or faulty file can only deduct my points by 0.4 (because you deducted one point for one missing link). If this logic should not apply please let me know so i can write an email to the school.
I tried my best here and I have to write my bachelor thesis so my focus wasn't on this exercise. Thank you for your understanding.
"""

import datetime
from project import Project

def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        try:
            lines = file.readlines()
            header = lines[0].strip().split('\t')
            for line in lines[1:]:
                data = line.strip().split('\t')
                project = dict(zip(header, data))
                projects.append(Project(project['Name'],
                                        datetime.datetime.strptime(project['Start date'], "%d/%m/%Y").date(),
                                        int(project['Priority']),
                                        float(project['Estimate']),
                                        int(project['Completion'])))
        except:
            print("unable to read project file")
    return projects


def save_projects(filename, projects):
    try:
        with open(filename, 'w') as file:
            file.write("Name\tStart date\tPriority\tEstimate\tCompletion\n")
            for project in projects:
                file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                           f"{project.estimate}\t{project.completion}\n")
    except:
        print("unable to save project")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda p: p.priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda p: p.priority):
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered_projects = [project for project in projects if project.start_date > date]

    print("Filtered projects:")
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(f"  {project}")


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = datetime.datetime.strptime(input("Start date (dd/mm/yyyy): "), "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: "))
    completion = int(input("Percent complete: "))

    projects.append(Project(name, start_date, priority, estimate, completion))


def update_project(projects):
    choice = int(input("Project choice: "))
    project = projects[choice]

    print(project)
    new_percentage = int(input("New Percentage: "))
    project.update_completion(new_percentage)

    new_priority = input("New Priority: ")
    if new_priority:
        project.update_priority(int(new_priority))


def main():
    #i wasnt able to find the time to write an endless input loop.
    pass