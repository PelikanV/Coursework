from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View
from store.models.reviewrating import Review
from store.models.reviewrating import Customer
class Index(View):
    def post(self , request):
        product = request.POST.get('product')
        print(product)
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1

                else:
                    cart[product]  = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return HttpResponseRedirect("http://127.0.0.1:8000/store")
    def get(self , request):
        return render(request, 'homepage.html')
    def details(self,request):
        return render(request,"detailpage.html")
def store(request):
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)

def product_detail(request,*args,**kwargs):
    id = kwargs.get("id")
    product1 = Products.get_product_by_id(id)

    context ={
        "product": product1,
        "reviews" : Review.objects.filter(product = product1),
    }
    if (request.method == "POST"):
        customer = Customer.objects.get(user=request.user)
        product = product1
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        review = Review.objects.create(product=product, user=customer, rating=rating, comment=comment)
        review.save()
    return render(request, 'detailpage.html',context)



def cart(request):
    if request.session.get("cart"):
        ids = list(request.session.get('cart').keys())
    else:
        ids = []
    products = Products.get_products_by_id(ids)
    return render(request, 'cart.html', {'products': products, "ids": ids})
