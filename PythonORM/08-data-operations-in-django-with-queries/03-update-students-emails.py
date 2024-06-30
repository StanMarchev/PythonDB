def update_students_emails():
    all_students = Student.objects.all()
    for s in all_students:
        s.email = s.email.replace(s.email.split('@')[1], 'uni-students.com')
        s.save()
