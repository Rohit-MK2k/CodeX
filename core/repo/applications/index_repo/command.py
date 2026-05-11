from dataclasses import dataclass
from uuid import UUID

@dataclass(frozen=True)
class GenerateRepoIndexCommand:
    name: str
    path: str