from django.http import JsonResponse
from api.models import Company, Vacancy


def companies_list(request):
    companies = Company.objects.all()
    company_list = [c.to_json() for c in companies]
    return JsonResponse(company_list, safe=False)


def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse(company.to_json())


def vacancies_by_company(request, company_id):
    try:
        vacancies = Company.objects.get(id=company_id).vacancies.all()
        vacancy_list = [c.to_json() for c in vacancies]
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    # vacancies = Company.objects.get(id=company_id).vacancies.all()
    # vacancy_list = [c.to_json() for c in vacancies]
    return JsonResponse(vacancy_list, safe=False)


# Product.objects.filter(name__startswith="Pr")
# Product.objects.filter(name__contains="Pr")
# Product.objects.filter(name="Product5")
def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    vacancy_list = [v.to_json() for v in vacancies]
    return JsonResponse(vacancy_list, safe=False)


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse(vacancy.to_json())


def sorted_top_10_vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary').values()
    vacancy_list = []
    for i in range(10):
        vacancy_list.append(vacancies[i])
    # vacancy_list = [vacancies[i].to_json() for i in range(10)]
    return JsonResponse(vacancy_list, safe=False)
