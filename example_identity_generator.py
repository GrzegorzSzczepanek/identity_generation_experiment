import pprint

name = input("Jak masz na imię: ")
surname = input("Jak masz na nazwisko: ")
gender = input("Podaj swoją płeć: ")
hometown = input("Napisz jak nazywa się twoje miasto rodzinne: ")
month = input("Podaj miesiąc swojego urodzenia: ")
mothers_name = input("Podaj imię swojej matki: ")
fathers_name = input("Podaj imię swojego ojca: ")


male_names = list(filter(lambda x: (x != name and x != fathers_name), open("imiona_męskie.txt", "r").read().strip().split("\n")))
female_names = list(filter(lambda x: (x != name and x != mothers_name), open("imiona_żeńskie.txt", "r").read().strip().split("\n")))
hometowns = list(filter(lambda x: (x != hometown), open("miasta_rodzinne.txt", "r").read().strip().split("\n")))
surnames = list(filter(lambda x: (x != surname), open("nazwiska.txt", "r").read().strip().split("\n")))
months = list(filter(lambda x: (x != month), open("miesiące.txt", "r").read().strip().split("\n")))


def create_celebrity_identity(name: str, surname: str, gender: str, hometown: str, month: str, mothers_name: str, fathers_name: str) -> dict:
    celebrities = [x.split(", ") for x in open('celebryci.txt', "r").read().split("\n")]
    filtered_celebrities = []
    
    # Getting rid of celebrities that have user data
    for celebrity in celebrities:
        if not (name in celebrity or
                surname in celebrity or
                gender in celebrity or
                hometown in celebrity or
                month in celebrity or
                mothers_name in celebrity or
                fathers_name in celebrity):
            filtered_celebrities.append(celebrity)
        
    keys = ["name", "surname", "month", "mothers_name", "fathers_name", "hometown"]
    celebrity_identity = filtered_celebrities[0]
    celebrity_identity = dict(zip(keys, celebrity_identity))

    return celebrity_identity



def create_unknown_person_indentity() -> dict:

    unknown_identity = {
        "name": male_names[0] if gender == "męska" else female_names[0],
        "surname": surnames[0],
        "hometown": hometowns[0],
        "mothers_name": female_names[0] if gender == "męska" else female_names[1],
        "fathers_name": male_names[0] if gender == "żeńska" else male_names[1],
        "month": months[0],
    }

    return unknown_identity


celebrity_identity = create_celebrity_identity(name,
                                               surname,
                                               gender,
                                               hometown,
                                               month,
                                               mothers_name,
                                               fathers_name)


male_names = list(filter(lambda x: x != celebrity_identity['name'] and x != celebrity_identity['fathers_name'] , male_names))
hometowns = list(filter(lambda x: x != celebrity_identity['hometown'], hometowns))
surnames = list(filter(lambda x: x != celebrity_identity['surname'], surnames))
female_names = list(filter(lambda x: x != celebrity_identity['name'] and x != celebrity_identity['mothers_name'], female_names))
months = list(filter(lambda x: x != celebrity_identity['month'], months))
hometowns = list(filter(lambda x: x != celebrity_identity.get('hometown', ''), hometowns))

unknown_identity = create_unknown_person_indentity()

male_names = list(filter(lambda x: x != unknown_identity['name'] and x != unknown_identity['fathers_name'], male_names))
hometowns = list(filter(lambda x: x != unknown_identity['hometown'], hometowns))
surnames = list(filter(lambda x: x != unknown_identity['surname'], surnames))
female_names = list(filter(lambda x: x != unknown_identity['name'] and x != unknown_identity['mothers_name'], female_names))
months = list(filter(lambda x: x != unknown_identity['month'], months))

print("\n###### Tożsamość Celebryty ######" )
pprint.pprint(celebrity_identity)
print("\n###### Tożsamość Nieznanej Osoby ######" )
pprint.pprint(unknown_identity, indent=1)

def create_fake_indetity() -> dict:
    fake_identity = {
            'name': male_names[0] if gender == "męska" else female_names[0],
            'surname': surnames[0],
            'hometown': hometowns[0],
            'mothers_name': female_names[1],
            'fathers_name': male_names[1],
            'month': months[0]
        }
    return fake_identity


# print(male_names, female_names, hometowns, surnames)
fake_identity = create_fake_indetity()
print("\n###### Fałszywa tożsamość ######" )
pprint.pprint(fake_identity)
