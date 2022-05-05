import os
from shutil import copytree


def assembly_templates(scan_folder_path=os.getcwd(), root_path=os.getcwd()):
    templates_path = []

    if not os.path.exists(scan_folder_path):
        print('directory not found')
        exit(1)
    try:
        for i in os.walk(scan_folder_path):
            if i[1] == ['templates']:
                templates_path.append(os.path.join(i[0], 'templates'))
    except TypeError:
        print('Use only string')
        exit(2)

    all_templates_path = os.path.join(root_path, 'templates')

    try:
        os.makedirs(all_templates_path, exist_ok=True)
    except TypeError:
        print('Use only string')
        exit(2)

    for path in templates_path:
        copytree(path, all_templates_path, dirs_exist_ok=True)


if __name__ == '__main__':
    assembly_templates('my_project','my_project')

