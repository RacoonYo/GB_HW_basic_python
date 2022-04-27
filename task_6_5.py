import sys
import os

with open(os.path.join('task_6_5', sys.argv[3]), 'w') as f:
    f.write('')
f_hobby = open(os.path.join('task_6_5', sys.argv[2]), 'r')
f_users = open(os.path.join('task_6_5', sys.argv[1]), 'r')
f_join_text = open(os.path.join('task_6_5', sys.argv[3]), 'a')

users = f_users.readline()
hobby = f_hobby.readline()
while users:
    if not hobby:
        hobby = 'None \n'
    f_join_text.write(f'{users[:-1]}: {hobby}')
    users = f_users.readline()
    hobby = f_hobby.readline()

if hobby:
    sys.exit(1)

f_users.close()
f_hobby.close()
f_join_text.close()
