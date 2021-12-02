import optparse
from APIRequests import APIRequest
from searchEngine import SearchEngine

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

    if options.apiKey:
        print("Update Dataset")
        a = APIRequest(options.apiKey, "co0050471")
        #a.performRequest()
    if options.check:
        print("Check movie:", options.check)
        s = SearchEngine(options.check)
        s.checkPattern()

if __name__ == '__main__':
    main()
