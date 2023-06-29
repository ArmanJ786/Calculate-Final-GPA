
'''
This project was created by Arman Jabari on June 29, 2023
This project is basic and simple and is made without any Python libraries or frameworks
Copyright(C) 2023
'''

def main():
    print("[Mathematic - Science - Humanities]")
    entery = input("Enter your field of study? ").lower().capitalize()

    if entery == "Mathematic":
        geometry = float(input("Enter the grade of the geometry course: ")) * 2
        if geometry/2 > 20:
            print("Login Error:\nYou must enter a valid numeric value.\n")
            main()

        lessons(3,3,4,4, geometry)


    elif entery == "Science":
        biology = float(input("Enter the grade of the biology course: ")) * 3
        if biology/3 > 20 :
            print("Login Error:\nYou must enter a valid numeric value.\n")
            main()

        lessons(3,3,4,3, biology)


    elif entery == "Humanities":
        l1 = lesson('history', 'mathematics and statistics', 3, 3)
        l2 = lesson('economy', 'literary sciences and techniques', 2, 2)
        l3 = lesson('sociology', 'logic', 2, 2)

        if l1/6 or l2/4 or l3/4 > 20:
            print("Login Error:\nYou must enter a valid numeric value.\n")
            main()

        SCH = l1 + l2 + l3
        lessons(0,3,0,0 ,SCH)

    else:
        print("Please enter your field of study.\n")
        main()

def lesson(name, name2, Coefficient, Coefficient2):
    try:
        lesson = float(input(f"Enter the grade of the {name} course: ")) * Coefficient
        lesson2 = float(input(f"Enter the grade of the {name2} course: ")) * Coefficient2
        return lesson + lesson2
    except ValueError:
        print("Login Error:\nYou must enter a valid numeric value.\n")
        main()


def lessons(chn, rn, mn, phn, Specialized_courses):

    l1 = lesson('math', 'chemistry', mn, chn)
    l2 = lesson('religious', 'physics', rn, phn)
    l3 = lesson('literature', 'arabic', 2, 2)
    l4 = lesson('essay', 'P.E', 2, 2)
    l5 = lesson('science', 'discipline', 2, 2)
    l6 = lesson('media literacy', 'english', 2, 3)
    l7 = lesson('defense readiness', 'geography', 3, 2)


    final_GPA  = Specialized_courses + l1 + l2 + l3 + l4 + l5 + l6 + l7
    if final_GPA / 37 <= 20:
        print(f"Your final GPA grade is: {final_GPA / 37}")
    else:
        print("Output error:\nThe value of your GPA number is greater than the specified range.\n")
        main()


main()
