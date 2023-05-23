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
        # Здесь 6 пробелов - по PEP8 отступ- 4 пробела. 2 удалить. Пробелы выставляются относительно верхней строки
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            # Убрать в конце двойную и в середине закрывающую скобки. + Убрав их РС все ещё подчеркивает конец строки. +ошибка - лишние 2 пробела в начале строки
            os.rename(path + '/' + mp3), path + '/' + hashname))
          f = open(output, 'r')
          f.write(str(self.map))

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:
            self.map = ast.literal_eval(f.read())
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':
                   # Один пробел лишний
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            # Последняя скобка лишняя
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
            #  отступ 4 пробела должны быть относительно "for"
        os.remove(restore_path)

        # лишний пробел
     def generateName(self, seed=time()):
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
    # Имя Класса CamelCase
    Shuffler = shuffler()
    if args.subcommand == 'rename':
          if args.output:
              # Удалить 2 лиших пробела
                Shuffler.rename(args.dirname, 'restore.info')
          else:
              # Удалить 2 лиших пробела
                Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
