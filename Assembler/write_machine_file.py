
code_list = []
def create_machine_code(Filename, Code_list):
    try:
        with open(Filename, mode='w', encoding='UTF-8') as file:
            file.writelines(f"{code}\n" for code in Code_list)
        print(f"文件 {Filename} 已成功生成！")
    except IOError as e:
        print(f"错误: 无法写入文件 {Filename}")
        print(f"详细信息: {e}")

if __name__ == '__main__':
     create_machine_code('machine', code_list)
