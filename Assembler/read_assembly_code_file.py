assembly_code = list()
code = None

def readfile(file_path, code_address):
    global assembly_code, code
    assembly_code.clear()  # 清空全局变量，避免历史数据累积
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:  # 跳过空行
                    assembly_code.append(stripped_line)
            # 检查 code_address 是否合法
            if 0 < code_address <= len(assembly_code):
                code = assembly_code[code_address - 1]
            else:
                print(f"错误: code_address {code_address} 超出范围")
                code = None
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
    return code

def code_len(file_path):
    Assembly_code = list()
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            for line in file:
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                Assembly_code.append(stripped_line)
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
    return len(Assembly_code)

if __name__ == "__main__":
    file_path = 'assembly code.txt'
    code_address = 1
    print(readfile(file_path, code_address))  # 输出第一行有效代码
    print(code_len(file_path))                # 输出有效代码行数

