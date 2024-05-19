import re

def add_div_to_equations(md_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    modified_content = ""
    within_div = False

    # 正则表达式，用于匹配$$...$$格式公式
    equation_pattern = re.compile(r'\$\$(.+?)\$\$', re.DOTALL)

    for line in content:
        if '<div>' in line:
            within_div = True
        if '</div>' in line:
            within_div = False

        # 如果当前行包含$$...$$格式公式且不在<div>标签内，那么添加<div>标签
        if equation_pattern.search(line) and not within_div:
            modified_line = equation_pattern.sub(r'\n<div>\n\$\$\1\$\$\n</div>\n', line)
            modified_content += modified_line
        else:
            modified_content += line

    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

# 使用函数加<div>到所有的$$...$$公式
md_file_path = r'D:\Hugo\hugo-xmin-master\exampleSite\content\post\2. 插值法.md'  # 替换成您的Markdown文件路径
add_div_to_equations(md_file_path)