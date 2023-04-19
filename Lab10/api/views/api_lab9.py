import json
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

from api.models import Company, Vacancy


@csrf_exempt
def companies_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        company_list = [c.to_json() for c in companies]
        return JsonResponse(company_list, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        company_name = data.get('name', '')
        company = Company.objects.create(name=company_name)
        return JsonResponse(company.to_json())


@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        new_company_name = data.get('name', company.name)
        company.name = new_company_name
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})


def vacancies_by_company(request, company_id):
    try:
        vacancies = Company.objects.get(id=company_id).vacancies.all()
        vacancy_list = [c.to_json() for c in vacancies]
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse(vacancy_list, safe=False)


# Product.objects.filter(name__startswith="Pr")
# Product.objects.filter(name__contains="Pr")
# Product.objects.filter(name="Product5")
@csrf_exempt
def vacancies_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancy_list = [v.to_json() for v in vacancies]
        return JsonResponse(vacancy_list, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        vacancy_name = data.get('name', '')
        vacancy = Vacancy.objects.create(name=vacancy_name)
        return JsonResponse(vacancy.to_json())


@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        new_vacancy_name = data.get('name', vacancy.name)
        # desc = data.get('desc', category.desc)
        vacancy.name = new_vacancy_name
        vacancy.save()
        return JsonResponse(vacancy.to_json())
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'deleted': True})


def sorted_top_10_vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary').values()
    vacancy_list = []
    for i in range(10):
        vacancy_list.append(vacancies[i])
    # vacancy_list = [vacancies[i].to_json() for i in range(10)]
    return JsonResponse(vacancy_list, safe=False)
