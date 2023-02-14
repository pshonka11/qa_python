from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_same_book_twice_error(self):
        collector = BooksCollector()
        collector.add_new_book('Питон для чайников')
        collector.add_new_book('Питон для чайников')
        assert len(collector.get_books_rating()) == 1

    def test_add_rating_to_book_not_in_list_error(self):
            collector = BooksCollector()
            collector.set_book_rating('Анна Каренина', 9)
            assert collector.get_book_rating('Анна Каренина') == None

    def test_set_rating_less_than_one_error(self):
                collector = BooksCollector()
                collector.add_new_book('Три мушкетера')
                collector.set_book_rating('Три мушкетера', 0)
                assert collector.get_book_rating('Три мушкетера') == 1

    def test_set_rating_more_than_ten_error(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_rating('Преступление и наказание', 11)
        assert collector.get_book_rating('Преступление и наказание') == 1

    def test_book_not_in_list_shows_no_rating(self):
        collector = BooksCollector()
        collector.set_book_rating('Путешествия Гулливера', 9)
        assert collector.get_book_rating('Путешествия Гулливера') == None

    def test_add_to_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Собор Парижской Богоматери')
        collector.add_book_in_favorites('Собор Парижской Богоматери')
        assert collector.get_list_of_favorites_books() == ['Собор Парижской Богоматери']

    def test_add_to_favorites_book_not_in_books_raiting_shows_error(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Алиса в стране чудес') == None

    def test_delete_from_favorites_success(self):
            collector = BooksCollector()
            collector.add_new_book('Тесирование DOT COM')
            collector.add_book_in_favorites('Тесирование DOT COM')
            collector.delete_book_from_favorites('Тесирование DOT COM')
            assert collector.get_list_of_favorites_books() == []