import pytest
from coinbase_app.models import Product
from django.urls import reverse

# set test data
@pytest.fixture
def setup_products():
    Product.objects.create(ticker='BTC-USD', name='Bitcoin')
    Product.objects.create(ticker='ETH-USD', name='Ethereum')

@pytest.mark.django_db # access database
def test_product_list_view(client, setup_products):
# reverse get url
    url = reverse('product_list')
    response = client.get(url) # set a get request
# check the response status
    assert response.status_code == 200
# check context
    products =response.context['products']
    assert len(products) == 2

@pytest.mark.django_db
def test_product_detail_view(client, setup_products):
    product = Product.objects.get(ticker='BTC-USD')
    url = reverse('product_detail', args=[product.pk])
    response = client.get(url)

    assert response.status_code == 200
    assert response.context['product'] == product

@pytest.mark.django_db
def test_product_create_view(client, setup_products):
    url = reverse('product_create')
    data = {
        'ticker': 'LTC-USD',
        'name': 'Litecoin'
    }

    response = client.get(url)

    assert response.status_code == 200