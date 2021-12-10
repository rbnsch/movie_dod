"""
File: main.py
Author: Robin Schmidt
Purpose: The main file is responsible for evaluating the passed parameters and arguments with the help of optparse and
calling the corresponding controller method.
"""
import optparse
from Controller import Controller


def main():
    parser = optparse.OptionParser()
    parser.add_option("-c", "--check", dest="check", type='string',
                      metavar="MOVIENAME",
                      help='Check a title if it is financed by Department of Defense. Please provide a '
                           'searching Pattern')

    parser.add_option("-u", "--update", dest="apiKey", type='string',
                      metavar="APIKEY", help='Update local data basis. Please provide an API Key.')

    (options, args) = parser.parse_args()

    if not options.check and not options.apiKey:
        parser.print_help()
        exit()

    if options.check and options.apiKey:
        print("Please don't update the data basis and check a movie at the same time")
        exit()

    c = Controller()

    if options.apiKey:
        c.update_data_basis(options.apiKey)
    if options.check:
        c.check_movie(options.check)


if __name__ == '__main__':
    main()
