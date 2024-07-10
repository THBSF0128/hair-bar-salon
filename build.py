import os
from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Define a function to render a template with given context and write to a file
def render_template(template_name, context, output_file):
    template = env.get_template(template_name)
    output = template.render(context)
    with open(output_file, 'w') as f:
        f.write(output)

services = [
    {'name': 'Haircuts', 'description': 'Professional haircuts for all styles.', 'price': '$30'},
    {'name': 'Coloring', 'description': 'High-quality hair coloring services.', 'price': '$50'}
    # Add more services as needed
]

products = [
    {'name': 'Shampoo', 'description': 'High-quality shampoo.', 'price': '$10', 'image': 'shampoo.jpg'},
    {'name': 'Conditioner', 'description': 'High-quality conditioner.', 'price': '$12', 'image': 'conditioner.jpg'}
    # Add more products as needed
]

# Define the pages to be generated
pages = [
    {'template': 'index.html', 'context': {'title': 'Home'}, 'output': 'dist/index.html'},
    {'template': 'services.html', 'context': {'title': 'Services', 'services': services}, 'output': 'dist/services.html'},
    {'template': 'shop.html', 'context': {'title': 'Shop', 'products': products}, 'output': 'dist/shop.html'},
    {'template': 'contact.html', 'context': {'title': 'Contact'}, 'output': 'dist/contact.html'},
    {'template': 'product.html', 'context': {'title': 'Product'}, 'output': 'dist/product.html'}
]

# Create dist directory if it doesn't exist
os.makedirs('dist', exist_ok=True)

# Render each page
for page in pages:
    render_template(page['template'], page['context'], page['output'])

print("\r\nStatic site generated.\r\n")

