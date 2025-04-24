import os
import sys
import chardet
import subprocess
from docx import Document

def convert_txt_files(source_dir, output_dir):
    """遍历并转换指定目录中的所有.txt文件为UTF-8编码"""
    for filename in os.listdir(source_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(source_dir, filename)
            try:
                # 检测文件编码
                with open(file_path, 'rb') as f:
                    raw_data = f.read(1024)
                detected = chardet.detect(raw_data)
                encoding = detected['encoding'] or 'latin-1'

                # 读取文件内容
                with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
                    content = f.read().replace('\r\n', '\n').replace('\r', '\n')
                    base_name = os.path.splitext(filename)[0]

                target_path = os.path.join(output_dir, f"{base_name}_txt.txt")
                with open(target_path, 'w', encoding='utf-8', newline='\n') as f:
                    f.write(content)
                print(f"完成转换: {filename}")

            except Exception as e:
                print(f"转换失败: {filename} - {str(e)}")

def convert_doc_files(source_dir, output_dir):
    """使用antiword将.doc文件转换为UTF-8编码的.txt文件"""
    for filename in os.listdir(source_dir):
        if filename.endswith('.doc'):
            file_path = os.path.join(source_dir, filename)
            base_name = os.path.splitext(filename)[0]
            target_path = os.path.join(output_dir, f"{base_name}_doc.txt")

            try:
                # 运行antiword命令
                result = subprocess.run(['antiword', file_path], 
                                        capture_output=True, check=True)
                
                # 检测输出编码并转换
                detected = chardet.detect(result.stdout)
                encoding = detected['encoding'] or 'latin-1'
                content = result.stdout.decode(encoding, errors='ignore')

                # 清理换行符并写入新文件
                content = content.replace('\r\n', '\n').replace('\r', '\n')
                with open(target_path, 'w', encoding='utf-8', newline='\n') as f:
                    f.write(content)
                print(f"转换成功: {filename} → {target_path}")

            except subprocess.CalledProcessError as e:
                print(f"转换失败（antiword报错）: {filename}")
            except Exception as e:
                print(f"转换失败: {filename} - {str(e)}")

def convert_docx_files(source_dir, output_dir):
    """使用python-docx将.docx文件转换为UTF-8编码的.txt文件"""
    for filename in os.listdir(source_dir):
        if filename.endswith('.docx'):
            file_path = os.path.join(source_dir, filename)
            base_name = os.path.splitext(filename)[0]
            target_path = os.path.join(output_dir, f"{base_name}_docx.txt")

            try:
                # 读取Word文档内容
                doc = Document(file_path)
                content = '\n'.join([para.text for para in doc.paragraphs])

                # 清理换行符并写入新文件
                content = content.replace('\r\n', '\n').replace('\r', '\n')
                with open(target_path, 'w', encoding='utf-8', newline='\n') as f:
                    f.write(content)
                print(f"转换成功: {filename} → {target_path}")

            except Exception as e:
                print(f"转换失败: {filename} - {str(e)}")

def main():
    try:
        # 检查antiword是否安装
        subprocess.run(['antiword', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print("错误：未找到antiword，请先安装：sudo apt install antiword")
        sys.exit(1)

    # 处理.txt文件
    input_dir = "/home/coder/project/totext/1/input"
    output_dir = "/home/coder/project/totext/1/output"
    if not os.path.exists(input_dir):
        print(f"错误：输入目录 {input_dir} 不存在")
        return
    os.makedirs(output_dir, exist_ok=True)
    convert_txt_files(input_dir, output_dir)

    # 处理.doc和.docx文件
    convert_doc_files(input_dir, output_dir)
    convert_docx_files(input_dir, output_dir)

if __name__ == "__main__":
    main()