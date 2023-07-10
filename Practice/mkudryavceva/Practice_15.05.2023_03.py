import sys
import os
import hashlib
import ast
import argparse
# Возможно, здесь знак умножения нужно заменить на time.
from time import *


class shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []
# Я пока не поняла саму суть этого года, но в конце строки должно быть либо "os.walk()", либо "os.path.dirname()".
    for root, directories, files in os.walk(dirname):
        for file in files:
            if file[-3:] == '.mp3':
# Не совсем поняла какой элемент списка mp3s будет добавляться в конец, если элементов в списке пока нет.
                mp3s.append([root, file])
# В самом верху кода не указано "from pathlib import Path".
# И непонятно как связаны "mp3" и "mp3s", если "mp3s" является списком, то что такое "mp3"?
    for path, mp3 in mp3s:
        hashname = self.generateName() + '.mp3'
        self.map[hashname] = mp3
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
                mp3s.append({root, file})
    for path, hashname in mp3s:
# Второй закрывающей скобки быть не должно.
        os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
        os.remove(restore_path)

    def generateName(self, seed=time()):
        return hashlib.md5(str(seed)).hexdigest()

# Если "def" относиться к "class shuffler", то должно отступить 4 пробела.
def parse_arguments():
# Такое чувство, что в этом блоке либо нужно проставить if, else, либо переименовать функции.
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
# В коде используются либо одинарные, либо двойные скобки. Если их и смешивают, то для цитирования '"Какой-то фразы"'.
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

# Если это продолжение рабочего кода, то зачем здесь разделение в две строки?
def main():
    args = parse_arguments()
    Shuffler = shuffler()
    if args.subcommand == 'rename':
        if args.output:
            Shuffler.rename(args.dirname, 'restore.info')
        else:
            Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()

# Функция main() используется для разделения блоков кода в программе. Какой смысл от неё в конце кода?
main()
