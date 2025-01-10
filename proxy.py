import requests
import pandas as pd

# 定义ProxyPool的API地址
PROXY_POOL_URL = 'http://127.0.0.1:5010/get_all/'

# 获取代理列表
response = requests.get(PROXY_POOL_URL)
proxies = response.json()

# 提取前100个代理地址和账户密码
proxy_list = []
for proxy in proxies[:100]:
    # 假设proxy是格式化为 'ip:port' 或 'username:password@ip:port'
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

# 创建DataFrame
df = pd.DataFrame(proxy_list)

# 保存为CSV文件
df.to_csv('proxies.csv', index=False)

print("CSV文件已生成")
