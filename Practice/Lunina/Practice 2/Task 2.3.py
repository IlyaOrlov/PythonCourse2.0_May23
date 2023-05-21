import sys
import os
import hashlib
import ast
import argparse
from time import *


# CamelCase Название пишется с большой буквы правильно - Shuffler
class shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          #Здесь отступ 2 пробела - правильно по PEP 8 отступ- 4 пробела
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            # В конце двойная скобка.
            os.rename(path + '/' + mp3), path + '/' + hashname))
          # в конце строки поставить ";"
          f = open(output, 'r')
          f.write(str(self.map))

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:
            self.map = ast.literal_eval(f.read())
              #Ошибка ytn пробелов Правильно - 4
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':
                   # Ошибка больше 4 пробелов (5) Правильно - 4
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            # В конце двойная скобка. (os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None) -
            # переименовывает файл или директорию из src в dst )
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
            # функция библиотеки os.  удалить.  В скобках дословный перевод: восстановление части
            # возможная ошибка - название файла указано не в кавычках
        os.remove(restore_path)

    def generateName(self, seed=time()):
                #Ошибка -строчка далеко уехала. Правильно - нужно не более 4 пробелов
            # между return hashlib д.б. нижнее подчеркивание
          return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    Shuffler = shuffler()
    if args.subcommand == 'rename':
        # Ошибка больше 4 пробелов (6) Правильно - 4
          if args.output:
              # Ошибка больше 4 пробелов (6) Правильно - 4
                Shuffler.rename(args.dirname, 'restore.info')
          # Ошибка больше 4 пробелов (6) Правильно - 4
          else:
              # Ошибка больше 4 пробелов (6) Правильно - 4
                Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
