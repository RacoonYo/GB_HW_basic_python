import sys
import os
from itertools import zip_longest
import json


with open(os.path.join('task_6_5', 'hobby_2.csv'), 'r', encoding='UTF-8') as f:
    hobby = f.read().split('\n')
    hobby.pop()

with open(os.path.join('task_6_5', 'users_1.csv'), 'r', encoding='UTF-8') as f:
    users = f.read().split('\n')
    users.pop()

if len(hobby) > len(users):
    sys.exit(1)

desired_dict = {key: value for key, value in zip_longest(users, hobby)}

with open(os.path.join('task_6_5', 'dict_task_6_3.json'), 'w', encoding='UTF-8') as f:
    json.dump(desired_dict, f)

with open(os.path.join('task_6_5', 'dict_task_6_3.json'), 'r', encoding='UTF-8') as f:
    print(json.load(f))