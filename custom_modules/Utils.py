from custom_modules.PlatformConstants import LINE_SEP as lsep
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.TypeTester import arg_is_a_dict as aiad, arg_is_a_list as aial


def non_none_value(*args):
    errors = []

    for a in args:
        if a == None:
            errors.append({"{}".format(a): "Nonne"})
        else:
            continue

    if len(errors) > 0:
        return {"status": False, "errors": errors}
    else:
        return {"status": True}


def print_dict_values(_dict=None):
    if not _dict == None:
        items = _dict.items()

        for item in items:
            print("{}\t{}".format(item[0], item[1]))


def print_dict_keys(_dict=None):
    if not _dict == None:
        keys = _dict.keys()

        print(*keys, sep="\t")


def flatten_dict(_dict=None):
    if not _dict == None and len(_dict) > 0 and aiad(_dict):
        _string = ""
        for i, item in enumerate(_dict.items()):
            if i < (len(_dict.items())):
                _string += "{}\t{}{}".format(item[0], item[1], lsep)
            else:
                _string += "{}\t{}".format(item[0], item[1])
        return _string
    return None


def flatten_list(_list=None):
    if not _list == None and len(_list) > 0 and aial(_list):
        _string = ""
        for i, item in enumerate(_list):
            if i < (len(_list)):
                _string += "{}\t{}".format(item, lsep)
            else:
                _string += "{}\t{}".format(item)
        return _string
    return None
