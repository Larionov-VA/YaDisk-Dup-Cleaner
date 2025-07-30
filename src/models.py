from dataclasses import dataclass

@dataclass
class FileInfo:
    timestamp: int
    id: str
    name: str
    path: str