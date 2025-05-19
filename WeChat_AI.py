from openai import OpenAI
from wxauto import *


client = OpenAI(
    api_key = "<DeepSeek API Key>", 
    base_url = "https://api.deepseek.com"
)
wx = WeChat()
while True:
    m = wx.GetNextNewMessage()
    for user, l in m.items():
        for m in l:
            if m.type == "friend":
                response = client.chat.completions.create(
                    model = "deepseek-chat",
                    messages = [
                        {"role": "system", "content": """
                            你的名字是“智能助手”，
                            你是一位精通高情商沟通技巧的专家，擅长根据不同的情境和对象，
                            调整沟通方式，使回复既得体又富有同理心，能够有效缓解紧张情绪，
                            促进积极的社交互动。你具备敏锐的社交洞察力、出色的情绪管理能
                        """},
                        {"role": "user", "content": m.content},
                    ],
                    stream = False
                )
                wx.SendMsg(msg = esponse.choices[0].message.content, who = user)
                print("来自", user)
                print("TA:", m.content)
            elif m.type == "self":
                print("ME", m.content)
            else:
                print(m.type, m.content)

