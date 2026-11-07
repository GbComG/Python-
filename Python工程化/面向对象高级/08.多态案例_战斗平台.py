"""
案例：Python多态案例之 战斗平台
1. 构建战斗平台函数 `object_fight()`，接收：英雄、敌机两个对象
2. 要求：**不修改战斗平台代码**的前提下，完成多次战斗
3. 规则：
   - 英雄 1：1 代战士，攻击力 60
   - 英雄 2：2 代战士，攻击力 80
   - 敌机 1：1 代敌机，防御力 70
4. 类规划：
   - 英雄基类：`HeroFighter`
   - 英雄子类：`AdvHeroFighter`
   - 敌机类：`EnemyFighter`
"""
class HeroFighter(object):
    def power(self):
        return 60
class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80
class EnemyFighter:
    def power(self):
        return 70
#4.构建对战平台，公共的函数，不同的参数，不同的效果

def object_fight(hero,enemy):
    #参1：英雄机，参2：敌机
    if hero.power()>= enemy.power():
        print("英雄机 战胜 敌机")
    else:
        print("英雄机 惜败 敌机")

#5.测试
if __name__ == '__main__':
    h1p = HeroFighter()
    e1p = EnemyFighter()
    if h1p.power() >= e1p.power():
        print("英雄机一代 战胜 敌机一代")
    else:
        print("英雄级一代 惜败 敌机一代")
    print("-" * 20)
#场景二
    h2p = AdvHeroFighter()
    e1p = EnemyFighter()
    if h2p.power() >= e1p.power():
        print("英雄机二代 战胜 敌机一代")
    else:
        print("英雄机二代 惜败 敌机一代")
#思路二：使用多态
h1p = HeroFighter()
h2p = AdvHeroFighter()
e1p = EnemyFighter()
#场景一:
object_fight(h1p,e1p)
#场景二:
object_fight(h2p,e1p)



