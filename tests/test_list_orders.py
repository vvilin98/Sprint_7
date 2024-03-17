import allure
import requests
from handle import Handle
from urls import Urls


class TestReturnOrderList:
    @allure.title('В тело ответа возвращается список заказов')
    def test_list_order(self):
        response = requests.get(f'{Urls.URL}{Handle.CREATE_ORDER}')
        assert response.status_code == 200 and "orders" in response.json()
