from mastodon import Mastodon
import os

mdon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://botsin.space/'
)

mdon.status_post("Whuddup world!")
