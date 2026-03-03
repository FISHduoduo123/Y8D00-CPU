class READ:
    def __init__(self,file_path):
        self.machine_code = list()
        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                for line in file:
                    stripped_line = line.strip()
                    self.machine_code.append(stripped_line)
        except FileNotFoundError:
            print(f"文件未找到: {file_path}")
        except Exception as e:
            print(f"读取文件时发生错误: {e}")
    def addr(self,addr):
        code = self.machine_code[addr - 1]
        return code

