import requests
from bs4 import BeautifulSoup
import re

# 定义基本URL和页数范围
base_url = 'https://college.gaokao.com/spepoint/a21/s2/'
total_pages = 888  # 总页数
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

# 打开文件以写入模式
with open('output.txt', 'w', encoding='utf-8') as file:
    for page in range(1, total_pages + 1):
        if page == 1:
            url = base_url
        else:
            url = f'{base_url}p{page}/'

        # 调用requests中的get方法
        response = requests.get(url, headers=headers)
        response.encoding = 'gbk'

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # 提取所有文本
            for script in soup(["script", "style"]):  # 移除脚本和样式
                script.decompose()  # 清除脚本和样式标签

            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())

            # 去掉空行
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)

            # 将文本写入文件
            file.write(f"Page {page}:\n{text}\n\n")  # 添加页面标识符

            print(f"Page {page} 文本已成功写入output.txt文件")
        else:
            print(f"请求失败: Page {page}")
        # 为了避免频繁请求，可以在这里添加一个小小的延迟
        # import time
        # time.sleep(1)  # 每页请求间隔1秒

print("所有页面数据爬取完成")
