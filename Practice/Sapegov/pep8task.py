import sys
import os
import hashlib
import ast
import argparse
from time import *     # на данном уровне не могу определить какие библиотеки стандартные, а какие сторонние


class Shuffler:      # класс должен быть CamelCase

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = []                                                  # 2 лишних пробела
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))  # 2 лишних скобки после hashname
          f = open(output, 'r')                                   # нужно добавить 2 пробела
          f.write(str(self.map))                                  # нужно добавить 2 пробела

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:                     # 2 лишних пробела
            self.map = ast.literal_eval(f.read())            # нужно добавить 2 пробела
          mp3s = []                                          # 2 лишних пробела (либо добавить 2. не очень понял)
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':                       # нужно добавить пробел
                    mp3s.append({root, file})                # лишний пробел
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])) # 1 лишняя скобка после hashname
        os.remove(restore_path)                              # нужно добавить 4 пробела
                
     def generateName(self, seed=time()):                    # лишний пробел + функция должна быть def generate_name
          return hashlib.md5(str(seed)).hexdigest()          # лишний пробел


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

def main():                                           # должно быть 2 пустых строчки
    args = parse_arguments()
    Shuffler = shuffler()
    if args.subcommand == 'rename':
          if args.output:                                            # 2 лишних пробела
                Shuffler.rename(args.dirname, 'restore.info')        # 2 лишних пробела
          else:                                                      # 2 лишних пробела
                Shuffler.rename(args.dirname, args.output)           # 2 лишних пробела
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
