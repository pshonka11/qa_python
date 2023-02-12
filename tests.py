import pytest


class BooksCollector:
    def __init__(self):
        self.books_rating = {}
        self.favorites = []

    def add_new_book(self, name):
        if not self.books_rating.get(name):
            self.books_rating[name] = 1

    def set_book_rating(self, name, rating):
        if self.books_rating.get(name) and rating in range(1, 11):
            self.books_rating[name] = rating

    def get_book_rating(self, name):
        return self.books_rating.get(name)

    def get_books_with_specific_rating(self, rating):
        books_with_specific_rating = []
        if self.books_rating and rating in range(1, 11):
            for name, book_rating in self.books_rating.items():
                if book_rating == rating:
                    books_with_specific_rating.append(name)

        return books_with_specific_rating

    def get_books_rating(self):
        return self.books_rating

    def add_book_in_favorites(self, name):
        if self.books_rating.get(name):
            if name not in self.favorites:
                self.favorites.append(name)

    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    def get_list_of_favorites_books(self):
        return self.favorites


@pytest.fixture(scope='function')
def books_collector():
    return BooksCollector()


NAME = 'Book Name'
WRONG_NAME = 'Wrong Name'


def test_add_book_success(books_collector):
    books_collector.add_new_book(NAME)
    assert books_collector.favorites == []
    assert books_collector.books_rating == {NAME: 1}


def test_add_book_twice_shows_error(books_collector):
    books_collector.add_new_book(NAME)
    books_collector.add_new_book(NAME)
    assert books_collector.favorites == []
    assert books_collector.books_rating == {NAME: 1}


def test_add_rating_to_book_not_in_list_shows_error(books_collector):
    books_collector.add_new_book(NAME)
    books_collector.set_book_rating(WRONG_NAME, 5)
    assert books_collector.favorites == []
    assert books_collector.books_rating == {NAME: 1}


def test_set_rating_less_than_one_shows_error(books_collector):
    books_collector.add_new_book(NAME)
    books_collector.set_book_rating(NAME, 0)
    assert books_collector.favorites == []
    assert books_collector.books_rating == {NAME: 1}


def test_set_rating_more_than_ten_shows_error(books_collector):
    books_collector.add_new_book(NAME)
    books_collector.set_book_rating(NAME, 11)
    assert books_collector.favorites == []
    assert books_collector.books_rating == {NAME: 1}


def test_book_not_in_list_shows_no_rating(books_collector):
    books_collector.add_new_book(NAME)
    rating = books_collector.get_book_rating(WRONG_NAME)
    assert rating is None


def test_add_to_favorites_success(books_collector):
    books_collector.add_new_book(NAME)
    books_collector.add_book_in_favorites(NAME)
    assert books_collector.favorites == [NAME]
    assert books_collector.books_rating == {NAME: 1}


def test_add_to_favorites_book_not_in_books_raiting_shows_error(books_collector):
    books_collector.add_book_in_favorites(NAME)
    assert books_collector.favorites == []
    assert books_collector.books_rating == {}


def test_delete_from_favorites_success(books_collector):
    books_collector.add_new_book(NAME)
    books_collector.add_book_in_favorites(NAME)
    books_collector.delete_book_from_favorites(NAME)
    assert books_collector.favorites == []
    assert books_collector.books_rating == {NAME: 1}