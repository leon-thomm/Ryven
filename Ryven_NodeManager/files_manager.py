import os


def save_file(file_path, content):
    try:
        os.remove(file_path)
    except OSError:
        pass

    f = open(file_path, 'w')
    f.write(content)
    f.close()