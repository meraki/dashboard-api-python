def handle_3xx(self, response):
    abs_url = response.headers['Location']
    substring = 'meraki.com/api/v'
    if substring not in abs_url:
        substring = 'meraki.cn/api/v'
    self._base_url = abs_url[:abs_url.find(substring) + len(substring) + 1]
    return abs_url

