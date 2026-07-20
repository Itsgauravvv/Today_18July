def employee_skills(emp_id, emp_name, skills):
    print(f"Employee ID: {emp_id}")
    print(f"Employee Name: {emp_name}")
    print(f"Skills: {skills}")

def add_skill(skills):
    skill = input("Enter skill to add: ")
    skills.append(skill)
    print("Skill added successfully!")

def remove_skill(skills):
    skill = input("Enter skill to remove: ")

    if skill in skills:
        skills.remove(skill)
        print("Skill removed successfully!")
    else:
        print("Skill not found!")

def update_skill(skills):
    old_skill = input("Enter skill to update: ")

    if old_skill in skills:
        new_skill = input("Enter new skill: ")
        index = skills.index(old_skill)
        skills[index] = new_skill
        print("Skill updated successfully!")
    else:
        print("Skill not found!")


def insert_skill(skills):
    pos = int(input("Enter position: "))
    skill = input("Enter skill to insert: ")

    skills.insert(pos, skill)
    print("Skill inserted successfully!")

def search_skill(skills):
    s = input("Enter skill to search: ")

    if s in skills:
        print("Skill found!")
    else:
        print("Skill not found!")

def count_skill(skills):
    print("Total skills =", len(skills))
    
def sort_skill(skills):
    skills.sort()
    print("Skills sorted successfully!")
    print(skills)

def reverse_skill(skills):
    skills.reverse()
    print("Skills reversed successfully!")
    print(skills)

def copy_skills(skills):
    copied_skills = skills.copy()
    print("Copied Skills:", copied_skills)

def clear_skills(skills):
    skills.clear()
    print("All skills have been removed.")
    
def display_skills_by_enumerate(skills):
    print("Skills with their indices:")
    for index, skill in enumerate(skills, start =1):
        print(f"{index} - {skill}")

emp_id = int(input("Enter Employee ID: "))
emp_name = input("Enter Employee Name: ")
skills = []
for s in skills:
    skills.append(input("Enter skill: "))

while True:

    print("\n========== Employee management ==========")
    print("1. Display Skills")
    print("2. Add Skill")
    print("3. Remove Skill")
    print("4. Update Skill")
    print("5. Insert Skill")
    print("6. Search Skill")
    print("7. Count Skills")
    print("8. Sort Skills")
    print("9. Reverse Skills")
    print("10. Copy Skills")
    print("11. Clear Skills")
    print("12. Display skills by enumerate")
    print("13. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        employee_skills(emp_id, emp_name, skills)
    elif choice == 2:
        add_skill(skills)
    elif choice == 3:
        remove_skill(skills)
    elif choice == 4:
        update_skill(skills)
    elif choice == 5:
        insert_skill(skills)
    elif choice == 6:
        search_skill(skills)
    elif choice == 7:
        count_skill(skills)
    elif choice == 8:
        sort_skill(skills)
    elif choice == 9:
        reverse_skill(skills)
    elif choice == 10:
        copy_skills(skills)
    elif choice == 11:
        clear_skills(skills)
    elif choice == 12:
        display_skills_by_enumerate(skills)
    elif choice == 13:
        break

    else:
        print("Invalid Choice!")