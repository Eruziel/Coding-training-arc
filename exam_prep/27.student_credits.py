def students_credits(*args):
    courses = {}
    result = ''
    total_credits = 0
    for i in args:
        course_name, given_credits, max_points, points = i.split('-')
        diyan_credits = (int(points) / int(max_points)) * int(given_credits)
        total_credits += diyan_credits
        courses[course_name] = diyan_credits

    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result += f'Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n'

    sorted_courses = sorted(courses.items(), key=lambda kvp: -kvp[1])

    for key, value in sorted_courses:
        result += f"{key} - {value:.1f}\n"

    return result


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
