"""

完成assembly code.txt的汇编编程运行该程序，
即可生成machine code.txt对应机器码

"""

from replace_assembly_code import Code_list
from write_machine_file import create_machine_code

assembly_path = 'assembly code.txt'
machine_path = 'machine code_1.txt'
#machine_path = 'machine code_2.txt'
code = Code_list(assembly_path)
create_machine_code(machine_path,code)
