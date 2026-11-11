# 任务背景
#
# 你正在开发一个跑步训练数据分析程序。现在有一批训练记录，你需要清洗数据、筛选有效记录，并统计训练情况。
#
# 原始数据如下：
from idlelib.autocomplete import TRY_A
from unittest import expectedFailure

# 第一关：数据清洗
# 遍历 records，筛选出有效的训练记录。
# 一条记录只有同时满足以下条件才有效：
# • distance 大于 0。
# • minutes 大于 0。
# • date 和 type 不为空。
# 要求：
# 1. 创建一个新的列表 valid_records 保存有效记录。
# 2. 不要直接删除或修改原始的 records。
# 3. 输出有效记录的数量


records = [
    {"date": "2026-10-01", "distance": 10.0, "minutes": 42, "type": "有氧跑"},
    {"date": "2026-10-02", "distance": 5.0, "minutes": 22, "type": "间歇跑"},
    {"date": "2026-10-03", "distance": 0, "minutes": 0, "type": "有氧跑"},
    {"date": "2026-10-04", "distance": 8.0, "minutes": 36, "type": "有氧跑"},
    {"date": "2026-10-05", "distance": 12.0, "minutes": 55, "type": "长距离"},
    {"date": "2026-10-06", "distance": -3.0, "minutes": 15, "type": "有氧跑"},
    {"date": "2026-10-07", "distance": 6.0, "minutes": 30, "type": "间歇跑"},
    {"date": "2026-10-08", "distance": "八公里", "minutes": 35, "type": "有氧跑"}
]


def filter_record(records):
    valid_records = []
    for i, record in enumerate(records):
        try:
            distance = float(record["distance"])
            minutes = float(record["minutes"])
        except (ValueError, TypeError):
            print(f"第{i + 1}条记录的数据格式不正确，已跳过")
            continue
        except KeyError:
            print(f"第{i + 1}条记录缺少必要字段，已跳过")
            continue
    # 检查里程和时间是否大于 0
        if distance <= 0 or minutes <= 0:
            print(f"第{i + 1}条记录的里程或时间不合法，已跳过")
            continue

    # 检查日期和训练类型是否存在且不为空
        date = str(record.get("date") or "").strip()
        training_type = str(record.get("type") or "").strip()

        if not date or not training_type:
            print(f"第{i + 1}条记录的日期或训练类型为空，已跳过")
            continue


        # 保存到新列表，不修改原始 records
        new_record = record.copy()
        new_record["distance"] = distance
        new_record["minutes"] = minutes
        new_record["pace"] = round(minutes / distance, 2)

        valid_records.append(new_record)
    return valid_records

#调用函数
valid_records = filter_record(records)

#输出结果
print(f"\n有效数据共有 {len(valid_records)} 条")
print("有效记录如下：")

for record in valid_records:
    print(record)

#三：计算有效数据的总里程

distance_sum = 0
time_sum = 0
average_pace = 0
slow_type = 0 #有氧跑出现的次数
jian_type = 0 #间歇出现的次数
long_type = 0 #长距离出现的次数
max_distance = valid_records[0] #最长距离数
fastest_record = valid_records[0] #最快速度
for k in range(len(valid_records)):
    distance_sum += valid_records [k]["distance"]
    time_sum += valid_records[k]["minutes"]
    #统计每种训练类型出现的次数
    if valid_records[k]["type"] == "有氧跑":
        slow_type += 1
    elif valid_records[k]["type"] == "间歇跑":
        jian_type += 1
    elif valid_records[k]["type"] == "长距离":
        long_type += 1
    # 找出最长训练
    if valid_records[k]["distance"] > max_distance["distance"]:
        max_distance = valid_records[k]

    # 找出最快配速训练
    if valid_records[k]["pace"] < fastest_record["pace"]:
        fastest_record = valid_records[k]
#输出总里程和总时间
print(f"有效数据的总里程为{distance_sum}")
print(f"有效数据的总时间为{time_sum}")

#计算并输出有效数据的平均配速
average_pace = round(time_sum / distance_sum, 2)
print(f"有效数据的平均配速为{average_pace}")

#输出每种训练类型出现的次数
print(f"有氧跑出现的次数为{slow_type}")
print(f"间歇跑出现的次数为{jian_type}")
print(f"长距离出现的次数为{long_type}")

#找出最长训练和最快配速训练
print("\n最长训练记录：")
print(f"日期：{max_distance['date']}")
print(f"距离：{max_distance['distance']} km")
print(f"时间：{max_distance['minutes']} 分钟")
print(f"配速：{max_distance['pace']} 分钟/公里")

print("\n最快配速训练记录：")
print(f"日期：{fastest_record['date']}")
print(f"距离：{fastest_record['distance']} km")
print(f"时间：{fastest_record['minutes']} 分钟")
print(f"配速：{fastest_record['pace']} 分钟/公里")

long_records = []

for k in range(len(valid_records)):
    if valid_records[k]["distance"] >= 8:
        long_records.append(valid_records[k])

print("\n距离大于等于 8 km 的训练记录：")
print(f"共找到 {len(long_records)} 条记录")

for k in range(len(long_records)):
    print(long_records[k])

