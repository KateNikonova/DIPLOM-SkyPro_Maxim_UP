import pytest
from pages.main_page import MainPage
from pages.search_page import SearchPage
from data import SEARCH_PHRASES


@pytest.mark.parametrize("search_query", SEARCH_PHRASES)
@pytest.mark.search
def test_search_main(browser, search_query):
    page = MainPage(browser)
    page.open()
    page.search(search_query)

    search_page = SearchPage(browser)
    search_page.wait_for_search_results()
    results_count = search_page.get_results_count()

    assert results_count > 0
