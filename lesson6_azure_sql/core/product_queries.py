from django.shortcuts import render
import random
from .models import Product, Category, Tag

def seed():
    Product.objects.create(
        name = "product1",
        price = round(random.uniform(100, 1000),2),
        description = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.",
        image_path = 'http://eheziskel.lr/mov'
    )
    
    Product.objects.create(
        name = "product2",
        price = round(random.uniform(100, 1000),2),
        description = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.",
        image_path = 'http://eheziskel.lr/mov'
    )
    
    Product.objects.create(
        name = "product3",
        price = round(random.uniform(100, 1000),2),
        image_path = 'http://eheziskel.lr/mov'
    )
    
    Product.objects.create(
        name = "product4",
        price = round(random.uniform(100, 1000),2),
    )
    
    Product.objects.create(
        name = "product5",
        price = round(random.uniform(100, 1000),2),
        description = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.",
    )
    
    Product.objects.create(
        name = "product6",
        price = round(random.uniform(100, 1000),2),
    )
    
    Product.objects.create(
        name = "product7",
        price = round(random.uniform(100, 1000),2),
        description = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.",
        image_path = 'http://eheziskel.lr/mov'
    )
    
def print_product(product):
    if not product:
        print("Product is null")
        return
    print("="*20)
    print(product)
    print("="*20)
    
def print_products(products):
    if not products or len(products)<=0:
        print("No products")
        return
    
    print(f"\n{"-"*20} Start printing {"-"*20}")
    for item in products:
        print_product(item)
    print(f"\n{"-"*20} End printing {"-"*20}")

def tag_seed():
    Tag(name="New").save()
    Tag(name="Hit").save()
    Tag(name="Sale").save()
    Tag(name="Limited").save()
    Tag(name="Recommended").save()
    Tag(name="In-Stock").save()
    Tag(name="Coming Soon").save()

# tag_seed()

def category_seed():
    Category(name="Smartphones").save()
    Category(name="Laptops").save()
    Category(name="Clothes").save()
    Category(name="Food").save()
    Category(name="Toys").save()
    
# category_seed()

