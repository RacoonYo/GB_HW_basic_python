import sys
import os

with open(os.path.join('task_6_5', 'join_text_task_6_4.csv'), 'w') as f:
    f.write('')
f_hobby = open(os.path.join('task_6_5', 'hobby_1.csv'), 'r')
f_users = open(os.path.join('task_6_5', 'users_1.csv'), 'r')
f_join_text = open(os.path.join('task_6_5', 'join_text_task_6_4.csv'), 'a')

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