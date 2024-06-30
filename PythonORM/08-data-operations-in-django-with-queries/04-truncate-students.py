def truncate_students():
    all_students = Student.objects.all().delete()