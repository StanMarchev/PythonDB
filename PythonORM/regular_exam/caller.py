import os
import django
from django.db.models.functions import Coalesce

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Q, Count, Sum, Avg, F
from main_app.models import Astronaut, Mission, Spacecraft


def get_astronauts(search_string=None):
    if search_string is None:
        return ""

    if search_string == "":
        search_string = " "


    query = Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)
    matching_astronauts = Astronaut.objects.filter(query).order_by('name')

    result = "\n".join(
        f"Astronaut: {astronaut.name}, phone number: {astronaut.phone_number}, status: {'Active' if astronaut.is_active else 'Inactive'}"
        for astronaut in matching_astronauts
    )

    return result



def get_top_astronaut():

    astronauts_with_mission_counts = Astronaut.objects.annotate(
        num_of_missions=Count('missions')
    ).order_by('-num_of_missions', 'phone_number')


    if not astronauts_with_mission_counts.exists():
        return "No data."


    top_astronaut = astronauts_with_mission_counts.first()
    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.num_of_missions} missions."

def get_top_commander():

    astronauts_with_command_counts = Astronaut.objects.annotate(
        num_of_commanded_missions=Count('commanded_missions')
    ).order_by('-num_of_commanded_missions', 'phone_number')


    if not astronauts_with_command_counts.exists() or astronauts_with_command_counts.first().num_of_commanded_missions == 0:
        return "No data."


    top_commander = astronauts_with_command_counts.first()
    return f"Top Commander: {top_commander.name} with {top_commander.num_of_commanded_missions} commanded missions."


def get_last_completed_mission():
    last_completed_mission = Mission.objects.filter(status='Completed').order_by('-launch_date').first()

    if not last_completed_mission:
        return "No data."

    commander_name = last_completed_mission.commander.name if last_completed_mission.commander else "TBA"

    astronaut_names = last_completed_mission.astronauts.order_by('name').values_list('name', flat=True)
    astronauts_str = ", ".join(astronaut_names)
    total_spacewalks = last_completed_mission.astronauts.aggregate(
        total_spacewalks=Sum('spacewalks')
    )['total_spacewalks'] or 0

    result = (
        f"The last completed mission is: {last_completed_mission.name}. "
        f"Commander: {commander_name}. Astronauts: {astronauts_str}. "
        f"Spacecraft: {last_completed_mission.spacecraft.name}. Total spacewalks: {total_spacewalks}."
    )

    return result


def get_most_used_spacecraft():

    most_used_spacecraft = Spacecraft.objects.annotate(
        num_missions=Count('missions')
    ).order_by('-num_missions', 'name').first()

    if not most_used_spacecraft:
        return "No data."

    num_astronauts = Astronaut.objects.filter(
        missions__spacecraft=most_used_spacecraft
    ).distinct().count()

    result = (
        f"The most used spacecraft is: {most_used_spacecraft.name}, manufactured by {most_used_spacecraft.manufacturer}, "
        f"used in {most_used_spacecraft.num_missions} missions, astronauts on missions: {num_astronauts}."
    )

    return result


def decrease_spacecrafts_weight():
    planned_spacecrafts = Spacecraft.objects.filter(
        missions__status='Planned'
    ).distinct()

    affected_spacecrafts = []

    for spacecraft in planned_spacecrafts:
        if spacecraft.weight >= 200.0:
            spacecraft.weight -= 200.0
            spacecraft.save()
            affected_spacecrafts.append(spacecraft)

    if not affected_spacecrafts:
        return "No changes in weight."

    avg_weight = Spacecraft.objects.aggregate(
        avg_weight=Avg('weight')
    )['avg_weight']

    result = (
        f"The weight of {len(affected_spacecrafts)} spacecrafts has been decreased. "
        f"The new average weight of all spacecrafts is {avg_weight:.1f}kg"
    )

    return result
