from main_app.models import  Pet


def create_pet(name: str, species:str) ->str :
    pet = Pet.objects.create(
        name=name,
        species=species,
    )

    return f"{pet.name} is a very cute {pet.species}!"
