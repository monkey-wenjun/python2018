# -*- coding:utf-8 -*-


# 定义一个用于存放学员信息的列表变量

stulist = [
    {'name':'张三','age':20,'classid':'java'},
    {'name':'李四','age':25,'classid':'java'},
    {'name':'王五','age':15,'classid':'java'},
]


# 定义一个学员的输出函数

def showStu(stulist):

    if len(stulist) ==0:
        print("="*12,"没有学员信息可以输出","="*14)
        return

    print("|{0:<5}|{1:<10}|{2:<5}|{3:10}|".format("sid","name","age","classid"))
    print("-"*40)
    for i in range(len(stulist)):
        print("|{0:<5}|{1:<10}|{2:<5}|{3:10}|".format(i+1, stulist[i]['name'], stulist[i]['age'], stulist[i]['classid']))
        print("-" * 40)



# 输出界面
def main():
    while 1:

        print("="*12,"学员管理系统","="*14)
        print("{0:1}{1:13}{2:15}".format(" ","1.查看学员信息","2.添加学员信息"))
        print("{0:1}{1:13}{2:15}".format(" ","3.删除学员信息","4.修改学员信息"))
        print("{0:1}{1:13}{2:15}".format(" ", "5.退出系统",""))
        print("="*40)

        key = input("请输入对应的选择:")


        if key == "1":
            print("="*12,"学员信息浏览","="*14)
            showStu(stulist)
            input("按回车键继续...")

        elif key == "2":
            print("="*12,"学员信息添加","="*14)

            stu = {}
            stu['name'] = input("请输入你要添加的姓名:")
            stu['age'] = input("请输入要添加的年龄:")
            stu['classid'] = input("请输入要添加的班级信息:")
            stulist.append(stu)
            showStu(stulist)

            input("按回车键继续...")

        elif key == "3":
            print("="*12,"删除学员信息","="*14)
            sid = input("请输入你需要删除的 id 号:")

            del stulist[int(sid)-1]
            showStu(stulist)
            input("按回车键继续...")

        elif key == "4":
            showStu(stulist)
            sid = int(input("请输入你需要修改的 id 号:"))-1
            stulist[sid]["name"] = input("请输入你要修改的姓名:")
            stulist[sid]["age"] = input("请输入你要修改的姓名:")
            stulist[sid]["classid"] = input("请输入你要添加的班级信息:")
            showStu(stulist)

        elif key == "5":
            print("=" * 12, "退出系统", "=" * 14)
            break

        else:

            print("="*12,"无效的键盘输入","="*14)

if __name__ == '__main__':
    main()