from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from app.models import Product,Category
from app.forms import ProductForms,CommentModelForm,OrderModelForm
from django.db.models import Q
# Create your views here.
from django.template.defaulttags import register


def index_page(request,cat_id = None):
    filter_type = request.GET.get('filter',' ')
    categories = Category.objects.all()
    search_query = request.GET.get('search')
    if cat_id:
        products = Product.objects.filter(category = cat_id)
        if filter_type == 'expensive':
            products = products.order_by('-price')
        elif filter_type == 'cheap':
            products = products.order_by('price')

    else:
        products = Product.objects.all()
        if filter_type == 'expensive':
            products = products.order_by('-price')
        elif filter_type == 'cheap':
            products = products.order_by('price')
    if search_query:
        products = products.filter(Q(name__icontains  = search_query)|Q(description__icontains = search_query))

    context = {
        'products': products,
        'categories': categories

    }
    return render(request, 'app/home.html', context)





def detail_product(request,pk):
    
    product = Product.objects.get(id=pk)
    comments = product.comments.all().order_by('-created_at')[:2]
    count = product.comments.count()
    price_lower_bound = product.price*0.8
    price_upper_bound = product.price*1.2
    similar_products = Product.objects.filter(Q(price__gte = price_lower_bound)&Q(price__lte = price_upper_bound)).exclude(id = pk)
    context = {
        'product': product,
        'comments': comments,
        'count' : count,
        'similar_products': similar_products,
    }
    return render(request, 'app/detail.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForms(request.POST,request.FILES)
        if form.is_valid():
            name = request.POST['name']
            description = request.POST['description']
            price = request.POST['price']
            image = request.FILES['image']
            rating = request.POST['rating']
            discount = request.POST['discount']
            product = Product(name = name,description=description,price=price,image = image,rating=rating,discount=discount)
            product.save()
            return redirect('index')
    else:
        form = ProductForms()
    
    return render(request,'app/add_product.html',{'form':form})


# def add_product(request):
#     if request.method == 'POST':
#         form = ProductModelForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = ProductModelForm()
#     context = {
#         'form':form
#     }
#     return render(request, 'app/add_product.html',context)
#

def add_comment(request,pk):
    # comments = CommentModelForm.objects.all()
    product = get_object_or_404(Product,id = pk)


    # product = Product.objects.filter(id=product_id)
    form = CommentModelForm()

    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.product = product
            comment.save()
            return redirect('detail',pk)

    
    context = {
        'form':form,
        'product':product,
        
        }
    return render(request,'app/detail.html',context)


def to_order(request, pk):
    product = get_object_or_404(Product, id=pk)
    form = OrderModelForm()

    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('detail', pk)

    context = {
        'form': form,
        'product': product,

    }
    return render(request, 'app/detail.html', context)

