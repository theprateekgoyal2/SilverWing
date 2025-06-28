from flask import request
from .utils import get_dishes_handler, create_dishes_handler, toggle_status_of_dish_handler


def get_dishes_api():

    try:
        limit = int(request.args.get('limit', 10))
        offset = int(request.args.get('offset', 0))

        dish_id_raw = request.args.get('dish_id')
        dish_id = int(dish_id_raw) if dish_id_raw is not None else None

    except (ValueError, TypeError):
        return {'error': 'limit, offset, and dish_id must be valid integers'}

    return get_dishes_handler(limit=limit, offset=offset, dish_id=dish_id)


def create_dishes_api():

    request_body = request.get_json()
    dishes_payload = request_body.get('dishes_data')

    return create_dishes_handler(payload=dishes_payload)


def toggle_status_of_dish_api():

    request_body = request.get_json()
    status = request_body.get('status', False)

    dish_id_raw = request.args.get('dish_id')
    dish_id = int(dish_id_raw) if dish_id_raw is not None else None

    if dish_id:
        return toggle_status_of_dish_handler(dish_id=dish_id, status=status)

    return {'error': 'Provide valid dish_id'}
