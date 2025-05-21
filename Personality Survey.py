name = input("Name please: ")
gend = input("Are you a Male or Female? ")
favmov = input("what is your favorite movie "+ name + "? ")
favfood = input("What is your favorite food " + name + "? ")
favsport = input("What is your favorite sport " + name + "? ")
hobbs3 = input("What are your top 3 hobbies " +name+ "? ")
if gend == "Male" or gend == "male" or gend == "m" or gend == "M":
    print("\n" +name+ "'s favorite movie is " +favmov+ ", his favorite food is " +favfood+ ", plus he also likes " +favsport)
    if "." not in hobbs3:
        hobbs3 = hobbs3 + "."
    print("and his top 3 hobbies are " + hobbs3)
elif gend == "Female" or gend == "female" or gend == "f" or gend == "F":
    print("\n" +name+ "'s favorite movie is " +favmov+ ", her favorite food is " +favfood+ ", plus she also likes " +favsport)
    if "." not in hobbs3:
        hobbs3 = hobbs3 + "."
    print("and her top 3 hobbies are " + hobbs3)