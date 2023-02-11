import util.download as download
from util.helper import menu_input
from util.files import make_input_output_folders


def menu():
    make_input_output_folders()
    while True:
        user_choice = menu_input('Welcome to Package Installer',
                                 ['Download', 'Upload', 'Exit'])

        if user_choice == 'Download':
            download.download()

        if user_choice == 'Upload':
            pass

        if user_choice == 'Exit':
            exit(0)
