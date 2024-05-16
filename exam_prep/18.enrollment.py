def gather_credits(credits_needed, *args):
    courses = []
    current_credits = 0
    result = ''
    for name, credits_given in args:
        if current_credits < credits_needed:
            if name not in courses:
                courses.append(name)
                current_credits += credits_given
        else:
            break

    if current_credits >= credits_needed:
        result += f"Enrollment finished! Maximum credits: {current_credits}.\nCourses: {', '.join(c for c in sorted(courses))}"
    else:
        result += f"You need to enroll in more courses! You have to gather {credits_needed - current_credits} credits more."

    return result


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
