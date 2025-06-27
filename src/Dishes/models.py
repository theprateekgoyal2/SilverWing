from sqlalchemy import Column, Integer, String, Text, Boolean

from sql_config import Base


class Dishes(Base):
    __tablename__ = 'dishes'

    dish_id = Column(Integer, primary_key=True)
    dish_name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    is_published = Column(Boolean, default=False)
    image_url = Column(Text)

    def __repr__(self):
        return f"<Dish_id={self.dish_id}>"

    @classmethod
    def add_dish(cls, dish_name: str, description: str = None, image_url: str = None):
        return cls(
            dish_name=dish_name,
            description=description,
            image_url=image_url
        )

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
