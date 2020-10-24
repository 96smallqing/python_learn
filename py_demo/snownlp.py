Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from snownlp import SnowNLP
>>> s = SnowNLP("这个人真帅啊")
>>> s
<snownlp.SnowNLP object at 0x000001A7B1EF8248>
>>> s.sentiments
0.5443456329515354
>>> s.words
['这个', '人', '真帅', '啊']
>>> s.pinyin
['zhe', 'ge', 'ren', 'zhen', 'shuai', 'a']
>>> s.tf
[{'这': 1}, {'个': 1}, {'人': 1}, {'真': 1}, {'帅': 1}, {'啊': 1}]
>>> s.idf
{'这': 1.2992829841302609, '个': 1.2992829841302609, '人': 1.2992829841302609, '真': 1.2992829841302609, '帅': 1.2992829841302609, '啊': 1.2992829841302609}
>>> text = '你好啊，我吃饭了，一起去学嵌入式吧'
>>> s=SnowNLP(text)
>>> s.sentences
['你好啊', '我吃饭了', '一起去学嵌入式吧']
>>> s.sentiments
0.6010889886991343
>>> s.keywords(4)
['入式', '学嵌', '去']
>>> s.summary
<bound method SnowNLP.summary of <snownlp.SnowNLP object at 0x000001A7B1F0D108>>
>>> s.summary(2)
['你好啊', '我吃饭了']
>>> s.words
['你', '好', '啊', '，', '我', '吃饭', '了', '，', '一起', '去', '学嵌', '入式', '吧']
>>> 
