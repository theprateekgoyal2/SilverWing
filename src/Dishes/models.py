import pytz
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, func
from src.sql_config import Base


class Dishes(Base):
    __tablename__ = 'dishes'

    dish_id = Column(Integer, primary_key=True)
    dish_name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    is_published = Column(Boolean, default=False)
    image_url = Column(Text)
    dt_created = Column(DateTime, default=func.now())
    dt_updated = Column(DateTime, onupdate=func.now(), default=func.now())

    def __repr__(self):
        return f"<Dish_id={self.dish_id}>"

    def __init__(self,dish_name: str, description: str = None,
                 image_url: str = None, is_published: bool = False):
        self.dish_name = dish_name
        self.description = description
        self.image_url = image_url
        self.is_published = is_published

    @classmethod
    def get_by_id(cls, session, dish_id: int, with_for_update=False, no_wait=False):
        if with_for_update:
            return session.query(cls).with_for_update(nowait=no_wait).filter_by(dish_id=dish_id).first()
        return session.query(cls).filter_by(dish_id=dish_id).first()

    @classmethod
    def get_by_ids(cls, session, dish_ids: list):
        return session.query(cls).filter(cls.dish_id.in_(dish_ids)).all()

    def to_dict(self):
        return {
            'dish_id': self.dish_id,
            'dish_name': self.dish_name,
            'description': self.description,
            'is_published': self.is_published,
            'image_url': self.image_url,
            'last_updated': format_datetime_to_ist(self.dt_updated)
        }


def format_datetime_to_ist(dt_obj: datetime) -> str:
    if not isinstance(dt_obj, datetime):
        raise TypeError(f"Expected datetime, got {type(dt_obj)}")

    # First: Localize to UTC if naive
    if dt_obj.tzinfo is None:
        dt_obj = pytz.utc.localize(dt_obj)

    # Then: Convert to IST
    ist = pytz.timezone("Asia/Kolkata")
    ist_time = dt_obj.astimezone(ist)

    # Finally: Format to readable string
    return ist_time.strftime("%b %d, %Y %I:%M %p")
