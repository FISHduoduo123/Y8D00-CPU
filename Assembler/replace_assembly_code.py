from read_assembly_code_file import readfile,code_len

op_types = {'count':{'add':'00001',
                   'xor':'00010',
                   'xnor':'00011',
                   'not':'00100',
                   'and':'00101',
                   'or':'00110',
                   'sub':'00111',
                   'cmp':'01000'},
            'mov':'01001',
            'JP':{"br":'01010',
                  'jp':'01011'},
            'push':'01100',
            'pop':'01101',
            'call':'01110',
            'ret':'01111',
            'in':'10000',
            'out':'10001'}
addressing_types = {'addr_1':'001',
                    'addr_2':'010',
                    'addr_3':'011',
                    'addr_4':'100',
                    'addr_5':'101',
                    'addr_6':'110',
                    'addr_7':'111'}
jp_types = {'jc':'0001',
            'jo':'0010',
            'jz':'0011',
            'js':'0100',
            'je':'0101',
            'jne':'0110',
            'jnbe':'0111',
            'jnae':'1000'}
regfile = {'r0':'0000',
           'r1':'0001',
           'r2':'0010',
           'r3':'0011',
           'r4':'0100',
           'r5':'0101',
           'r6':'0110',
           'r7':'0111',
           'r8':'1000',
           'r9':'1001',
           'r10':'1010',
           'r11':'1011',
           'r12':'1100',
           'r13':'1101',
           'r14':'1110',
           'r15':'1111'}
interface_types = {'in1':'0001',
                   'in2':'0010',
                   'in3':'0011',
                   'in4':'0100'}

