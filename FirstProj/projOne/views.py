from django.shortcuts import render


# Create your views here.
def index(req):
    insert_me = "Welcome"
    return render(req, "index.html", {'insert_me': insert_me})
    # return HttpResponse("Welcome To Django !\n signup/ to see new page !")


def reg(request):
    print("Sign up is executed")
    name = request.POST.get('name')
    age = request.POST.get('age')
    dob = request.POST.get('dob')
    gen = request.POST.get('gender')
    mob = request.POST.get('mobile')
    email = request.POST.get('email')
    m_t = request.POST.get('mother_tongue')
    print(name)
    print(age)
    print(dob)
    print(gen)
    print(mob)
    print(email)
    print(m_t)

    my_dic = {
        'name': name,
        'age': age,
        'dob': dob,
        'gen': gen,
        'mob': mob,
        'email': email,
        'm_t': m_t
    }

    print(my_dic)

    return render(request, "signup.html", {'my_dic': my_dic})
