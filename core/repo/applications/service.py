from uuid import UUID
from .index_repo.command import GenerateRepoIndexCommand
from ..domain.entity import Repo
from .port import RepoPort


class RegisterRepoService:
    def __init__(
        self,
        repo_repo: RepoPort,
    ) -> None:
        self.repo_repo = repo_repo
    
    async def execute(self, cmd: GenerateRepoIndexCommand) -> str:
        repo_obj = Repo(
            name = cmd.name,
            path = cmd.path
        )

        await self.repo_repo.save(repo_obj)

        return repo_obj.id