import traceback
from services.logging import logger


class CustomException(Exception):
    def __init__(
        self,
        status_code: int = 400,
        detail: str = None,
        type: str = "ServerApi",
        code: str = 946,
    ) -> None:
        self.status_code = status_code
        self.detail = detail
        self.type = type
        self.code = code
        self.__repr__()

    def __repr__(self) -> str:
        class_name = self.__class__.__name__

        logger.error(
            f"{class_name}(status_code={self.status_code!r}, detail={self.detail!r},\
            type={self.type!r}, code={self.code!r}): {traceback.format_exc()!r}"
        )

        return {"status_code": self.status_code, "data": {"message": str(self.detail)}}
