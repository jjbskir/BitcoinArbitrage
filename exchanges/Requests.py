import urllib.request
import urllib.parse
import urllib.error
import json

class Requests:
    '''
    HTTP request class. For making GET and POST calls.
    '''
    def __init__(self, baseURL):
        self.baseURL = baseURL
        self.URLError = None
        self.HTTPError = None

    def get(self, ext, params=None):
        '''
        Creates a get request.

        :param ext: URL extension for API.
        :param params: Paramters for GET request.
        '''
        url = self.create_url(ext, params)
        response = None
        try:
            # try making HTTP GET request. use "User-Agent" to make your urllib request seem like it is from a real person.
            hdr = {'Accept': 'application/json', 'User-Agent' : "Magic Browser"} # accept JSON data.
            req = urllib.request.Request(url, headers=hdr) # make request.
            response = urllib.request.urlopen(req) # get response.
        except urllib.error.URLError as e:
            # handle URL errors.
            print('URL error: ' + e.reason + ' - ' + e.read().decode("utf8", 'ignore'))
            self.URLError = e.reason
        except urllib.error.HTTPError as e:
            # handle HTTP errors.
            print('HTTP error: ' + e.reason + ' - ' + e.read().decode("utf8", 'ignore'))
            self.HTTPError = e.reason
        # JSON decode request if it exists.
        return self.json_decode(response)

    def create_url(self, ext, params=None):
        """
        Create a url from the base url, extension, and api parameters.

        :param ext: URL extension.
        :param params: API parameters for GET request.
        :return: Constructed URL for making GET request.
        """
        url = self.baseURL + ext
        if params:
            # add parameteres to the url.
            params = urllib.parse.urlencode(params)
            url = url + '?' + params
        return url

    def json_decode(self, response):
        """
        Takes a JSON HTTP GET request and decodes it into a python dictionary.

        :param response: HTTP GET request using urllib.request.urlopen.
        :return: dictionary of values.
        """
        try:
            return json.loads(response.read().decode('utf8'))
        except Exception:
            print('JSON Decoder failed')




