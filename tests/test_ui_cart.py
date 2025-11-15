import pytest
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.cart_page import CartPage
from data import SEARCH_FOR_CART_PHRASES


@pytest.mark.parametrize("search_query", SEARCH_FOR_CART_PHRASES)
@pytest.mark.cart
def test_add_to_cart_flow(browser, search_query):
    """Тест поиску и добавлению товара в корзину"""
    main_page = MainPage(browser)
    main_page.open()
    main_page.search(search_query)

    search_page = SearchPage(browser)
    search_page.wait_for_search_results()
    search_page.add_first_product_to_cart()
    search_page.go_to_cart()

    cart_page = CartPage(browser)

    assert cart_page.get_cart_items_count() == 1
