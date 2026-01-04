from urllib.request import Request, urlopen
from json import dumps, loads


class ConnApi:

    def __init__(self, api, api_key):
        self.api = api
        self.api_key = api_key

    def request(
            self,
            type_method,
            data=None,
            content_type='application/json',
            *endpoints
        ):

        endpoints_str = '' if endpoints else None

        if endpoints:
            for endpoint in endpoints:
                endpoints_str = endpoints_str + f'/{endpoint}'

        headers =  {'API-Key':self.api_key, 'Content-Type': content_type}

        request = Request(
            url=self.api if not endpoints else f'{self.api}/{endpoints_str}',
            data=bytes(dumps(data), encoding='utf-8'),
            headers=headers,
            method=type_method
        )

        response = urlopen(request)

        if response:
            return loads(response.read().decode('utf-8'))
