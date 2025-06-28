import logging
from typing import Any, List, Dict
from src.sql_config.utils import session_wrap
from .models import Dishes


@session_wrap
def get_dishes_handler(
    session: Any,
    limit: int = 10,
    offset: int = 0,
    dish_id: int = None
) -> Dict:
    """
    Fetch a single dish by ID, or a paginated list of dishes.

    Args:
        session (Any): SQLAlchemy session
        limit (int): Number of dishes to fetch
        offset (int): Pagination offset
        dish_id (int): Optional, fetch a specific dish

    Returns:
        Dict: Dish data or error message
    """

    if dish_id is not None:
        dish = Dishes.get_by_id(session, dish_id)
        if dish:
            return {'message': 'Dish fetched successfully', 'dish': dish.to_dict()}
        return {'error': f'Dish with ID {dish_id} not found'}

    dishes = session.query(Dishes).limit(limit).offset(offset).all()

    if not dishes:
        return {
            'error': f'No dishes found for limit={limit} and offset={offset}'
        }

    dishes_dict = [dish.to_dict() for dish in dishes]

    return {
        'message': 'Dishes fetched successfully',
        'dishes': dishes_dict
    }


@session_wrap
def get_individual_dish_handler(session: Any, dish_id: int) -> Dict:
    dish = Dishes.get_by_id(session, dish_id)
    if dish:
        return {'message': 'Done', 'dish': dish.to_dict()}

    return {'error': 'No dish found'}


@session_wrap
def create_dishes_handler(session: Any, payload: List[Dict[str, str]]) -> Dict:
    """
    Adds one or more dishes to the database.

    Args:
       session (Any): SQLAlchemy session
       payload (List[Dict[str, str]]): List of dish data dicts

    Returns:
        Dict: Success message and inserted dishes or error
    """
    dishes = []
    for item in payload:
        dish_name = item.get('dishName')
        description = item.get('description')
        image_url = item.get('imageUrl')
        is_published = bool(item.get('isPublished'))

        if not dish_name or not isinstance(dish_name, str):
            return {'error': 'Each dish must have a valid "dish_name"'}

        dish_name = dish_name.strip().lower()

        dish = Dishes(dish_name, description, image_url, is_published)
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
    """
    Toggles the is_published status of a dish.

    Args:
        session (Any): SQLAlchemy session
        dish_id (int): ID of the dish to update
        status (bool): New publish status

    Returns:
        Dict: Success or error message
    """
    dish = Dishes.get_by_id(session, dish_id)

    if not dish:
        return {'error': f'No dish found with dish_id: {dish_id}'}

    try:
        dish.is_published = status
        session.add(dish)
        session.commit()
        return {'message': f'Dish status updated to {"Published" if status else "Unpublished"}'}

    except Exception as e:
        session.rollback()
        message = f'Error updating dish status: {str(e)}'
        logging.error(message)
        return {'error': message}
