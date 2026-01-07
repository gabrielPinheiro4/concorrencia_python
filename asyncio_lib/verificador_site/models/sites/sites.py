from urllib.error import HTTPError


class Sites:

    def __init__(self, sites):
        self.__sites = sites

    def verify_sites(self):
        
        for site in self.__sites:

            if not isinstance(site, HTTPError):
                print(f'{site.get('page').get('domain')} é malicioso?: {site.get('verdicts').get('overall').get('malicious')}')
