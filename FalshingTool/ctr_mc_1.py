"""
该烧录程序配套Assembler YDD-ISA 1.0汇编器使用
仅支持127Byte(0x01~0x7F)内存空间
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

def set_basic(x_basic,y_basic,z_basic):
    x=x_basic
    y=y_basic
    z=z_basic
    while z > z_basic-127:
        while y-8<(y_basic+8):
            mc.setBlock(x,y,z,251,9)
            mc.setBlock(x, y, z - 1, 0)
            y += 2
        y = y_basic
        z -= 2
    x = x_basic+7
    y = y_basic
    z = z_basic-1
    while z > z_basic-128:
        while y-8<(y_basic+8):
            mc.setBlock(x,y,z,251,9)
            mc.setBlock(x, y, z - 1, 0)
            y += 2
        y = y_basic
        z -= 2
    x = x_basic + 14
    y = y_basic
    z = z_basic
    while z > z_basic - 127:
        while y - 8 < (y_basic + 8):
            mc.setBlock(x, y, z, 251, 9)
            mc.setBlock(x, y, z - 1, 0)
            y += 2
        y = y_basic
        z -= 2

    x = x_basic+2
    y = y_basic
    z = z_basic
    while z > z_basic - 125:
        while y - 8 < (y_basic + 8):
            mc.setBlock(x, y, z, 251, 9)
            mc.setBlock(x, y, z-1, 0)
            y += 2
        y = y_basic
        z -= 2
    x = x_basic + 9
    y = y_basic
    z = z_basic-1
    while z > z_basic - 126:
        while y - 8 < (y_basic + 8):
            mc.setBlock(x, y, z, 251, 9)
            mc.setBlock(x, y, z - 1, 0)
            y += 2
        y = y_basic
        z -= 2
    x = x_basic + 16
    y = y_basic
    z = z_basic
    while z > z_basic - 125:
        while y - 8 < (y_basic + 8):
            mc.setBlock(x, y, z, 251, 9)
            mc.setBlock(x, y, z - 1, 0)
            y += 2
        y = y_basic
        z -= 2

def set_code_1(x_basic,y_basic,z_basic,Code_1):
    x = x_basic
    y = y_basic+14
    z = z_basic-1
    addr = 0
    i = 0
    while z > z_basic-128:
        if addr+1 > len(Code_1):
            break
        if addr+1 == 65:
            break
        while y >= y_basic:
            if i == 8:
                break
            elif Code_1[addr][i] == '1':
                mc.setBlock(x, y, z, 76, 4)
                y -= 2
            elif Code_1[addr][i] == '0':
                mc.setBlock(x, y, z, 0)
                y -= 2
            i += 1
        i = 0
        addr += 1
        y = y_basic + 14
        z -= 2
    x = x_basic + 2
    y = y_basic + 14
    z = z_basic - 1
    i = 0
    while z > z_basic - 125:
        if addr+1 > len(Code_1):
            break
        if addr + 1 == 64:
            break
        while y >= y_basic:
            print(i)
            if i == 8:
                break
            elif Code_1[addr][i] == '1':
                mc.setBlock(x, y, z, 76, 4)
                y -= 2
            elif Code_1[addr][i] == '0':
                mc.setBlock(x, y, z, 0)
                y -= 2
            i += 1
        i = 0
        addr += 1
        y = y_basic + 14
        z -= 2

def set_code_2(x_basic,y_basic,z_basic,Code_2):
    x = x_basic + 7
    y = y_basic+14
    z = z_basic-2
    addr = 0
    i = 0
    while z > z_basic-129:
        if addr+1 > len(Code_2):
            break
        if addr+1 == 65:
            break
        while y >= y_basic:
            if i == 8:
                break
            elif Code_2[addr][i] == '1':
                mc.setBlock(x, y, z, 76, 4)
                y -= 2
            elif Code_2[addr][i] == '0':
                mc.setBlock(x, y, z, 0)
                y -= 2
            i += 1
        i = 0
        addr += 1
        y = y_basic + 14
        z -= 2
    x = x_basic + 9
    y = y_basic + 14
    z = z_basic - 2
    while z > z_basic - 126:
        if addr+1 > len(Code_2):
            break
        if addr + 1 == 64:
            break
        while y >= y_basic:
            if i == 8:
                break
            elif Code_2[addr][i] == '1':
                mc.setBlock(x, y, z, 76, 4)
                y -= 2
            elif Code_2[addr][i] == '0':
                mc.setBlock(x, y, z, 0)
                y -= 2
            i += 1
        i = 0
        addr += 1
        y = y_basic + 14
        z -= 2

def set_code_3(x_basic,y_basic,z_basic,Code_3):
    x = x_basic+14
    y = y_basic+14
    z = z_basic-1
    addr = 0
    i = 0
    while z > z_basic-128:
        if addr+1 > len(Code_3):
            break
        if addr+1 == 65:
            break
        while y >= y_basic:
            if i == 8:
                break
            elif Code_3[addr][i] == '1':
                mc.setBlock(x, y, z, 76, 4)
                y -= 2
            elif Code_3[addr][i] == '0':
                mc.setBlock(x, y, z, 0)
                y -= 2
            i += 1
        i = 0
        addr += 1
        y = y_basic + 14
        z -= 2
    x = x_basic + 16
    y = y_basic + 14
    z = z_basic - 1
    i = 0
    while z > z_basic - 125:
        if addr+1 > len(Code_3):
            break
        if addr + 1 == 64:
            break
        while y >= y_basic:
            print(i)
            if i == 8:
                break
            elif Code_3[addr][i] == '1':
                mc.setBlock(x, y, z, 76, 4)
                y -= 2
            elif Code_3[addr][i] == '0':
                mc.setBlock(x, y, z, 0)
                y -= 2
            i += 1
        i = 0
        addr += 1
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

    code_1,code_2,code_3=read_file("D:\\python\\Python-Assembler\\Assembler YDD-ISA 1.0\\machine code_1.txt")

    mc = Minecraft.create()

    ply_x, ply_y, ply_z = get_player_position('FISHduoduo')
    print(ply_x,ply_y,ply_z)

    print(code_1)
    print(code_2)
    print(code_3)
    set_basic(ply_x, ply_y, ply_z-1)
    set_code_1(ply_x, ply_y, ply_z-1,code_1)
    set_code_2(ply_x, ply_y, ply_z-1,code_2)
    set_code_3(ply_x, ply_y, ply_z-1,code_3)
    print('烧录完成！！！')






