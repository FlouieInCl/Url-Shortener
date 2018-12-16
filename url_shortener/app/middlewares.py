from werkzeug.exceptions import HTTPException
from flask import jsonify


def error_handler(e):
    if isinstance(e, HTTPException):
        des = e.description
        code = e.code
    else:
        des = '[Internal server error] Fix it now!'
        code = 500

    return jsonify({
        'description': des
    }), code


def after_request(response):
    """
    Set header - X-Content-Type-Options=nosniff, X-Frame-Options=deny before response
    """
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'deny'

    return response
