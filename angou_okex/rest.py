import requests
import hashlib
from urllib.parse import urlencode


class InvalidJSON(Exception):
    pass


class RestError(Exception):
    def __init__(self, obj):
        super().__init__(str(obj))


class RestSession:
    def __init__(self, api_key, api_secret, timeout=None):
        self.api_key = api_key
        self.api_secret = api_secret
        self.timeout = timeout
        self._session = requests.Session()

    @staticmethod
    def _get_sign(params, api_secret):
        new_params = list(sorted(params.items()))
        new_params.append(('secret_key', api_secret))
        payload = urlencode(new_params)
        return hashlib.md5(payload.encode('utf8')).hexdigest().upper()

    def post(self, path, params, sign=False):
        if sign:
            params['api_key'] = self.api_key
            params['sign'] = RestSession._get_sign(params, self.api_secret)

        r = self._session.request('POST', f'https://www.okex.com/api/v1/{path}',
                                  params=params, timeout=self.timeout)
        r.raise_for_status()
        try:
            result = r.json()
        except ValueError:
            raise InvalidJSON() from None

        if not result['result']:
            raise RestError(result)

        return result
