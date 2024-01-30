from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key' #Placeholder 


products = [
    {'id': 1, 'name': 'Product 1', 'price': 500.00},
    {'id': 2, 'name': 'Product 2', 'price': 1000.00},
    {'id': 3, 'name': 'Product 3', 'price': 780.00},
    {'id': 4, 'name': 'Product 4', 'price': 450.00},
    {'id': 5, 'name': 'Product 5', 'price': 1200.00},
    {'id': 6, 'name': 'Product 6', 'price': 400.00},
]


@app.before_request
def before_request():
    session.setdefault('cart', [])

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart = session.get('cart', [])
        cart.append(product)
        session['cart'] = cart
    return redirect(url_for('view_cart'))

@app.route('/view_cart')
def view_cart():
    cart = session.get('cart', [])
    return render_template('cart.html', cart=cart)

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    product_id = int(request.form.get('product_id'))
    cart = session.get('cart', [])
    updated_cart = [item for item in cart if item['id'] != product_id]
    session['cart'] = updated_cart
    return redirect(url_for('view_cart'))

if __name__ == '__main__':
    app.run(debug=True)
