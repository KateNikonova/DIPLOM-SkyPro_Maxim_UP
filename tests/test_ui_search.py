import pytest
from pages.main_page import MainPage
from data import SEARCH_PHRASES


@pytest.mark.parametrize("search_query",SEARCH_PHRASES)
@pytest.mark.search
def test_search_main(browser, search_query):
    page = MainPage(browser)
    page.open()
    page.search(search_query)
    page.wait_for_search_results()
    results_count = page.get_results_count()

    assert results_count > 0
