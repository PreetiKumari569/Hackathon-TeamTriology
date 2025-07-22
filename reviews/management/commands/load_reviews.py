import csv
from django.core.management.base import BaseCommand
from reviews.models import Product, Review
from reviews.utils.sentiment import get_sentiment
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Load product reviews from a CSV file and analyze sentiment'

    def handle(self, *args, **kwargs):
        print("📁 Starting to load CSV...")  # Debug print

        file_path = 'Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv'

        try:
            with open(file_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                count = 0

                for row in tqdm(reader):
                    product_name = row.get('name')
                    review_text = row.get('reviews.text')

                    if not product_name or not review_text:
                        continue

                    product, _ = Product.objects.get_or_create(name=product_name)
                    sentiment = get_sentiment(review_text)

                    Review.objects.create(
                        product=product,
                        text=review_text,
                        sentiment=sentiment
                    )
                    count += 1
                    if count % 100 == 0:
                        print(f"✅ Processed {count} reviews")

            print(f"✔ Finished loading reviews. Total: {count}")

        except FileNotFoundError:
            print(f"❌ File not found: {file_path}")
        except Exception as e:
            print(f"❌ Error occurred: {e}")
