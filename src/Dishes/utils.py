import logging
from typing import Any, List, Dict
from sql_config.utils import session_wrap
from .models import Dishes


@session_wrap
def get_dishes_handler(session: Any, limit: int = 10, offset: int = 0) -> Dict:
    dishes = session.query(Dishes).limit(limit).offset(offset).all()

    if dishes:
        dishes_dict = [dish.to_dict() for dish in dishes]

        return {'message': 'Done', 'dishes': dishes_dict}

    return {'error': f'No dishes found for page_size: {limit} and page_no: {(1 + offset)*limit}'}


@session_wrap
def create_dishes_handler(session: Any, payload: List[Dict[str, str]]) -> Dict:

    dishes = []
    for item in payload:
        dish_name = item.get('dish_name').strip().lower()
        description = item.get('description')
        image_url = item.get('image_url')

        dish = Dishes.add_dish(dish_name, description, image_url)
        dishes.append(dish)

    try:
        session.add_all(dishes)
        session.commit()

    except Exception as e:
        session.rollback()
        message = f'An error occurred while adding the dish(s): {str(e)}'
        logging.info(message)
        return {'error': message}

    return {
        'message': 'Dish(s) details added successfully',
        'dishes': [dish.to_dict() for dish in dishes]
    }


@session_wrap
def toggle_status_of_dish_handler(session: Any, dish_id: int, status: bool) -> Dict:

    dish = Dishes.get_by_id(session, dish_id)

    if dish:
        dish.is_published = status

        try:
            session.add_all(dish)
            session.commit()
            return {'message': 'Successfully changed the status of the dish'}

        except Exception as e:
            session.rollback()
            message = f'An error occurred while updating dish status: {str(e)}'
            logging.info(message)
            return {'error': message}

    return {'error': f'No dish found with this dish id: {dish_id}'}
