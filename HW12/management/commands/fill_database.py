from HW12.models import Author, Book, Publisher, Store

from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    command_help = 'Fills the database with sample data'

    def handle(self, *args, **options):
        fake = Faker()

        # Create authors
        authors = []
        for _ in range(200):
            author = Author.objects.create(
                name=fake.name(),
                age=fake.random_int(min=20, max=60)
            )
            authors.append(author)

        # Create publishers
        publishers = []
        for _ in range(5):
            publisher = Publisher.objects.create(name=fake.company())
            publishers.append(publisher)

        # Create stores
        stores = []
        for _ in range(5):
            store = Store.objects.create(name=fake.company())
            stores.append(store)

        # Create books
        books = []
        for _ in range(300):
            publisher = fake.random_element(publishers)
            book = Book.objects.create(
                name=fake.catch_phrase(),
                pages=fake.random_int(min=100, max=500),
                price=fake.random.uniform(10.0, 50.0),
                rating=round(fake.random.uniform(1.0, 5.0), 2),
                publisher=publisher,
                pubdate=fake.date_between(start_date='-1y', end_date='today')
            )
            book.authors.set(fake.random_elements(elements=authors, length=fake.random_int(min=1, max=5)))
            books.append(book)

        # Assign books to stores
        for store in stores:
            store.books.set(fake.random_elements(elements=books, length=fake.random_int(min=5, max=10)))

        self.stdout.write(self.style.SUCCESS('Database filled successfully!'))
