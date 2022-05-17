DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():

    #LIST COMPREHENSIONS
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    for worker in all_python_devs:
        print(worker)

    for workerplatzi in all_platzi_workers:
        print(workerplatzi)    

    #-------------------------------------------------------------------------
    print()
    print("High order Functions")

    #high order functions
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))

    print()
    for worker in adults:
        print(worker)

    #le concatena la key old y su valor si es True or false,  | concatena la key al diccionario existente
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    #  + suma una lista a otra
    #  | suma diccionario en otro

    print()

    for worker in old_people:
        print(worker)

    ## ------------------challlenge------------------------------------------------------------

    #challenge with high order functions---------------

    print()
    print("-------------CHALLENGE------------")

    all_python_devs_2 = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs_2 = list(map(lambda worker: worker["name"], all_python_devs_2))
    for worker in all_python_devs_2:
        print(worker)

    print()

    all_platzi_workers__2 = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers__2 = list(map(lambda worker: worker["name"], all_platzi_workers__2))
    for worker in all_platzi_workers__2:
        print(worker)

    #callege with list comprenhesion------------------
    #LIST COMPREHENSIONS
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    for worker in all_python_devs:
        print(worker)

    for workerplatzi in all_platzi_workers:
        print(workerplatzi)    

    #-------------------------------------------------------------------------
    print()
    print("High order Functions")

    #high order functions
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    #le concatena la key old y su valor si es True or false,  | concatena la key al diccionario existente
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))



    adults_2 = [worker["name"] for worker in DATA  if worker["age"] > 18]
    for worker in adults_2:
        print(worker)
    
    print()

    old_people_2 = [worker | {"old": worker["age"]> 70 }for worker in DATA ]
    for worker in old_people_2:
        print(worker)


if __name__ == '__main__':
    run()