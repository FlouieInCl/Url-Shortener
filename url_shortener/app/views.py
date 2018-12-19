from flask import request, redirect, Response, current_app

from app.models import db, UrlMappingModel
from app.helpers import encode_for_shorten, decode_for_original


def register_shorten_url():
    original_url = request.json['originalUrl']

    mapping = UrlMappingModel(original_url=original_url)
    db.session.add(mapping)
    db.session.commit()

    id = UrlMappingModel.query.filter_by(original_url=original_url).first().id
    res = encode_for_shorten(id)

    return Response('http://{0}/{1}'.format(current_app.config['REPRESENTATION_URL'], res))


def redirect_original_url(shorten_url):
    print('tlqkffusdk')
    decoded_id = decode_for_original(shorten_url)
    original_url = UrlMappingModel.query.filter_by(id=decoded_id).first().original_url

    return redirect(original_url, 301)
