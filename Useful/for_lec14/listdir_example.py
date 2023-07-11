import os

#os.makedirs('mydirectory/mydirectory')
def show_dir(cur_dir):
    for i in os.listdir(cur_dir):
        path = os.path.join(cur_dir, i)
        print(path)
        if os.path.isfile(path):
            print(f"Файл: {i}")
        else:
            print(f"Папка: {i}")
            show_dir(path)

show_dir('.')
# show_dir(r"C:\Users\Stmadm\Documents\Python\PythonCourseForKursia3\PythonCourse2.0_May23\Useful\for_lec14")

# for i in os.walk('.'):
#     print(i)

# t = 'mydirectory'
# f = 'композиция_vs_наследование.txt'
# with open(os.path.join(t, f), 'w'):
#     pass



