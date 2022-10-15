from email import header
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from contact.models import contact
from contact.forms import ContactForm

# Create your views here.
'''def contactView(request):
    if(request.method == 'POST'):
        fname = request.POST.get('first_name')
        email = request.POST.get('email_address')
        telefone = request.POST.get("telephone")
        company = request.POST.get('company')
        address = request.POST.get('address')
        comment = request.POST.get('comment')

        contact.objects.create(first_name = fname, email_adress = email,company = company, telephone = telefone, address = address, comments = comment)
        # print(fname, email, telefone, company, address, comment)
    else:
        print('get')
    return render(request, 'contact_us.html')

'''

def contactView(request):
    context = {'form': ContactForm()}

    if request.method == 'POST':
        data = ContactForm(request.POST)
        if data.is_valid():
            data.save()
        else:
            context['form'] = data
            context['error'] = list(data.errors.items())[0][1][0] #bu hisse suallar yaratdi(nece isleyir)
   

    return render(request,'contact_us.html', context)

def test1(request):
    print('isledi')
    import json
    # return HttpResponse(json.dumps({'name':'sabina', 'lname':'aliyev'}), header='application/json')
    return JsonResponse({'name':'sabina', 'lname':'aliyev'})