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
        @param ext: URL extension for API.
        @param params: Paramters for GET request.
        '''
        url = self.baseURL + ext
        if params:
            # add parameteres to the url.
            params = urllib.parse.urlencode(params)
            url = url + '?' + params
        req = None
        try:
             # try making HTTP GET request.
            req = urllib.request.urlopen(url)
        except urllib.error.URLError as e:
            # handle URL errors.
            print(e.reason)
            self.URLError = e.reason
        except urllib.error.HTTPError as e:
            # handle HTTP errors.
            print(e.reason)
            self.HTTPError = e.reason
        if not req:
            return None
        else:
            # JSON decode request if it exists.
            return self.json_decode(req)

    def json_decode(self, req):
        '''
        Takes a JSON HTTP GET request and decodes it into a python dictionary.
        @param req: HTTP GET request using urllib.request.urlopen.
        @return: dictionary of values.
        '''
        try:
            return json.loads(req.read().decode('utf8'))
        except Exception:
            print('JSON Decoder failed')




