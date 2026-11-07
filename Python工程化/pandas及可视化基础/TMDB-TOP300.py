from matplotlib.axes import Axes
import pandas as pd
import matplotlib.pyplot as plt


def load_movie_data(file_path: str) -> pd.DataFrame:
    print(f"正在加载文件：{file_path}")
    df = pd.read_csv(
        file_path,
        usecols=['电影名', '年份', '上映时间', '类型', '时长', '评分', '语言'],
        dtype={'年份': 'Int64'}
    )
    print("原始缺失值：")
    print(df.isnull().sum())

    # 填充年份：优先用上映时间前4位
    df['年份'] = df['年份'].astype('object').fillna(df['上映时间'].str[0:4])
    # 转成字符串，防止混合类型报错
    df['年份'] = df['年份'].astype(str)
    print("数据加载完成，总行数：", len(df))
    return df


def plot_year_trend(ax: Axes, df: pd.DataFrame):
    year_count = df.groupby('年份')['年份'].count()
    # 转数字，过滤掉无法转数字的脏数据
    year_count.index = pd.to_numeric(year_count.index, errors='coerce')
    year_count = year_count.dropna()
    if len(year_count) == 0:
        ax.text(0.5, 0.5, "无有效年份数据", ha="center")
        return

    min_year = int(year_count.index.min())
    max_year = int(year_count.index.max())
    x = [i for i in range(min_year, max_year + 1)]
    y = [int(year_count.get(i, 0)) for i in x]

    ax.plot(x, y, color='green')
    ax.set_title('每年高分电影数量变化折线图', fontsize=20)
    ax.set_xlabel('年份', fontsize=12)
    ax.set_ylabel('电影数量', fontsize=12)
    ax.set_xticks(x[::8])
    y_ticks = list(range(0, 31, 3))
    ax.set_yticks(y_ticks)
    ax.grid(linestyle='--', alpha=0.5)


def plot_language_bar(ax: Axes, df: pd.DataFrame):
    language_count = df.groupby('语言')['语言'].count().sort_values(ascending=False)
    x_language = language_count.index.tolist()
    y_language_count = language_count.values.tolist()

    ax.bar(x_language, y_language_count, color='green', width=0.8)
    ax.set_title('不同语言电影数量柱状图', fontsize=20)
    ax.set_xlabel('语言', fontsize=12)
    ax.set_ylabel('电影数量', fontsize=12)
    ax.grid(linestyle='--', alpha=0.5)
    ax.tick_params(axis='x', rotation=90)


def plot_genre_bar(ax: Axes, df: pd.DataFrame):
    type_count = {}
    for types in df['类型'].str.split(','):
        for t in types:
            t = t.strip()
            type_count[t] = type_count.get(t, 0) + 1
    sorted_type = sorted(type_count.items(), key=lambda item: item[1], reverse=True)
    x_type = [item[0] for item in sorted_type]
    y_type = [item[1] for item in sorted_type]

    ax.bar(x_type, y_type, color='green')
    ax.set_title('不同类型电影数量', fontsize=20)
    ax.set_xlabel('类型', fontsize=12)
    ax.set_ylabel('电影数量', fontsize=12)
    ax.grid(linestyle='--', alpha=0.5)
    ax.tick_params(axis='x', rotation=90)


def plot_score_pie(ax: Axes, df: pd.DataFrame):
    score_count = df.groupby('评分')['评分'].count().sort_values(ascending=False)
    total = score_count.sum()
    threshold = total * 0.02

    large_scores = score_count[score_count >= threshold].copy()
    small_sum = score_count[score_count < threshold].sum()
    if small_sum > 0:
        large_scores['其他'] = small_sum

    scores = large_scores.index.tolist()
    scores_values = large_scores.values.tolist()

    ax.pie(
        scores_values,
        labels=scores,
        autopct='%1.1f%%',
        shadow=False,
        startangle=90,
        radius=1.2
    )
    ax.set_title('不同评分电影占比', fontsize=20, y=1.08)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))


def draw_tmdb_report(data_path: str, save_img_path: str = "TMDB-TOP300.png"):
    # 字体容错：优先SimHei，找不到就用默认
    try:
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
    except Exception as e:
        print("SimHei字体加载失败，中文会变成方框，不影响运行：", e)

    df = load_movie_data(data_path)

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
    fig.suptitle('TMDB-TOP300 电影榜单数据统计', fontsize=25, x=0.5, y=0.98)
    fig.subplots_adjust(hspace=0.6, wspace=0.3)

    ax1: Axes = axes[0, 0]
    ax2: Axes = axes[0, 1]
    ax3: Axes = axes[1, 0]
    ax4: Axes = axes[1, 1]

    plot_year_trend(ax1, df)
    plot_language_bar(ax2, df)
    plot_genre_bar(ax3, df)
    plot_score_pie(ax4, df)

    plt.savefig(save_img_path, bbox_inches="tight")
    print(f"图片已经保存到：{save_img_path}")
    # 重点：如果plt.show不弹窗，可以先注释掉show，直接去文件夹看图片是否生成
    plt.show()


if __name__ == "__main__":
    try:
        CSV_PATH = r"C:\Users\LENOVO\Desktop\movies.csv"
        draw_tmdb_report(CSV_PATH)
    except Exception as err:
        print("程序报错：", err)
        input("按回车关闭窗口（防止控制台一闪而过）")
