from abc import ABC, abstractmethod
from uuid import UUID
from ..domain.entity import Repo

class RepoPort(ABC):

    @abstractmethod
    async def save(self, repo: Repo) -> None:
        ...
    
    @abstractmethod
    async def find_by_id(self, repo_id: UUID) -> Repo | None:
        ...

    @abstractmethod
    async def find_all(self) -> list[Repo]:
        ...

    @abstractmethod
    async def delete_by_id(self, repo_id: UUID) -> None:
        ... 