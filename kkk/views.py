from django.shortcuts import render,redirect
from kkk.models import Grade,Student

from django.http import HttpResponse
def insert(request):
    g1 = Grade(g_name="大数据一班")
    g2 = Grade(g_name="大数据二班")
    g3 = Grade(g_name="大数据三班")

    g1.save()
    g2.save()
    g3.save()

    Student.objects.create(s_name="甲",phone="133****5855",email="145@qq.com",password="123456",g=g1,sex ="男",age = 18,zhiwei="同学")
    Student.objects.create(s_name="乙",phone="153****7754",email="134@qq.com",password="123456",g=g1,sex ="男",age = 18,zhiwei="同学")

    Student.objects.create(s_name="龙",phone="133****5855",email="145@qq.com",password="123456",g=g2,sex ="男",age = 18,zhiwei="同学")
    Student.objects.create(s_name="蛇",phone="133****5855",email="145@qq.com",password="123456",g=g2,sex ="男",age = 18,zhiwei="同学")

    Student.objects.create(s_name="狗",phone="133****5855",email="145@qq.com",password="123456",g=g3,sex ="男",age = 18,zhiwei="同学")
    Student.objects.create(s_name="猫",phone="133****5855",email="145@qq.com",password="123456",g=g3,sex ="男",age = 18,zhiwei="同学")

    return HttpResponse("数据添加成功")


# def login(request):
#     if request.method == "POST":
#
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         s1 =  Student.objects.filter(email=email,password=password)
#         if s1:
#             print("登陆成功")
#             return redirect("show")
#         else:
#             print("登录失败")
#             return redirect("login")
#     else:
#         return render(request,"login.html")

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")
        s1 = Student.objects.filter(email=email,password=password)
        if s1:
            return redirect("show")
        else:
            return redirect("login")


def show(request):
    g_all = Grade.objects.all()
    s_all = Student.objects.all()

    if request.method == "GET":
        return render(request,"show.html",{
            'g_all':g_all,
            's_all':s_all
        })
    # else:
    #     g_name = request.POST.get("g_name")
    #     sex = request.POST.get("sex")
    #     zhiwei = request.POST.get("zhiwei")
    #
    #     #查询班级
    #     if g_name:
    #         one_g = Grade.objects.filter(g_name=g_name).first()
    #         #通过班级、班级所对应的学生
    #         filter_s = Student.objects.filter(g=one_g).all()
    #         return render(request, "show_filter.html", {
    #             'filter_s': filter_s,
    #         })





def one_insert(request):
    if request.method == "GET":
        return render(request,"one_insert.html")
    else:
        g_name = request.POST.get("g_name")
        s_name = request.POST.get("s_name")
        sex = request.POST.get("sex")
        age = request.POST.get("age")
        zhiwei = request.POST.get("zhiwei")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")

        g1 = Grade.objects.filter(g_name=g_name).first()
        if g1:
            Student.objects.create(s_name=s_name,sex=sex,age=age,zhiwei=zhiwei,phone=phone,email=email,password=password,g=g1)

        else:
            new_g = Grade(g_name=g_name)
            new_g.save()
            Student.objects.create(s_name=s_name, sex=sex, age=age, zhiwei=zhiwei, phone=phone, email=email,password=password, g=new_g)
        return redirect("show")



def update(request,id):
    s1 = Student.objects.filter(id=id).first()
    if request.method == "GET":
        return render(request,"update.html",{"s1":s1})
    else:

        g_name = request.POST.get("g_name")
        s_name = request.POST.get("s_name")
        sex = request.POST.get("sex")
        age = request.POST.get("age")
        zhiwei = request.POST.get("zhiwei")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")


        if g_name:
            g1 = Grade.objects.filter(g_name=g_name).first()
            if g1:
                s1.g = g1
            else:
                new_g = Grade(g_name=g_name)
                new_g.save()
                s1.g = new_g

        if s_name:
            s1.s_name = s_name
        if sex:
            s1.sex = sex
        if age:
            s1.age = age

        if zhiwei:
            s1.zhiwei = zhiwei
        if phone:
            s1.phone = phone
        if email:
            s1.email = email
        if password:
            s1.password = password
        s1.save()
        return redirect("show")




def delete(request,id):
    s1 = Student.objects.filter(id=id).first()
    s1.delete()
    return redirect("show")