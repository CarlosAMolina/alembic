import subprocess


# TODO rm
def sum_int(number_1: int, number_2: int) -> int:
    return number_1 + number_2


def create_migration():
    print("Creating migration")
    subprocess.run(["ls", "-l"])  # TODO
    print("The migration has been created")
