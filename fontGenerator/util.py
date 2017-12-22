import base64, os

def get_content(texts):

    if isinstance(texts, str) or isinstance(texts, unicode):
        file_path = texts
        with open(file_path, 'r') as f:
            result = list(f.read().decode("utf-8"))
            f.close()
            return result
    else:
      return texts

def write_file( path, data ):
    with open( path, "w" ) as f:
        f.write(data)
        f.close()

def read_by_base64(path):
    with open(path, "r") as f:
        data = f.read()
        f.close()
    return base64.b64encode(data)


def delete_file(path):
    os.remove(path)

def delete_files(paths):
    for path in paths:
        delete_file(path)

