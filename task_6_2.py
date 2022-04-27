full_ip = []
users_ip = []
user_dict = {}

# Вариант решения №1
with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    data = f.readline()
    while data:
        full_ip.append(data[: data.find(' ')])
        data = f.readline()

users_ip = [*set(full_ip)]
number_of_requests = [full_ip.count(i) for i in users_ip]
spammer_is = users_ip[number_of_requests.index(max(number_of_requests))]

print(f'spammer: {spammer_is}')

# Вариант решения №2
with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    data = f.readline()
    while data:
        if user_dict.get(data[: data.find(' ')]):
            user_dict[data[: data.find(' ')]] += 1
        else:
            user_dict[data[: data.find(' ')]] = 1
        data = f.readline()
inv_user_dict = {value: kay for kay, value in user_dict.items()}

spammer_is = inv_user_dict[max(inv_user_dict.keys())]

print(f'spammer: {spammer_is}')

