def show_all_locations() -> str:
    locations = Location.objects.all().order_by('-id')

    return "\n".join(str(l) for l in locations)


def new_capital() -> None:
    # Location.objects.filter(id=1).update(is_capital=True)

    location = Location.objects.first()  # SELECT * FROM locations LIMIT 1
    location.is_capital = True
    location.save()


def get_capitals() -> QuerySet:
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location() -> None:
    Location.objects.first().delete()