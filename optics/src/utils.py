from config.settings import NUMBER_OF_REVIEWS_DISPLAYED
from optics.models import Feedback


def get_random_reviews():
    reviews_set = Feedback.objects.filter(is_published=True).order_by('?')

    return reviews_set[:NUMBER_OF_REVIEWS_DISPLAYED]