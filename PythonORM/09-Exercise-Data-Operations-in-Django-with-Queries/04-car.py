def apply_discount() -> None:
    cars = Car.objects.all()

    for car in cars:
        percentage_off = sum(int(digit) for digit in str(car.year)) / 100  # 2014 => 2 + 0 + 1 + 4 => 7 / 100 => 0.07
        discount = float(car.price) * percentage_off  # 1000 * 0.07 => 70
        car.price_with_discount = float(car.price) - discount  # 1000 - 70 => 930
        car.save()


def get_recent_cars() -> QuerySet:
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car() -> None:
    Car.objects.last().delete()