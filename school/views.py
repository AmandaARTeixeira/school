from django.http import JsonResponse

def students(request):
    if request.method == 'GET':
        estudante = {
            'id':'1',
            'name':'amanda'
        }

        return JsonResponse(estudante)
