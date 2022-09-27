import os


def is_user_root():
    return os.getuid() == 0