class imm_and_address_replace:
    def __init__(self,assem_code_str):
        self.assem_code_str = list()
        self.assem_code_str = assem_code_str
        self.fill_none()
        print(self.assem_code_str)
        self.create_new()
        print(self.assem_code_str_new)
    def fill_none(self):
        num = 5-len(self.assem_code_str)
        while num > 0:
            self.assem_code_str.append('None')
            num -= 1

        """
        add r1 r2 #100 addr_3      !!!
        mov r1 [off:10,32] addr_4  !!!
        mov [off:10,200] r4 addr_5 !!!
        mov r1 [off:10],r5 addr_6  !!!
        mov [off:10],r5 r4 addr_7  !!!
        mov r1 #100 addr_3         !!!
        br types r1 [200]          !!!
        jp r1 [200]
        call [200]                 !!!
        in [8] in1 r1
        """
    def appendd_num(self,string,number):
        try:
            if isinstance(int(string),int):
                number.append(int(string))
        except ValueError:
            pass
    def mul_list(self,number,num):
        num = 0
        i = len(number) - 1
        for n in number:
            num += n * (10 ** i)
            i -= 1
        return num
    def create_new(self):
        self.assem_code_str_new = list()
        self.assem_code_str_new.append(self.assem_code_str[0])
        if self.assem_code_str[1][0] == '[':
            num = 1
            number_1 = list()
            number_2 = list()
            for instruction_byte in self.assem_code_str:
                if instruction_byte == 'addr_5':
                    #获取偏移量和内存地址
                    offset = None
                    address = None
                    for string in self.assem_code_str[1][5:]:
                        if string == ',':
                            i = num
                            offset = format(self.mul_list(number_1,num),'04b')
                            for string in self.assem_code_str[1][5+i:]:
                                if string == ']':
                                    address = format(self.mul_list(number_2,num),'08b')
                                    break
                                self.appendd_num(string,number_2)
                                continue
                            break
                        self.appendd_num(string,number_1)
                        num += 1
                        continue
                    #将偏移量与内存地址放入对应字段
                    self.assem_code_str_new.append(address[0:4])
                    self.assem_code_str_new.append(address[4:])
                    self.assem_code_str_new.append(self.assem_code_str[2])
                    self.assem_code_str_new.append(offset)
                    self.assem_code_str_new.append(self.assem_code_str[3])
                    break

                elif instruction_byte == 'addr_7':
                    #获取偏移量和指针
                    offset = None
                    sp =None
                    for string in self.assem_code_str[1][5:]:
                        if string == ']':
                            i = num + 1
                            offset = format(self.mul_list(number_1, num), '04b')
                            sp = self.assem_code_str[1][5+i:]
                            break
                        self.appendd_num(string,number_1)
                        num += 1
                        continue
                    self.assem_code_str_new.append(sp)
                    self.assem_code_str_new.append('None')
                    self.assem_code_str_new.append(self.assem_code_str[2])
                    self.assem_code_str_new.append(offset)
                    self.assem_code_str_new.append(self.assem_code_str[3])
                    break

                elif self.assem_code_str[0] == 'call':
                    #获取跳转地址
                    address = None
                    for string in self.assem_code_str[1][1:]:
                        if string == ']':
                            address = format(self.mul_list(number_2, num), '08b')
                            break
                        self.appendd_num(string, number_2)
                        continue
                    self.assem_code_str_new.append('None')
                    self.assem_code_str_new.append('None')
                    self.assem_code_str_new.append(address[0:4])
                    self.assem_code_str_new.append(address[4:])
                    self.assem_code_str_new.append('None')
                    break

                elif self.assem_code_str[0] == 'in' or self.assem_code_str[0] == 'out':
                    address = None
                    for string in self.assem_code_str[1][1:]:
                        if string == ']':
                            address = format(self.mul_list(number_2, num), '04b')
                            break
                        self.appendd_num(string, number_2)
                        continue
                    self.assem_code_str_new.append(address)
                    self.assem_code_str_new.append(self.assem_code_str[2])
                    self.assem_code_str_new.append(self.assem_code_str[3])
                    self.assem_code_str_new.append('None')
                    self.assem_code_str_new.append('None')
                    break

        elif self.assem_code_str[2][0] == '[':
            num = 1
            number_1 = list()
            number_2 = list()
            for instruction_byte in self.assem_code_str:
                if instruction_byte == 'addr_4':
                    # 获取偏移量和内存地址
                    offset = None
                    address = None
                    for string in self.assem_code_str[2][5:]:
                        if string == ',':
                            i = num
                            offset = format(self.mul_list(number_1,num),'04b')
                            for string in self.assem_code_str[2][5+i:]:
                                if string == ']':
                                    address = format(self.mul_list(number_2,num),'08b')
                                    break
                                self.appendd_num(string,number_2)
                                continue
                            break
                        self.appendd_num(string,number_1)
                        num += 1
                        continue
                    self.assem_code_str_new.append(self.assem_code_str[1])
                    self.assem_code_str_new.append(offset)
                    self.assem_code_str_new.append(address[0:4])
                    self.assem_code_str_new.append(address[4:])
                    self.assem_code_str_new.append(self.assem_code_str[3])
                    break

                elif instruction_byte == 'addr_6':
                    # 获取偏移量和指针
                    offset = None
                    sp = None
                    for string in self.assem_code_str[2][5:]:
                        if string == ']':
                            i = num + 1
                            offset = format(self.mul_list(number_1, num), '04b')
                            sp = self.assem_code_str[2][5 + i:]
                            break
                        self.appendd_num(string, number_1)
                        num += 1
                        continue
                    self.assem_code_str_new.append(self.assem_code_str[1])
                    self.assem_code_str_new.append(offset)
                    self.assem_code_str_new.append(sp)
                    self.assem_code_str_new.append('None')
                    self.assem_code_str_new.append(self.assem_code_str[3])
                    break


                elif self.assem_code_str[0] == 'jp':
                    address = None
                    for string in self.assem_code_str[2][1:]:
                        if string == ']':
                            address = format(self.mul_list(number_2, num), '08b')
                            break
                        self.appendd_num(string, number_2)
                        continue
                    self.assem_code_str_new.append('None')
                    self.assem_code_str_new.append(self.assem_code_str[1])
                    self.assem_code_str_new.append(address[0:4])
                    self.assem_code_str_new.append(address[4:])
                    self.assem_code_str_new.append('None')
                    break

        elif self.assem_code_str[3][0] == '[':
            num = 0
            number_2 = list()
            #获取跳转地址
            address = None
            for string in self.assem_code_str[3][1:]:
                if string == ']':
                    address = format(self.mul_list(number_2, num), '08b')
                    break
                self.appendd_num(string, number_2)
                continue
            self.assem_code_str_new.append(self.assem_code_str[1])
            self.assem_code_str_new.append(self.assem_code_str[2])
            self.assem_code_str_new.append(address[0:4])
            self.assem_code_str_new.append(address[4:])
            self.assem_code_str_new.append('None')

        elif self.assem_code_str[2][0] == '#':
            self.assem_code_str_new.append(self.assem_code_str[1])
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append(format(int(self.assem_code_str[2][1:]),'08b')[0:4])
            self.assem_code_str_new.append(format(int(self.assem_code_str[2][1:]), '08b')[4:])
            self.assem_code_str_new.append(self.assem_code_str[3])

        elif self.assem_code_str[3][0] == '#':
            self.assem_code_str_new.append(self.assem_code_str[1])
            self.assem_code_str_new.append(self.assem_code_str[2])
            self.assem_code_str_new.append(format(int(self.assem_code_str[3][1:]), '08b')[0:4])
            self.assem_code_str_new.append(format(int(self.assem_code_str[3][1:]), '08b')[4:])
            self.assem_code_str_new.append(self.assem_code_str[4])

        '''add r1 r2 r3 addr_1
           mov r1 r3 addr_1'''
        if self.assem_code_str[3] == 'addr_1':
            self.assem_code_str_new.append(self.assem_code_str[1])
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append(self.assem_code_str[2])
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append(self.assem_code_str[3])

        elif self.assem_code_str[4] == 'addr_1':
            self.assem_code_str_new.append(self.assem_code_str[1])
            self.assem_code_str_new.append(self.assem_code_str[2])
            self.assem_code_str_new.append(self.assem_code_str[3])
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append(self.assem_code_str[4])

        #add r1 r2 addr_2
        elif self.assem_code_str[3] == 'addr_2':
            self.assem_code_str_new.append(self.assem_code_str[1])
            self.assem_code_str_new.append(self.assem_code_str[2])
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append(self.assem_code_str[3])

        elif self.assem_code_str[0] == 'ret':
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append('None')

        elif self.assem_code_str[0] == 'push':
            self.assem_code_str_new.append(self.assem_code_str[1])
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append('None')

        elif self.assem_code_str[0] == 'pop':
            self.assem_code_str_new.append(self.assem_code_str[1])
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append('None')

        elif self.assem_code_str[0] == 'cmp':
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append(self.assem_code_str[1])
            self.assem_code_str_new.append(self.assem_code_str[2])
            self.assem_code_str_new.append('None')
            self.assem_code_str_new.append('None')

