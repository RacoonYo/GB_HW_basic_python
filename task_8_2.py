import re

RE_PATTERN = re.compile(r'((?:\d+)(?:\.\d+){3}).*\[(.*)\]\s*\"(\w*)\s*(/\w*/\w*).* (\d+) (\d+)')


with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    try:
        text = f.readline()
        while text:
            print(RE_PATTERN.match(text).groups())
            assert text, f'pattern is not optimal'
            text = f.readline().strip()
    except Exception as e:
        print(e)
    finally:
        f.close()

