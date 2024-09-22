from abc import ABC, abstractmethod
from typing import Optional
from pydantic import BaseModel


class Repository(ABC):
    @abstractmethod
    def store(self, data: BaseModel):
        """Stores vital sign data into the database."""
        pass

    def get(self, period: Optional[str]=None):
        """Retrieves vital sign data from the database."""
        pass