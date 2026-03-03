"""
该烧录程序配套Assembler YDD-ISA 1.0汇编器使用
仅支持顺序执行183条指令内存空间
"""

from mcpi.minecraft import Minecraft

import read_machine_code_file as file

def read_file(path):
    i = 1
    machine_1 = list()
    machine_2 = list()
    machine_3 = list()

    data = file.READ(path)
    while i <= len(data.machine_code):
        machine = data.addr(i)
        machine_1.append(machine[0:8])
        machine_2.append(machine[8:16])
        machine_3.append(machine[16:])
        i += 1
    return machine_1,machine_2,machine_3


def set_code_1(x_basic,y_basic,z_basic,Code_1):
    x = x_basic
    y = y_basic+14
    z = z_basic
    addr = 0
    i = 0
    while addr <= 63:
        if addr+1 > len(Code_1):
            break
        while i <= 7:
            if Code_1[addr][i] == '1':
                mc.setBlock(x, y, z, 152)
            elif Code_1[addr][i] == '0':
                mc.setBlock(x, y, z, 0)
            i += 1
            y -= 2
        addr += 1
        i = 0
        y = y_basic + 14
        z -= 2

    x -= 18
    z += 2
    while addr <= 127:
        if addr+1 > len(Code_1):
            break
        while i <= 7:
            if Code_1[addr][i] == '1':
                mc.setBlock(x, y, z, 152)
            elif Code_1[addr][i] == '0':
                mc.setBlock(x, y, z, 0)
            i += 1
            y -= 2
        addr += 1
        i = 0
        y = y_basic + 14
        z +=  2

    x -= 18
    z -= 20
    while addr <= 181:
        if addr+1 > len(Code_1):
            break
        while i <= 7:
            if Code_1[addr][i] == '1':
                mc.setBlock(x, y, z, 152)
            elif Code_1[addr][i] == '0':
                mc.setBlock(x, y, z, 0)
            i += 1
            y -= 2
        addr += 1
        i = 0
        y = y_basic + 14
        z -= 2

def set_code_2(x_basic,y_basic,z_basic,Code_2):
    x = x_basic
    y = y_basic+14
    z = z_basic
    addr = 0
    i = 0
    while addr <= 63:
        if addr+1 > len(Code_2):
            break
        while i <= 7:
            if Code_2[addr][i] == '1':
                mc.setBlock(x, y, z, 152)
            elif Code_2[addr][i] == '0':
                mc.setBlock(x, y, z, 0)
            i += 1
            y -= 2
        addr += 1
        i = 0
        y = y_basic + 14
        z -= 2

    x -= 18
    z += 2
    while addr <= 127:
        if addr+1 > len(Code_2):
            break
        while i <= 7:
            if Code_2[addr][i] == '1':
                mc.setBlock(x, y, z, 152)
            elif Code_2[addr][i] == '0':
                mc.setBlock(x, y, z, 0)
            i += 1
            y -= 2
        addr += 1
        i = 0
        y = y_basic + 14
        z +=  2

    x -= 18
    z -= 20
    while addr <= 181:
        if addr+1 > len(Code_2):
            break
        while i <= 7:
            if Code_2[addr][i] == '1':
                mc.setBlock(x, y, z, 152)
            elif Code_2[addr][i] == '0':
                mc.setBlock(x, y, z, 0)
            i += 1
            y -= 2
        addr += 1
        i = 0
        y = y_basic + 14
        z -= 2

def set_code_3(x_basic,y_basic,z_basic,Code_3):
    x = x_basic
    y = y_basic + 14
    z = z_basic
    addr = 0
    i = 0
    while addr <= 63:
        if addr + 1 > len(Code_3):
            break
        while i <= 7:
            if Code_3[addr][i] == '1':
                mc.setBlock(x, y, z, 152)
            elif Code_3[addr][i] == '0':
                mc.setBlock(x, y, z, 0)
            i += 1
            y -= 2
        addr += 1
        i = 0
        y = y_basic + 14
        z -= 2

    x -= 18
    z += 2
    while addr <= 127:
        if addr + 1 > len(Code_3):
            break
        while i <= 7:
            if Code_3[addr][i] == '1':
                mc.setBlock(x, y, z, 152)
            elif Code_3[addr][i] == '0':
                mc.setBlock(x, y, z, 0)
            i += 1
            y -= 2
        addr += 1
        i = 0
        y = y_basic + 14
        z += 2

    x -= 18
    z -= 20
    while addr <= 181:
        if addr + 1 > len(Code_3):
            break
        while i <= 7:
            if Code_3[addr][i] == '1':
                mc.setBlock(x, y, z, 152)
            elif Code_3[addr][i] == '0':
                mc.setBlock(x, y, z, 0)
            i += 1
            y -= 2
        addr += 1
        i = 0
        y = y_basic + 14
        z -= 2
def get_player_position(player_name):
    # 获取所有玩家的实体ID
    players = mc.getPlayerEntityIds()
    for player_id in players:
        # 获取玩家的名称
        player_info = mc.entity.getName(player_id)
        if player_info == player_name:
            # 获取玩家的坐标
            pos = mc.entity.getPos(player_id)
            return pos
if __name__ == '__main__':

    code_1,code_2,code_3=read_file("D:\\python\\Python-Assembler\\Assembler YDD-ISA 1.0\\machine code_2.txt")
    init_1,init_2,init_3=read_file('init')
    mc = Minecraft.create()
    ply_x, ply_y, ply_z = get_player_position('FISHduoduo')

    print(code_1)
    print(code_2)
    print(code_3)

    set_code_1(ply_x, ply_y, ply_z - 2, init_1)
    set_code_2(ply_x - 6, ply_y, ply_z - 2, init_2)
    set_code_3(ply_x - 12, ply_y, ply_z - 2, init_3)

    set_code_1(ply_x, ply_y, ply_z-2,code_1)
    set_code_2(ply_x-6, ply_y, ply_z - 2, code_2)
    set_code_3(ply_x-12, ply_y, ply_z - 2, code_3)
    print('烧录完成！！！')