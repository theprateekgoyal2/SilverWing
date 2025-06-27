from .apis import (
    get_dishes_api,
    create_dishes_api,
    toggle_status_of_dish_api
)

routes = [
    ('/api/nosh/v1/dishes', get_dishes_api, ['GET']),
    ('/api/nosh/v1/dishes', create_dishes_api, ['POST']),
    ('/api/nosh/v1/dishes/toggle', toggle_status_of_dish_api, ['POST'])
]
