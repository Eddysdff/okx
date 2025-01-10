import requests
import pandas as pd


PROXY_POOL_URL = 'http://127.0.0.1:5010/get_all/'


response = requests.get(PROXY_POOL_URL)
proxies = response.json()


proxy_list = []
for proxy in proxies[:100]:
    if '@' in proxy:
        auth, address = proxy.split('@')
        username, password = auth.split(':')
        ip, port = address.split(':')
    else:
        username, password = '', ''
        ip, port = proxy.split(':')
    
    proxy_list.append({
        'ip': ip,
        'port': port,
        'username': username,
        'password': password
    })


df = pd.DataFrame(proxy_list)


df.to_csv('proxies.csv', index=False)

print("CSV文件已生成")
