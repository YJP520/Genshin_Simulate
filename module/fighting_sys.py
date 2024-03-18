"""
@Project : GenShin - Fighting System
@Time : 2024/01/02
@Author : YU.J.P
@Version: 1.0
@CopyRight: YU.J.P
"""
import random

# 导入外部包
from plug_in.Colors import Color


########################################################################################################################


class FightSystem:

    # 初始化
    def __init__(self):
        # 变量
        # 生命值上限
        self.base_hp = 48610
        # 基础攻击力
        self.base_power = 1070
        # 攻击力加成
        self.power_buff = 0.75
        # 元素精通
        self.element_power = 200
        # 暴击率
        self.damage_probability = 0.75
        # 暴击伤害
        self.damage_buff = 1.12
        # 元素增伤
        self.element_buff = 0.766
        # self.element_buff = 0.30
        # 伤害增伤
        self.all_element_buff = 0.4

        # 普通攻击 加成倍率 65%
        self.common_base = 1.136
        # 元素战技 加成倍率 325%
        self.skill_base = 4.31
        # 元素爆发 加成倍率 525%
        self.skill_boss = 2.70

    # 是否暴击
    def is_damege(self):
        # 随机区间
        section = self.damage_probability * 100
        # 随机数
        number = random.randint(0, 100)
        # print(Color.carmine, number)
        # 是否暴击
        if number < section:
            print(Color.carmine, '暴击 ')
            return self.damage_buff
        else:
            print(Color.carmine, '未暴击 ')
            return 0

    # 攻击测试
    def culculate_damage(self, instruct):
        result = 0
        # 最终攻击力
        power = (self.base_power + self.base_power * (self.power_buff + 1))
        print(Color.carmine, '攻击力: ', power)
        # 最终伤害
        if instruct == '1':  # 普通攻击
            print(Color.yellow, '普通攻击')
            result = power * \
                     self.common_base * \
                     (self.element_buff + self.all_element_buff + 1) * \
                     (self.is_damege() + 1)
        elif instruct == '2':  # 元素战技
            print(Color.yellow, '元素战技')
            result = power * \
                     self.skill_base * \
                     (self.element_buff + self.all_element_buff + 1) * \
                     (self.is_damege() + 1)
        elif instruct == '3':  # 元素爆发
            print(Color.yellow, '元素爆发 * 10')
            result = power * \
                     self.skill_boss * \
                     (self.element_buff + self.all_element_buff + 1) * \
                     (self.is_damege() + 1)
        elif instruct == '4':  # 重击
            print(Color.yellow, '那维莱特重击')
            result = self.base_hp * 0.1447 * \
                     (self.element_buff + self.all_element_buff + 1) * \
                     (self.is_damege() + 1)
        return result


########################################################################################################################


########################################################################################################################


########################################################################################################################

# MAIN
if __name__ == '__main__':
    fight_ob = FightSystem()
    while True:
        instruct = input("[攻击1/战技2/爆发3]:")
        if instruct == '0':
            break
        else:
            damage = int(fight_ob.culculate_damage(instruct))
            print(Color.cyan, '最终伤害: ', damage, '\n')