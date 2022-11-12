from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.views.decorators.http import require_GET, require_POST

from django.views.generic import FormView

from .models import Product, Category, Review, UserProfile
from .forms import ProductForm, ReviewForm

# Create your views here.


def all_products(request):
    """ a View to return allproducts page """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'brand':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('brand'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(brand__icontains=query) 
            products = products.filter(queries)

    currrent_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'currrent_sorting': currrent_sorting,
    }
 
    return render(request, 'products/products.html', context)


# def product_detail(request, product_id):
#     """ a View to return individual product details page """

#     product = get_object_or_404(Product, pk=product_id)
#     reviews = product.reviews.all()

#     context = {
#         'product': product,
#         'reviews': reviews,
#         'review_form': ReviewForm(),
#     }

#     return render(request, 'products/product_detail.html', context)




def product_detail(request, product_id):
    """ a View to return individual product details page """

    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.filter(product=product)
    
    template = 'products/product_detail.html'
    context = {
        'product': product,
        'reviews': reviews,
    }

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                # We're only getting the review text from the frontend. We need to associate
                # the product and logged-in user ourselves.
                # Create review object but don't commit to database yet.
                review = form.save(commit=False)
                review.product = product

                review.user = request.user
                review.save()

        else:
            form = ReviewForm()

        context['form'] = form

    return render(request, template, context)


@login_required
@require_POST
def add_review(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    form = ReviewForm(request.POST)
    if form.is_valid():
        # We're only getting the review text from the frontend. We need to associate
        # the product and logged-in user ourselves.
        # Create review object but don't commit to database yet.
        review = form.save(commit=False)
        review.product = product

        review.user = request.user
        review.save()

    return redirect(reverse('product_detail', product_id=product_id))




















@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the shop owner can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the shop owner can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the shop owner can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted.')
    return redirect(reverse('products'))
