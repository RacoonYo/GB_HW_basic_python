import os


def stat_size(folder_path=os.getcwd()):
    stat_for_size = {}

    for path, folders, files in os.walk(folder_path):
        # print(path, folders, files)
        for file in files:
            capacity = 10**len(str(os.stat(os.path.join(path, file)).st_size))
            if stat_for_size.get(capacity):
                stat_for_size[capacity] += 1
            else:
                stat_for_size[capacity] = 1

    print(stat_for_size)




if __name__ == '__main__':
    stat_size('files')