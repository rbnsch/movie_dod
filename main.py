import optparse

def main():
    parser = optparse.OptionParser()
    parser.add_option("-c", "--check", dest = "check", type = 'string',
            metavar="MOVIENAME")

    parser.add_option("-u", "--update", action = "store_true", dest = "update")

    parser.add_option("-a", "--apikey", dest = "api", type = 'string',
            metavar="APIKEY")

    (options, args) = parser.parse_args()

    if not options.check and not options.update and not options.api:
        parser.print_help()
        exit()

    if options.api:
        print("New API Key:", options.api)
    if options.update:
        print("Update Dataset")
    if options.check:
        print("Check movie:", options.check)

if __name__ == '__main__':
    main()
