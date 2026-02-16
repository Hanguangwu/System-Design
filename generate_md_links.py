import os
import pathlib

def generate_md_links(source_dir, output_file=None):
    """
    遍历指定目录下的所有markdown文件，生成指定格式的markdown链接
    
    Args:
        source_dir (str): 要遍历的源目录路径
        output_file (str, optional): 输出文件路径，如果为None则只打印到控制台
    """
    # 验证目录是否存在
    if not os.path.isdir(source_dir):
        print(f"错误：目录 '{source_dir}' 不存在！")
        return
    
    # 存储生成的链接列表
    md_links = []
    
    # 遍历目录下的所有文件
    for filename in os.listdir(source_dir):
        # 只处理markdown文件
        if filename.lower().endswith('.md'):
            # 获取文件名（不含扩展名）
            file_name_without_ext = pathlib.Path(filename).stem
            # 生成指定格式的链接
            link = f"- [{file_name_without_ext}](./DesignPattern/{filename})"
            md_links.append(link)
    
    # 如果没有找到markdown文件
    if not md_links:
        print(f"在目录 '{source_dir}' 中未找到任何markdown文件")
        return
    
    # 按文件名排序（可选）
    md_links.sort()
    
    # 输出结果
    result = '\n'.join(md_links)
    
    # 打印到控制台
    print("生成的Markdown链接：")
    print("-" * 50)
    print(result)
    print("-" * 50)
    
    # 如果指定了输出文件，则写入文件
    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"\n链接已成功写入文件：{output_file}")
        except Exception as e:
            print(f"\n写入文件失败：{e}")

if __name__ == "__main__":
    # 配置参数
    # 你需要修改这里的目录路径为实际的System-Design目录路径
    SOURCE_DIRECTORY = "./DesignPattern/"
    # 可选：指定输出文件路径，如 "md_links.txt"，设为None则只输出到控制台
    OUTPUT_FILE = "md_links.txt"
    
    # 执行生成函数
    generate_md_links(SOURCE_DIRECTORY, OUTPUT_FILE)