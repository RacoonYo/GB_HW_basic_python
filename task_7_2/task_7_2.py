import os
import yaml

root = os.getcwd()

try:
    with open('config.yaml') as f:
        folder_map = yaml.safe_load(f)
except OSError as e:
    print(f'OS say:{e}')
finally:
    f.close()

def make_dir(yaml_dict: dict, root=os.getcwd()):
    for key, value in yaml_dict.items():
        try:
            os.makedirs(os.path.join(root, key), exist_ok=True)
        except TypeError:
            print('Invalid type, please use only Type: string')

        for _ in value:
            if type(_) == dict:
                make_dir(_, os.path.join(root, key))
            else:
                if _.count('.'):
                    with open(os.path.join(root, key, _), 'w') as f:
                        pass
                else:
                    try:
                        os.makedirs(os.path.join(root, key, _), exist_ok=True)
                    except TypeError:
                        print('Invalid type, please use only Type: string')

if __name__=='__main__':
    make_dir(folder_map)