from sqlalchemy.orm import Session
from sqlalchemy import func
from exceptions.fast_api_custom import CustomException


class BaseCrudModel:
    @classmethod
    def create(cls, db_session: Session, **kwargs):
        new = cls(**kwargs)
        db_session.add(new)
        db_session.flush()
        return new

    @classmethod
    def update(cls, db_session: Session, id: str, **kwargs):
        query = cls.query.filter_by(id=id, disabled_at=None).first()

        if query is None:
            raise CustomException(
                status_code=404,
                type="NoData",
                detail="No es posible actualizar el registro, debido a que no se encuentra disponible ó ha sido eliminado.",
            )

        for key, value in kwargs.items():
            if hasattr(query, key):
                setattr(query, key, value)

        db_session.flush()
        return query

    @classmethod
    def read_by_id(cls, id: str):
        return cls.query.filter_by(id=id, disabled_at=None).first()

    @classmethod
    def read_disabled(cls, id: str):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def read_select(cls):
        return cls.query.filter_by(disabled_at=None).all()

    @classmethod
    def delete(cls, db_session: Session, id: str):
        query = cls.query.filter_by(id=id, disabled_at=None).first()

        if query is None:
            raise CustomException(
                status_code=404,
                type="NoData",
                detail="No es posible eliminar el registro, debido a que no se encuentra disponible ó ha sido eliminado.",
            )

        query.disabled_at = func.now()
        db_session.flush()
        return query

    @classmethod
    def restore(cls, db_session: Session, id: str):
        query = cls.query.filter(cls.id == id, cls.disabled_at.isnot(None)).first()

        if query is None:
            raise CustomException(
                status_code=404,
                type="NoData",
                detail="No es posible restaurar el registro, debido a que no se encuentra disponible ó ha sido eliminado.",
            )

        query.disabled_at = None
        db_session.flush()
        return query
