
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
            print("Error!!")
            main()
        lessons(3,3,4,4, geometry, 0, 0, 0, 0, 0)


    elif entery == "Science":
        biology = float(input("Enter the grade of the biology course: ")) * 3
        if biology/3 > 20 :
            print("Error!!")
            main()
        lessons(3,3,4,3, biology, 0, 0, 0, 0, 0)


    elif entery == "Humanities":
        history = float(input("Enter the grade of the history course: ")) * 3
        mathematics_and_statistics = float(input("Enter the grade of the Mathematics and statistics course: ")) * 3
        economy = float(input("Enter the grade of the economy course: ")) * 2
        literary_sciences_and_techniques = float(input("Enter the grade of the literary sciences and techniques course: ")) * 2
        sociology = float(input("Enter the grade of the sociology course: ")) * 2
        logic = float(input("Enter the grade of the logic course: ")) * 2
        if history/3 or sociology/2 or logic/2 or literary_sciences_and_techniques/2 or economy/2 or mathematics_and_statistics/3> 20:
            print("Error!!")
            main()

        lessons(0,3,0,0 ,history, mathematics_and_statistics, economy, sociology, literary_sciences_and_techniques, logic)

    else:
        print("Error!!")
        main()


def lessons(chn, rn, mn, phn, l1, l2, l3, l4, l5, l6 ):

    math = float(input("Enter the grade of the math course: ")) * mn
    chemistry = float(input("Enter the grade of the chemistry course: ")) * chn
    religious = float(input("Enter the grade of the religious course: ")) * rn
    physics = float(input("Enter the grade of the physics course: ")) * phn
    farsi = float(input("Enter the grade of the farsi course: ")) * 2
    arabic = float(input("Enter the grade of the arabic course: ")) * 2
    essay = float(input("Enter the grade of the essay course: ")) * 2
    physical_education = float(input("Enter the grade of the P.E course: ")) * 2
    science = float(input("Enter the grade of the science course: ")) * 2
    discipline = float(input("Enter the grade of the discipline: ")) * 2
    media_literacy = float(input("Enter the grade of the medialiteracy course: ")) * 2
    english_language = float(input("Enter the grade of the english course: ")) * 3
    defense_readiness = float(input("Enter the grade of the defense readiness course: ")) * 3
    geography = float(input("Enter the grade of the geography course: ")) * 2

    final_GPA  = l1 + l2 + l3 + l4 + l5 + l6 + math + chemistry + religious + physics + farsi + arabic + physical_education + science + discipline + media_literacy + english_language + defense_readiness + geography
    print(f"Your final GPA grade is: {final_GPA / 37}")


main()
