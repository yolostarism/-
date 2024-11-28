import re
import pandas as pd

with open('output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'(.*?)\n(.*?大学)\n(\d+)\n(\d+)\n(内蒙古)\n(文科)\n(\d{4})\n(.*?批|高校专项|------)'
matches = re.findall(pattern, text)

# 创建一个空的DataFrame
data = []

# 填充数据列表
for match in matches:
    data.append({
        '高校名称': match[1],
        '专业名称': match[0],
        '平均分': match[2],
        '最高分': match[3],
        '年份': match[6],
        '批次': match[7]
    })

# 创建DataFrame
df = pd.DataFrame(data)
# print(df.columns)
# 按高校名称排序
df = df.sort_values(by=['高校名称'])

# 保存到Excel文件
excel_file = 'university_scores.xlsx'
df.to_excel(excel_file, index=False)

if __name__ == '__main__':
    # for match in matches:
    #     major_name = match[0].replace('加入对比', '').strip()
    #     print(f"专业名称: {major_name}")
    #     print(f"高校名称: {match[1]}")
    #     print(f"平均分: {match[2]}")
    #     print(f"最高分: {match[3]}")
    #     print(f"考生地区: {match[4]}")
    #     print(f"科别: {match[5]}")
    #     print(f"年份: {match[6]}")
    #     print(f"批次: {match[7]}")
    #     print("-" * 50)
    print(f"数据已保存到 {excel_file}")



