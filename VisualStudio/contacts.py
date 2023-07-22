"""
contacts = {
    "number":4,
    "students":
        [
            {"name":"Sarah Holderness", "email":"sarah@example.com"},
            {"name":"Harry Potter", "email":"harry@example.com"},
            {"name":"Hermione Granger", "email":"hermione@example.com"},
            {"name":"Ron Weasley", "email":"ron@example.com"}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])# print(p['name'])

"""

contacts = {
    'number': 5,
    'students':
        [
            {"name":"Sarah Holderness", "email":"sarah@example.com"},
            {"name":"Harry Potter", "email":"harry@example.com"},
            {"name":"Hermione Granger", "email":"hermione@example.com"},
            {"name":"Ron Weasley", "email":"ron@example.com"},
            {'name':"Regina Phalangie", "email":"regina@example.com"}
        ]
}

print('student emails:')
for student in contacts['students']: #name of loop variable
    print(student['email'])
