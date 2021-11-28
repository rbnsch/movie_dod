import optparse
from APIRequests import APIRequest
from searchEngine import SearchEngine

def main():
    parser = optparse.OptionParser()
    parser.add_option("-c", "--check", dest = "check", type = 'string',
            metavar="MOVIENAME", help='Check a movie if it is financed by Department of Defense')

    parser.add_option("-u", "--update", action = "store_true", dest = "update", help='Update local data basis')

    parser.add_option("-a", "--apikey", dest = "api", type = 'string',
            metavar="APIKEY", help='Set API Key for IMDB API')

    (options, args) = parser.parse_args()

    if not options.check and not options.update and not options.api:
        parser.print_help()
        exit()

    if options.api:
        print("New API Key:", options.api)
    if options.update:
        key = input("Please enter api key")
        company = input("Please enter company id")
        print("Update Dataset")
        a = APIRequest(key, company)
        a.performRequest()
    if options.check:
        print("Check movie:", options.check)
        s = SearchEngine(options.check)
        s.checkPattern()

if __name__ == '__main__':
    main()
