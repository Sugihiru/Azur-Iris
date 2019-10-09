import sys
import os


def main():
    os.chdir(sys.path[0])
    for filename in os.listdir('.'):
        if filename.endswith(".ui"):
            root_filename, ext = os.path.splitext(filename)
            output_filename = root_filename + ".py"
            ret = os.system(f"pyside2-uic {filename} -o {output_filename}")
            if ret != 0:
                return
            print(filename)


if __name__ == '__main__':
    main()
