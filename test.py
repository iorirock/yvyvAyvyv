import time
import random
food = ['鸡','鸭','鱼','肉','菜','蛋','面']
res = ['KFC','麦当劳','德克士','老娘舅','全聚德','达美乐']

def welcome():      #欢迎语
    print('欢迎使用“选择困难症助手”！')
    time.sleep(1)
    print('今天中午吃什么呢？\n1.随机食物\n2.随机餐厅\n3.自定义\n4.退出')

def print_choice(a):      #选择
    print('系统帮您选择了%s。您满意么？满意请输入1，不满意请输入2：'%a)

def end_choice(a):     #结束语
    print('您的选择是%s,感谢使用！'%a)

def get_res():      #取得餐厅列表
    res_reserve = []
    print('请输入您心仪的三家餐厅')
    for i in range(3):
        a = input('请输入第%s家餐厅'%(i+1))
        res_reserve.append(a)
    return(res_reserve)

welcome()
main_choice = int(input('请选择：'))
while main_choice == 1:
    food_try = random.choice(food)
    print_choice(food_try)
    a = int(input('请选择'))
    if a == 1:
        end_choice(food_try)
        break

while main_choice == 2:
    res_try = random.choice(res)
    print_choice(res_try)
    a = int(input('请选择'))
    if a == 1:
        end_choice(res_try)
        break

if main_choice == 3:
    res3 = get_res()
    while True:
        res_try = random.choice(res3)
        print_choice(res_try)
        a = int(input('请选择'))
        if a == 1:
            end_choice(res_try)
            break

elif main_choice == 4:
    end_choice('“结束”')

