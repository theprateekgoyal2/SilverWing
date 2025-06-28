from sqlalchemy import Column, Integer, String, Text, Boolean

from src.sql_config import Base


class Dishes(Base):
    __tablename__ = 'dishes'

    dish_id = Column(Integer, primary_key=True)
    dish_name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    is_published = Column(Boolean, default=False)
    image_url = Column(Text)

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
            'image_url': self.image_url
        }
