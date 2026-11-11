"""
案例：基于传入的数值（每批次的歌词条数），创建生成器，生成批次歌词
"""


#需求:基于文件中 周杰伦的歌词，创建生成器，根据传入的每批次的歌词条数，生成歌词批次.
#1.定义函数，接受每批次的歌词条数，返回生成器
def dataset_loader(batch_size):
    """
    自定义的 歌词批量生成器
    :param batch_size:每批次的歌词条数
    :return: 生成器，每个元素都是一批次的数据，例如（8条，8条...）
    """

    def dataset_loader(batch_size):
        """
        自定义歌词批量生成器
        """
        with open('./jaychou.txt', 'r', encoding='utf-8') as src_file:
            # 读取所有歌词，得到列表
            lines = src_file.readlines()

            # 计算批次总数，向上取整
            total_batch = (len(lines) + batch_size - 1) // batch_size

            # 逐批生成歌词
            for i in range(total_batch):
                yield lines[i * batch_size:(i + 1) * batch_size]

    # 创建生成器
    loader = dataset_loader(8)

    # 遍历生成器
    for batch in loader:
        print(batch)
