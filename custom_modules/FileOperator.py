import os
from custom_modules.FileValidator import fileExists, isFile
from custom_modules.TypeTester import arg_is_a_list as aial, arg_is_none
from custom_modules.Utils import flatten_dict as fd


def delete_file(file_path):
    if fileExists(file_path) and isFile(file_path):
        os.remove(file_path)
        return not fileExists(file_path)


def append_file(file_path, list_data):
    if aial(list_data):
        file_exists = fileExists(file_path)
        is_file = isFile(file_path)

        if file_exists and is_file:
            deleted = delete_file(file_path)

            if deleted:
                with open(file_path, "a", 2) as f:
                    for d in list_data:
                        f.write(d)

                return fileExists(file_path)
        else:
            with open(file_path, "a", 2) as f:
                for d in list_data:
                    f.write(d)

            return fileExists(file_path)
    return None


def write_dataframe_to_file(file_path, _data):
    if fileExists(file_path):
        deleted = delete_file(file_path)

        if deleted:
            _data.to_csv(file_path)

        return fileExists(file_path)
    else:
        _data.to_csv(file_path)
        return fileExists(file_path)


def write_to_file(file_path, _data):
    _string_data = fd(_data)

    if not _string_data == None:

        if fileExists(file_path):
            deleted = delete_file(file_path)

            if deleted:
                with open(file_path, "w") as f:
                    f.write(_string_data)

        else:
            with open(file_path, "w") as f:
                f.write(_string_data)

        return fileExists(file_path)
