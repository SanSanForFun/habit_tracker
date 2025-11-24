import stripe
import os

stripe.api_key = os.getenv('STRIPE_API')


# Create Product
def create_stripe_product(create):
    """ Создает продукт в страйпе """
    product_name = create.course if create.course else create.lesson
    return stripe.Product.create(name=product_name)


# Create Price
def create_stripe_price(amount):
    """ Создает цену в страйпе """
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": "Course"},
    )


# Create Session
def create_stripe_session(price):
    """ Создает сессию на оплату """
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')
