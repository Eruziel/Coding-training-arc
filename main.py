# app for administrating a dance school, need a list for instructors, a list of classes, can be led by multiple instructors, students can sign up for any class


# functionality that checks for classes, teachers, dates

# class capacity check
print(
    "Welcome to the dance app, here is a list of our available classes, please select which number you would like to attend:"
)
# show all available classes

instructors = ["Adi", "Badi", "Jadi", "Gadi"]

styles = ["popping", "cwalk", "hiphop", "breakdance"]

classes_with_instructors = set(
    [("popping", "Adi"), ("popping", "Badi"), ("cwalk", "Jadi"), ("cwalk", "Gadi"), ("popping", "Gadi") ]
)
formatted_styles = "\n".join(
    [f"{i}: {style.title()}" for i, style in enumerate(styles, start=1)]
)
print(formatted_styles)

# asking user for class input


while True:
    print("Which class would you like to sign up for?")
    class_choice = input()

    if not class_choice.isdigit():  # guardian approach example
        print("Invalid input, please choose a class number!")
        continue

    selected_class = styles[int(class_choice) - 1]
    break

class_instructors = [
    instructor
    for style, instructor in classes_with_instructors
    if style == selected_class
]
print(f"Thank you for choosing class {selected_class} with {", ".join(class_instructors[:-1])} and {class_instructors[-1]} !")

