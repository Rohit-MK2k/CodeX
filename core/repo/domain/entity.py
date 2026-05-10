from typing import List
from uuid import uuid4, UUID
from datetime import datetime, timezone

class Repo:
    MAX_NAME_LENGTH = 100

    def __init__(self, name:str, path:str, stack: List[str]):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if len(name) > self.MAX_NAME_LENGTH:
            raise ValueError("Project name is too long. Max {self.MAX_NAME_LENGTH} chars.")

        if not path.strip():
            raise ValueError("Path cannot be empty")

        self.id: UUID = uuid4()
        self.name = name
        self.path = path
        self.chunk_counter = 0 
        self.stack = stack
        self.indexed_at = None
        self.created = datetime.now(timezone.utc)

    def mark_as_indexed(self, chunk_count:int):
        self.chunk_counter = chunk_count
        self.indexed_at = datetime.now(timezone.utc)

        
    