def get_students_info():
    result = []
    all_students = Student.objects.all()

    for student in all_students:
        result.append(f'Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}')
    return '\n'.join(result)