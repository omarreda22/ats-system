from django.shortcuts import render

from ats.models import LocalProduct
from facebook.models import FacebookProduct
from twitter.models import TwitterProduct


def store_home(request):
    query = request.GET.get("q")
    categories = request.GET.getlist("category")

    if query == None:
        query = ""

    local_products = list(LocalProduct.objects.filter(title__icontains=query))
    facebook_products = list(FacebookProduct.objects.filter(title__icontains=query))
    twitter_products = list(TwitterProduct.objects.filter(title__icontains=query))

    # Search
    if not categories:
        all_products = local_products + facebook_products + twitter_products
    else:
        all_products = []
        if "local" in categories:
            all_products += local_products
        if "facebook" in categories:
            all_products += facebook_products
        if "twitter" in categories:
            all_products += twitter_products

    products_count = len(all_products)

    all_products = sorted(all_products, key=lambda x: x.created_at, reverse=True)

    context = {
        "all_products": all_products,
        "products_count": products_count,
        "categories": categories,
    }
    return render(request, "store/home.html", context)


def store_charts(request):
    query = request.GET.get("q")
    categories = request.GET.getlist("category")

    if query == None:
        query = ""

    local_products = LocalProduct.objects.using("default").filter(
        title__icontains=query
    )
    facebook_products = FacebookProduct.objects.using("facebook_db").filter(
        title__icontains=query
    )
    twitter_products = TwitterProduct.objects.using("twitter_db").filter(
        title__icontains=query
    )

    all_products = []
    if categories:
        local_products = local_products if "local" in categories else []
        facebook_products = facebook_products if "facebook" in categories else []
        twitter_products = twitter_products if "twitter" in categories else []

    all_products_counts = [
        len(local_products),
        len(facebook_products),
        len(twitter_products),
    ]

    context = {
        "categories_items": ["Local", "Facebook", "Twitter"],
        "counts": all_products_counts,
        "categories": categories,
        "products_count": len(local_products)
        + len(facebook_products)
        + len(twitter_products),
    }
    return render(request, "store/charts.html", context)
