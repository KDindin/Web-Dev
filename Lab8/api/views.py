from django.http.response import JsonResponse
from api.models import Product, Category


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    products_list = [p.to_json() for p in products]
    return JsonResponse(products_list, safe=False)


def product_detail(request, product_id):
    products = Product.objects.all()
    products_list = [p.to_json() for p in products]
    for product in products_list:
        if product['id'] == product_id:
            return JsonResponse(product)
    return JsonResponse({'error': 'Product not found'})


def category_list(request):
    categories = Category.objects.all()
    categories_list = [c.to_json() for c in categories]
    return JsonResponse(categories_list, safe=False)


def category_detail(request, category_id):
    categories = Category.objects.all()
    categories_list = [c.to_json() for c in categories]
    for category in categories_list:
        if category['id'] == category_id:
            return JsonResponse(category)
    return JsonResponse({'error': 'Category not found'})


def products_by_category(request, category_id):
    categories = Category.objects.all()
    categories_list = [c.to_json() for c in categories]
    category_name = ''
    for category in categories_list:
        if category['id'] == category_id:
            category_name = category['name']
    products = Product.objects.all()
    products_list = [p.to_json() for p in products]
    selected_products = []
    for product in products_list:
        if product['description'] == category_name:
            selected_products.append(product)
    if selected_products:
        return JsonResponse(selected_products, safe=False)
    return JsonResponse({'error': 'Products not found'})

