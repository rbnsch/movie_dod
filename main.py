import optparse
from controller import Controller

def main():
    parser = optparse.OptionParser()
    parser.add_option("-c", "--check", dest = "check", type = 'string',
            metavar="MOVIENAME", help='Check a movie if it is financed by Department of Defense')

    parser.add_option("-u", "--update", dest = "apiKey", type = 'string',
            metavar="APIKEY", help='Update local data basis')

    (options, args) = parser.parse_args()

    if not options.check and not options.apiKey:
        parser.print_help()
        exit()

    c = Controller()

    if options.apiKey:
        c.updateDataBasis(options.apiKey)
    if options.check:
        c.checkMovie(options.check)

if __name__ == '__main__':
    main()
