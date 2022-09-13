import os as _os
from urllib import response
import dotenv as _dotenv
import praw as _praw
import urllib.parse as _parse
import requests as _requests
import shutil as _shutil

_dotenv.load_dotenv()


def _create_reddit_client():
    """
    Connecting to reddit API with client_id and client_secret from .env
    """
    client = _praw.Reddit(
        client_id=_os.environ["CLIENT_ID"],
        client_secret=_os.environ["CLIENT_SECRET"],
        user_agent=_os.environ["USER_AGENT"],
    )
    return client


def _is_image(post):
    """
    This function checking post, if it is a image.
    """
    try:
        return post.post_hint == "image"
    except AttributeError:
        return False


def _get_image_urls(client: _praw.Reddit, subreddit_name: str, limit: int):
    """
    Finding hot post and getting links to them
    """
    hot_post = client.subreddit(subreddit_name).hot(limit=limit)
    image_urls = list()
    for post in hot_post:
        if _is_image(post):
            image_urls.append(post.url)

    return image_urls


def _get_image_name(image_url: str) -> str:
    """
    Getting of unical name from urls
    """
    image_name = _parse.urlparse(image_url)
    return _os.path.basename(image_name.path)


def _create_folder(folder_name: str):
    """
    If the folder does not exists then create
    the folder using the given name
    """

    if not _os.path.exists(folder_name):
        try:
            _os.mkdir(folder_name)
        except OSError:
            print("Something goes wrong.")
        else:
            print("Folder created.")


def _download_image(folder_name: str, raw_response, image_name: str):
    """
    if folder exists, save image from reddit to file.
    """
    _create_folder(folder_name)
    with open(f"{folder_name}/{image_name}", "wb") as image_file:
        _shutil.copyfileobj(raw_response, image_file)


def _collect_memes(subreddit_name: str, limit: int = 20):
    """
    Collect the images from the urls and stores them into
    the folders named after their subreddits
    """
    client = _create_reddit_client()
    images_urls = _get_image_urls(
        client=client, subreddit_name=subreddit_name, limit=limit
    )
    for image_url in images_urls:
        image_name = _get_image_name(image_url)
        response = _requests.get(image_url, stream=True)

        if response.status_code == 200:
            response.raw.decode_content = True
            _download_image(subreddit_name, response.raw, image_name)


if __name__ == "__main__":
    _collect_memes("ProgrammerHumor")
