import pytest
from unittest.mock import patch, Mock
from coinbase_app.tasks import fetch_data
from coinbase_app.models import Product, Historical
import datetime
@pytest.mark.django_db
def test_fetch_data_task():
    Product.objects.create(ticker='BTC-USD', name='Bitcoin')
    product = Product.objects.get(ticker='BTC-USD')
    # mock API response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        [1234567890, 49000.0, 51000.0, 50000.0, 50500.0, 100.0]
    ]#[timestamp, price_low, price_high, price_open, price_close]

    with patch('requests.get') as mock_get:
        mock_get.return_value = mock_response

        fetch_data()

        historical_data = Historical.objects.filter(product=product)
        assert historical_data.count() == 1
        data = historical_data.first()

        assert data.timestamp.timestamp() == 1234567890
        assert data.open == 50000.0
        assert data.high == 51000.0
        assert data.low == 49000.0
        assert data.close == 50500.0
        assert data.volume == 100.0