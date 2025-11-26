import os
import sys

# --- 强制配置 ---
# 你的源代码目录
PROJECT_PATH = r"D:\Documents\Codes\2025_DroneControlCore"
OUTPUT_FILE = "all_code.txt"

# 包含的文件类型
EXTENSIONS = {'.py', '.vue', '.js', '.ts', '.cpp', '.h', '.c', '.java'}
# 忽略目录
EXCLUDE_DIRS = {
    'node_modules', '__pycache__', '.git', '.idea', '.vscode',
    'dist', 'build', 'coverage', 'tests', 'venv', 'migrations'
}
EXCLUDE_FILES = {'package-lock.json', 'yarn.lock', 'LICENSE', 'README.md'}

def collect_code():
    print(f"[*] 开始扫描目录: {PROJECT_PATH}")
    if not os.path.exists(PROJECT_PATH):
        print(f"[!] 错误: 找不到路径 {PROJECT_PATH}")
        return

    total_lines = 0
    file_count = 0
    
    # 使用 'w' 模式打开，errors='ignore' 防止写入时编码报错
    with open(OUTPUT_FILE, 'w', encoding='utf-8', errors='ignore') as outfile:
        for root, dirs, files in os.walk(PROJECT_PATH):
            # 修改 dirs 列表以原地跳过忽略目录
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in EXTENSIONS and file not in EXCLUDE_FILES:
                    file_path = os.path.join(root, file)
                    
                    try:
                        # 【核心修复】强制忽略读取错误 (errors='ignore')
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            
                            # 写入分隔符
                            rel_path = os.path.relpath(file_path, PROJECT_PATH)
                            outfile.write(f"\n\n{'/'*50}\n")
                            outfile.write(f"// FILE: {rel_path}\n")
                            outfile.write(f"{'/'*50}\n")
                            
                            # 去除空行
                            lines = [line for line in content.splitlines() if line.strip()]
                            cleaned_content = "\n".join(lines)
                            
                            outfile.write(cleaned_content)
                            
                            lines_count = len(lines)
                            total_lines += lines_count
                            file_count += 1
                            # 每处理10个文件打印一次，避免刷屏
                            if file_count % 10 == 0:
                                print(f"已处理 {file_count} 个文件...")
                                
                    except Exception as e:
                        print(f"[!] 跳过文件 {file}: {e}")

    print(f"\n{'='*30}")
    print(f"SUCCESS! 成功生成 {OUTPUT_FILE}")
    print(f"包含文件数: {file_count}")
    print(f"总代码行数: {total_lines}")
    print(f"{'='*30}")

if __name__ == '__main__':
    collect_code()
