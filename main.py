"""
Honor Roll Checker

Author: Patrick Kelley

This program determines whether students qualify for the Honor Roll or Dean's List based on their GPA.

"""
HONOR_ROLL_VALUE = 3.25
DEAN_LIST_VALUE = 3.5


def main():
    """

    Prompt user for first name, last name, and student GPA. Then compares the GPA
    to Honor Roll and Dean's List values. Prints a message indicating student achievement.

    """

    last_name = input("Enter a student's last name. (Or ZZZ to quit)\n")
    while last_name != "ZZZ":
        first_name = input("Enter student's first name.\n")
        gpa = get_and_validate_gpa()
        if gpa >= DEAN_LIST_VALUE:
            print(f"{last_name}, {first_name} has made the Dean's List")
        elif HONOR_ROLL_VALUE <= gpa < DEAN_LIST_VALUE:
            print(f"{last_name}, {first_name} has made the Honor Roll")
        else:
            print(f"{last_name}, {first_name} did not make the Honor Roll")
        last_name = input("Enter another last name to continue. (Or ZZZ to quit)\n")
    else:
        input("Press Enter to close the program.\n")


def get_and_validate_gpa():
    """
    Prompts user for student's GPA and validates that it is a float greater than 0.

    :return:
        Float: The validated GPA provided by the user.

    """
    while True:
        try:
            gpa = float(input("Enter the student's GPA.\n"))
            if gpa > 0:
                return gpa
            else:
                print("GPA must be greater than 0.")
        except:
            print("GPA must be a number.")


if __name__ == "__main__":
    main()
