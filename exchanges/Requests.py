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

    def request(self, ext, params=None, headers=None):
        url = self.create_url(ext, params)
        hdr = self.create_header(headers)
        response = None
        try:
            if 'params' in url:
                req = urllib.request.Request(url['url'], url['params'], headers=hdr) # make request.
            else:
                req = urllib.request.Request(url['url'], headers=hdr)
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
        :return: Constructed URL for making GET request that are in a dictionary of base url and parameters.
        url = {'url': url, 'params': params}
        """
        url = {}
        url['url'] = (self.baseURL + ext)
        if params:
            # add parameteres to the url.
            url['params'] = urllib.parse.urlencode(params).encode("utf-8")
        return url

    def create_header(self, headers=None):
        """
        Create header to be used in HTTP request.
        """
        #TODO: Make Test
        # try making HTTP GET request. use "User-Agent" to make your urllib request seem like it is from a real person.
        hdr = { 'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'} # accept JSON data.
        if headers:
            hdr.update(headers)
        return hdr

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




