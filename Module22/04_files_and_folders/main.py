import os


def find_file(current_path, data):
    for element in os.listdir(current_path):
        path = os.path.join(current_path, element)
        if os.path.isfile(path):
            data['files_amt'] += 1
            data['files_volume'] += os.path.getsize(path)
        elif os.path.isdir(path):
            data['dirs_amt'] += 1
            find_file(path, data)


statistics = {'dirs_amt': 0, 'files_amt': 0, 'files_volume': 0}
user_path = os.path.join('..', '..', 'Module14')
find_file(user_path, statistics)

size = statistics['files_volume'] / 1024
subdirs_amt = statistics['dirs_amt']
files_amt = statistics['files_amt']

print()
print('Размер каталога (в Кб):', size)
print('Количество подкаталогов:', subdirs_amt)
print('Количество файлов:', files_amt)