class Replace:
    def __init__(self,assem_code_str,op_types,addressing_types,jp_types,regfile,interface_types):
        self.assem_code_str = imm_and_address_replace(assem_code_str).assem_code_str_new
        self.op_types = op_types
        self.addressing_types = addressing_types
        self.jp_types = jp_types
        self.regfile = regfile
        self.interface_types = interface_types
        self.assembly_code_replace()
    def count_replace(self):
        # 将op替换为二进制
        self.assem_code_str[0] = self.op_types['count'][self.assem_code_str[0]]
        # 是否有寻址类型
        for addr_type in self.addressing_types.keys():
            if self.assem_code_str[5] == addr_type:
                # 将寻址字段替换为二进制
                self.assem_code_str[5] = self.addressing_types[addr_type]
                if self.addressing_types[addr_type] == '001':
                    self.assem_code_str[1] = self.regfile[self.assem_code_str[1]]
                    self.assem_code_str[2] = self.regfile[self.assem_code_str[2]]
                    self.assem_code_str[3] = self.regfile[self.assem_code_str[3]]
                    self.assem_code_str[4] = '0000'
                if self.addressing_types[addr_type] == '010':
                    self.assem_code_str[1] = self.regfile[self.assem_code_str[1]]
                    self.assem_code_str[2] = self.regfile[self.assem_code_str[2]]
                    self.assem_code_str[3] = '0000'
                    self.assem_code_str[4] = '0000'
                if self.addressing_types[addr_type] == '011':
                    self.assem_code_str[1] = self.regfile[self.assem_code_str[1]]
                    self.assem_code_str[2] = self.regfile[self.assem_code_str[2]]

    def mov_replace(self):
        self.assem_code_str[0] = self.op_types[self.assem_code_str[0]]
        for addr_type in self.addressing_types.keys():
            if self.assem_code_str[5] == addr_type:
                # 将寻址字段替换为二进制
                self.assem_code_str[5] = self.addressing_types[addr_type]
                if self.addressing_types[addr_type] == '001':
                    self.assem_code_str[1] = self.regfile[self.assem_code_str[1]]
                    self.assem_code_str[2] = '0000'
                    self.assem_code_str[3] = self.regfile[self.assem_code_str[3]]
                    self.assem_code_str[4] = '0000'
                elif self.addressing_types[addr_type] == '011':
                    self.assem_code_str[1] = self.regfile[self.assem_code_str[1]]
                    self.assem_code_str[2] = '0000'
                elif self.addressing_types[addr_type] == '100':
                    self.assem_code_str[1] = self.regfile[self.assem_code_str[1]]
                elif self.addressing_types[addr_type] == '101':
                    self.assem_code_str[3] = self.regfile[self.assem_code_str[3]]
                elif self.addressing_types[addr_type] == '110':
                    self.assem_code_str[1] = self.regfile[self.assem_code_str[1]]
                    self.assem_code_str[3] = self.regfile[self.assem_code_str[3]]
                    self.assem_code_str[4] = '0000'
                elif self.addressing_types[addr_type] == '111':
                    self.assem_code_str[1] = self.regfile[self.assem_code_str[1]]
                    self.assem_code_str[2] = '0000'
                    self.assem_code_str[3] = self.regfile[self.assem_code_str[3]]

    def jp_replace(self):
        self.assem_code_str[0] = self.op_types['JP'][self.assem_code_str[0]]
        self.assem_code_str[5] = '000'
        self.assem_code_str[2] = self.regfile[self.assem_code_str[2]]
        for jp_type in self.jp_types.keys():
            if self.assem_code_str[1] == jp_type:
                self.assem_code_str[1] = self.jp_types[jp_type]
            elif self.assem_code_str[1] == 'None':
                self.assem_code_str[1] = '0000'

    def stack_replace(self):
        self.assem_code_str[0] = self.op_types[self.assem_code_str[0]]
        if self.assem_code_str[0] == '01100' or self.assem_code_str[0] == '01101':
            print(self.assem_code_str[1])
            self.assem_code_str[1] = self.regfile[self.assem_code_str[1]]
            self.assem_code_str[2] = '0000'
            self.assem_code_str[3] = '0000'
            self.assem_code_str[4] = '0000'
            self.assem_code_str[5] = '000'
        elif self.assem_code_str[0] == '01111':
            self.assem_code_str[1] = '0000'
            self.assem_code_str[2] = '0000'
            self.assem_code_str[3] = '0000'
            self.assem_code_str[4] = '0000'
            self.assem_code_str[5] = '000'
        elif self.assem_code_str[0] == '01110':
            self.assem_code_str[1] = '0000'
            self.assem_code_str[2] = '0000'
            self.assem_code_str[5] = '000'

    def io_replace(self):
        self.assem_code_str[0] = self.op_types[self.assem_code_str[0]]
        self.assem_code_str[2] = self.interface_types[self.assem_code_str[2]]
        self.assem_code_str[3] = self.regfile[self.assem_code_str[3]]
        self.assem_code_str[4] = '0000'
        self.assem_code_str[5] = '000'

    # 对一条汇编指令进行编译
    # op:运算类型
    def assembly_code_replace(self):
        if self.assem_code_str[0] == 'add':
            self.count_replace()
        elif self.assem_code_str[0] == 'xor':
            self.count_replace()
        elif self.assem_code_str[0] == 'xnor':
            self.count_replace()
        elif self.assem_code_str[0] == 'not':
            self.count_replace()
        elif self.assem_code_str[0] == 'and':
            self.count_replace()
        elif self.assem_code_str[0] == 'or':
            self.count_replace()
        elif self.assem_code_str[0] == 'sub':
            self.count_replace()
        if self.assem_code_str[0] == 'cmp':
            self.assem_code_str[0] = op_types['count'][self.assem_code_str[0]]
            self.assem_code_str[1] = '0000'
            self.assem_code_str[2] = regfile[self.assem_code_str[2]]
            self.assem_code_str[3] = regfile[self.assem_code_str[3]]
            self.assem_code_str[4] = '0000'
            self.assem_code_str[5] = '000'
        # op:传输类型
        if self.assem_code_str[0] == 'mov':
            self.mov_replace()
        # op:控制流类型
        if self.assem_code_str[0] == 'br':
            self.jp_replace()
        elif self.assem_code_str[0] == 'jp':
            self.jp_replace()
        # op:调用类型
        if self.assem_code_str[0] == 'push':
            self.stack_replace()
        elif self.assem_code_str[0] == 'pop':
            self.stack_replace()
        elif self.assem_code_str[0] == 'call':
            self.stack_replace()
        elif self.assem_code_str[0] == 'ret':
            self.stack_replace()
        # op:输入输出类型
        if self.assem_code_str[0] == 'in':
            self.io_replace()
        elif self.assem_code_str[0] == 'out':
            self.io_replace()


def Code_list(File_path):
    file_path = File_path  # 文件路径
    code_list = list()
    code_address = 1
    if code_len(file_path) > 0:
        while code_address <= code_len(file_path):
            print('--------------------------------------')
            assem_code_str = readfile('assembly code.txt', code_address).split()
            code_text = Replace(assem_code_str, op_types, addressing_types, jp_types, regfile,
                                interface_types).assem_code_str
            print(code_text)
            code_list.append(f'{code_text[0]}{code_text[1]}{code_text[2]}{code_text[3]}{code_text[4]}{code_text[5]}')
            code_address += 1
    return code_list
if __name__ == '__main__':
    print(Code_list('assembly code.txt'))