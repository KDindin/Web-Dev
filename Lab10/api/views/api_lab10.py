import json
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from api.models import Company, Vacancy

# CRUD - CRATE, READ, UPDATE, DELETE
from api.serializers import CompanySerializer1, CompanySerializer2
from api.serializers import VacancySerializer1, VacancySerializer2


@csrf_exempt
def companies_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer1(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
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
        # desc = data.get('desc', category.desc)
        company.name = new_company_name
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})


def vacancies_list(request):
    # select * from auth_product;
    products = Vacancy.objects.all()
    products_json = [p.to_json() for p in products]
    return JsonResponse(products_json, safe=False)


def vacancy_detail(request, product_id):
    try:
        product = Vacancy.objects.get(id=product_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse(product.to_json())
