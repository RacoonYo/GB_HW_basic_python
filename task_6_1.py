with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    data = f.read()

_ = data.split('\n')
print(_)
_ = [i.split(' ') for i in _ if i]
desired_list = [(i[0], i[5][1:], i[6]) for i in _]

print(desired_list)





