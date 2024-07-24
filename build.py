import os
import json
from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Define a function to render a template with given context and write to a file
def render_template(template_name, context, output_file):
    template = env.get_template(template_name)
    output = template.render(context)
    with open(output_file, 'w') as f:
        f.write(output)

def render_products(items):
    for i in range(len(items)):
        current = items[i]
        prev_item = items[i - 1] if i > 0 else None
        next_item = items[i + 1] if i < len(items) - 1 else None
        
        prev_url = ''
        next_url = ''
        if prev_item:
            prev_url = f"{prev_item['data-item-url']}.html"
        if next_item:
            next_url = f"{next_item['data-item-url']}.html"

        context = {
          'title' : current['data-item-name'],
          'product': current,
          'next' : next_url,
          'prev' : prev_url
        }
        template = env.get_template('shop-item.njk')
        output = template.render(context)
        output_file = f"product-page/{current['data-item-id']}.html"
        with open(output_file, 'w') as f:
            f.write(output)

#products = [
#    {'name': 'Shampoo', 'description': 'High-quality shampoo.', 'price': '$10', 'image': 'shampoo.jpg'},
#    {'name': 'Conditioner', 'description': 'High-quality conditioner.', 'price': '$12', 'image': 'conditioner.jpg'}
#]
with open('products.json', 'r') as file:
    products = json.load(file)

# Define the pages to be generated
pages = [
    {'template': 'index.html', 'context': {'title': 'Home'}, 'output': 'index.html'},
    {'template': 'shop.html', 'context': {'title': 'Shop', 'products': products}, 'output': 'shop.html'},
    {'template': 'contact.html', 'context': {'title': 'Contact'}, 'output': 'contact.html'},
    {'template': 'product.html', 'context': {'title': 'Product'}, 'output': 'product.html'},
    {'template': 'services.html', 'context': {'title': 'Services'}, 'output': 'services.html'},
    {'template': 'book-online.html', 'context': {'title': 'Booking'}, 'output': 'book-online.html'},
    {'template': 'education.html', 'context': {'title': 'Education'}, 'output': 'education.html'}
]

# Render each page
for page in pages:
    render_template(page['template'], page['context'], page['output'])

render_products(products)

print("\r\nStatic site generated.\r\n")
