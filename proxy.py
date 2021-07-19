from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

def proxy_create():
    proxy = test_proxy() # 잘 작동되는 프록시 선별
    return proxy.get_address()

def test_proxy():
    req_proxy = RequestProxy()
    test_url = 'http://ipv4.icanhazip.com'
    while True: # 제대로된 프록시가 나올때까지 무한반복 
        requests = req_proxy.generate_proxied_request(test_url)

        if requests is not None:
            print("\t Response: ip={0}".format(u''.join(requests.text).encode('utf-8')))
            proxy = req_proxy.current_proxy
            break

        else:
            continue
    
    return proxy
# print(proxy_create())
