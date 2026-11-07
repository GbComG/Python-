#字典dict基础操作

# 类型	操作	含义	样例
# 添加	字典名称 [key] = value	往指定字典中添加 key-value 键值对	dict1 ["涛哥"] = 688
# 删除	字典名称.pop (key)	删除字典中指定的 key，并返回该 key 对应的 value	score = dict1.pop ("涛哥")
# 删除	del 字典名称 [key]	删除字典中指定的键值对	del dict1 ["涛哥"]
# 修改	字典名称 [key] = value	修改字典中指定的 key 对应的值	dict1 ["小智"] = 658
# 查询	字典名称 [key]	根据 key 获取 value	dict1 ["涛哥"]
# 查询	字典名称.get (key)	根据 key 获取 value	dict1.get ("涛哥")
# 查询	字典名称.keys ()	获取所有的 key	dict1.keys()
# 查询	字典名称.values ()	获取所有的 value	dict1.values()
# 查询	字典名称.items ()	获取所有的 key-value 键值对	dict1.items()

