# 准备工作
```python
pip install -r requirements.txt
```

本项目借助百度文字识别实现功能，因此你需要拥有账号，具体可以参考https://www.bilibili.com/video/BV1MJ411b78R   
获取应用的AppID、API Key、Secret Key分别填入test.py的第13、14、15行
# 如何使用
首先你需要打开wjx链接会出现的聊天框，注意是双击显示单独的聊天框，并保证窗口足够宽使wjx链接在一行内；  
接着运行get_window.py来获取该窗口的名称，将test.py第21行的“'群聊'”替换成该窗口的名称；  
你需要知道wjx的题目格式，将内容填写到第39行；  
提前点时间运行代码，记住在运行代码前以及中途不要最小化目标聊天框，接着仅需要等待即可。
