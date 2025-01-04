from config.settings import NUMBER_OF_REVIEWS_DISPLAYED
from tunes.models import Feedback, Quote


def get_random_reviews():
    reviews_set = Feedback.objects.filter(is_published=True).order_by('?')

    return reviews_set[:NUMBER_OF_REVIEWS_DISPLAYED]


def get_random_quote():
    quote = Quote.objects.filter(is_published=True).order_by('?').first()

    return quote