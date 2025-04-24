# totext 项目文档

## 项目概述
这个项目是一个Python脚本，用于将指定目录下的文件转换为UTF-8编码。支持的文件类型包括.txt、.doc和.docx。脚本会遍历目录，检测文件编码，并进行转换。

## 安装要求
- Python 3.x 环境
- 依赖库管理工具：uv（需先安装uv全局工具）
- 依赖库：chardet（用于编码检测）和python-docx（用于处理.docx文件）。通过uv管理依赖：
  ```bash
  uv init             # 初始化项目
  uv sync             # 生成虚拟环境
  uv pip install chardet python-docx  # 安装Python依赖
  ```
- 外部工具：antiword（用于处理.doc文件）。在Linux系统中可以通过命令安装：`sudo apt install antiword`

## 使用指南
1. 确保目录结构正确。脚本默认处理 `/home/coder/project/totext/1/txt` 和 `/home/coder/project/totext/1/doc` 目录。如果这些目录不存在，脚本会报错。
2. 安装所有依赖项和系统工具。
3. 激活虚拟环境后运行脚本：
   ```bash
   uv sync             # 确保虚拟环境已激活
   python main.py      # 运行主脚本
   ```
4. 脚本会自动转换文件并输出转换结果。

## 注意事项
- 如果antiword未安装，脚本会在启动时检查并提示安装。
- 确保目标目录存在且包含相应文件类型。
- 对于.txt文件，脚本直接转换编码；对于.doc和.docx文件，脚本会生成新的.txt文件。
- 处理过程中可能出现编码检测错误，请检查文件内容。
- 使用uv时请确保遵循其项目管理规范，依赖变更需通过uv管理而非手动修改
- 如果doc或docx文件加密则无法处理