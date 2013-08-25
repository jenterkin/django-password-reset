from django.contrib.auth.models import (
        User,
        AnonymousUser,
    )
from django.core.exceptions import (
        PermissionDenied,
        ObjectDoesNotExist,
    )
from password_reset.models import (
        Burn,
    )
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson
from django.core import serializers
from django.core.mail import EmailMessage

@csrf_exempt
@require_http_methods(['POST'])
def request_link(request):
    '''
    Creates burn link for user and sends email with link
    '''
    user = User.objects.get(username=request.POST['username'])
    if not user:
        data = simplejson.dumps({'message': 'Invalid username'})
        return HttpResponse(data, status=403)
    try:
        burner = Burn.objects.get(user=user)
    except:
        burner = Burn()
        burner.user = user
        burner.reset()
        burner.save()

    link =  'home.cspuredesign.com/labaide/app/#/chg_password?link={}' \
            .format(Burn.objects.get(user=user).link)
    body =  ''' 
            <html>
                <body>
                    <a href={}>Here is your password reset link.</a> <br />
                    <img src=http://static.giantbomb.com/uploads/original/1/17172/1419618-unicorn2.jpg> <br />
                </body> 
            </html>
            ''' \
            .format(link)

    email = EmailMessage('Password Reset', body, to=[user.email])
    email.content_subtype = 'html'
    try:
        email.send()
    except:
        data = simplejson.dumps({'message': 'Could not send email'})
        return HttpResponse(data, status=400)
    data = simplejson.dumps({'message': ''})
    return HttpResponse(data, status=200, mimetype='application/json')

@csrf_exempt
@require_http_methods(['POST'])
def reset(request):
    try:
        burner = Burn.objects.get(link=request.POST['link'])
        user = burner.user
        user.set_password(request.POST['password'])
        user.save()
        data = simplejson.dumps({'message': 'Password reset'})
        burner.delete()
        return HttpResponse(data, status=200)
    except:
        data = simplejson.dumps({'message': 'Error resetting password'})
        return HttpResponse(data, status=400)
