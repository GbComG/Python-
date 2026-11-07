#while循环:打印十遍"人生苦短，我用python"

# i = 0
# while i < 10:
#     i += 1
#     print("人生苦短，我用python")
# else :
#     print("循环完成")


#while案例，记录0-100所有偶数的累加之和
total = 0
i = 1
while i<= 100:
    if i% 2 == 0:
        total += i
    i += 1
print(f"1-100之间偶数累加的和为:{total}")

