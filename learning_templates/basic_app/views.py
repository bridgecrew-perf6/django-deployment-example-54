from django.shortcuts import render


# Create your views here.
def index(request):
    mytext = {'insert_text':'i am going to get 15lakhs package from TCS for the position which I have interviewed for on 29th Jan 2022', 'before':'14-FEB-2022', 'num':90}
    return render(request,'basic_app/index.html', mytext)


def other(request):
    return render(request,'basic_app/other.html')


def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
