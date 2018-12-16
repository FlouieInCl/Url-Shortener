from flask import request, redirect


def register_shorten_url():
    pass


def redirect_original_url(shorten_url):
    return redirect("www.google.co.kr", 301)
