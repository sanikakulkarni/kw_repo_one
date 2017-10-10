"""" store and verify driver """
import Actions.OneActions
from WarriorCore import kw_driver


def main(keyword, data_repository, args_repository):
    """Doc Strings """
    # Declare a list of packages to be used by this driver,
    # if you want to add more packages import them outside the main function
    # and then add them to the package_list below
    package_list = [Actions.OneActions]

    return kw_driver.execute_keyword(keyword, data_repository, args_repository, package_list)
