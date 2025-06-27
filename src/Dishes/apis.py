from flask import request
from .utils import get_dishes_handler, create_dishes_handler, toggle_status_of_dish_handler


def get_dishes_api():

    # Fetch limit and offset from query params, if not present use default
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))

    return get_dishes_handler(limit, offset)


def create_dishes_api():

    request_body = request.get_json()
    dishes_payload = request_body.get('dishes_data')

    return create_dishes_handler(dishes_payload)


def toggle_status_of_dish_api():

    request_body = request.get_json()
    dish_id = request_body.get('dish_id')
    status = request_body.get('status', False)

    if dish_id and int(dish_id):
        return toggle_status_of_dish_handler(int(dish_id), status)

    return {'error': 'Provide valid dish_id'}
