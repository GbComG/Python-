# 变量定义 - 未指定类型注解 ---> 类型推导
a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A", "C", "E"]
phones = {"13309091111", "15209101902", "18809019201"}
options = {"count":2 , "total":10}
goods = ("手机", 6999, 1)

names.append("X")
names.append(10010)


# 变量定义 - 指定类型注解
a2: int = 596
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str | int] = ["A", "C", "E"]
phones2: set[str] = {"13309091111", "15209101902", "18809019201"}
options2: dict[str, int] = {"count": 2, "total": 10}
goods2: tuple[str, int, int] = ("手机", 6999, 1)

#————-------------------函数-类型注解
def calc(scores:list[int]):
    return sum(scores)/len(scores)

def calc_data(scores:list[int]):
    max_v = max(scores)
    min_v = min(scores)
    avg_v = sum(scores)/len(scores)
    return max_v, min_v, avg_v