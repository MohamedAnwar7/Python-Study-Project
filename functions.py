def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Math', 'Sci']
info = {'name':'ahmed', 'age': 23}
student_info(*courses, **info)
