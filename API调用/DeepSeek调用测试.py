# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
#创建与AI大模型交互的客户端对象 DEEPSEEK_API_KEY环境变量的名字，值就是DeepSeek API_KEY的值
client = OpenAI(    api_key=os.environ.get('DEEPSEEK_API_KEY'),   base_url="https://api.deepseek.com")
#与AI大模型进行交互
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=["""帮我生成一个适用于 Windows 10/11 的爱心弹窗程序，不依赖 Python，使用 PowerShell + WinForms 实现，生成.ps1脚本和可双击启动的 BAT 文件。
程序启动后，第一个弹窗出现在爱心顶部缺口处，随后立即向右连续生成弹窗，不要出现额外停顿。
弹窗按照顶部缺口、右上弧线、右侧、底部尖角、左侧、左上弧线的顺序逐渐组成完整爱心。
爱心阶段使用约128个弹窗，弹窗必须沿轮廓均匀排列，每次只出现一个，不能跳跃、倒退或在相同位置重复生成。
每个新弹窗都必须覆盖在旧弹窗上方，让窗口产生按顺序不断堆叠的视觉效果，不能跑到旧窗口下面。
爱心尽量占据屏幕中央的大部分区域，并根据屏幕分辨率自动缩放，不能超出屏幕边缘。
每个弹窗约166×92像素，保留Windows系统标题栏，标题显示“♡”，正文使用微软雅黑并居中显示。
弹窗背景随机使用青色、绿色、粉色、淡黄色、洋红色和浅蓝色，整体风格明亮柔和"
    """
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)
#输出大模型返回的结果
print(response.choices[0].message.content)
