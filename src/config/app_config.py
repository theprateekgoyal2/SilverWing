import logging
from flask import current_app as app, request
from src.common.routes import SILVERWING_ROUTES
from src.common.models import all_models


def configure_current_application():
    configure_app_routes()
    configure_database()


def configure_database():
    from sql_config import Base, engine
    logging.info("✅ Running Database Configuration...")
    Base.metadata.create_all(engine, checkfirst=True)  # Creates tables if missing
    logging.info("✅ Tables Created (if not exist)")


def configure_app_routes():
    for route in SILVERWING_ROUTES:
        api_url = route[0]
        handler = route[1]
        methods = route[2]
        app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=methods)
