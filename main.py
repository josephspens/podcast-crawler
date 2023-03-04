"""Module to crawl the Apple podcast catalog."""
import functions_framework

from models.genre import Genre


@functions_framework.http
def crawl(request):
    """Pull podcast categories"""
    print(request)

    genre = Genre()
    genre_ids = genre.fetch()
    genre.publish_all(genre_ids)

    print('\n'.join(genre_ids))
    return '', 204


if __name__ == "__main__":
    crawl({})
