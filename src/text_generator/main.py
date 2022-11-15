import os

# создает кортеж из всех файлов директории data
filename_tuple = ()
for filename in os.listdir("../data"):
    filename_tuple += ((filename), )

# выводим все файлы в список
for filename in filename_tuple:
    print(filename)

