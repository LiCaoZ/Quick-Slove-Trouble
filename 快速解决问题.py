# 引用依赖开始
from time import sleep # 引用用于停顿的模块
from urllib.parse import quote # 引用URL编码模块
from random import choice, randint # 引用用于获取金额随机数的模块
# 引用依赖结束

# 定义变量开始
app_name = "快速解决问题"
# 定义应用名以便后方引用
start_message = "欢迎使用" + app_name + "软件！希望我能帮你解决问题。"
ask_trouble = "请问您有什么问题吗？\n"
end_message = "程序运行结束，感谢您的使用，按Enter键即可退出。"
# 定义变量结束

# 应用主体开始
print(start_message) # 输出欢迎信息
sleep(1.5) # 停顿1.5s
trouble = input(ask_trouble) # 输出询问问题讯息
sleep(1.5) # 停顿1.5s
print("哦，您的问题是" + trouble) # 输出询问结果
need_pay_money = str(randint(18,25)) + "元" # 获取一个金额随机数
sleep(1.5) # 停顿1.5s
print("那么，您需要向我支付" + need_pay_money + "以获取这个问题的答案")
sleep(1.5) # 停顿1.5s
print("亦或者，您可以选择白嫖")
sleep(1.5)
choice = int(input("请输入您的选择——1.付费 2.白嫖\n"))
if choice == 1:
    print("恭喜您，您的问题马上就会解决")
elif choice == 2:
    print("那么，请您自行搜索，我们稍后会为您打印搜索链接")
    sleep(3)
    print("请复制链接前往\nhttps://cn.bing.com/search?q=" + quote(trouble, 'utf-8'))
else:
    print("？您输入了一个不存在的选项")
# 应用主体结束

input(end_message)
quit()