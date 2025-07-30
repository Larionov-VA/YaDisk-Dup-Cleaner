from yadisk import YaDisk
from models import FileInfo

class YaDiskCleaner:
    def __init__(self, token: str, id: str, secret: str):
        self.disk = YaDisk(id = id, secret = secret, token = token)
    
    def parse_filename(self, filename: str) -> FileInfo:
        parts = filename.split('_', 2)
        if len(parts) != 3:
            raise ValueError(f"Invalid filename format: {filename}")
        return FileInfo(
            timestamp=int(parts[0]),
            id=parts[1],
            name=parts[2],
            path=filename
        )

    def get_files_to_delete(self, folder_path: str) -> list[str]:
        files = list(self.disk.listdir(folder_path))
        file_groups: dict[str, list[FileInfo]] = {}
        for file in files:
            try:
                file_info = self.parse_filename(file.name)
                file_groups.setdefault(file_info.id, []).append(file_info)
            except ValueError:
                continue
        to_delete = []
        for file_group in file_groups.values():
            if len(file_group) <= 1:
                continue
            max_timestamp = max(f.timestamp for f in file_group)
            to_delete.extend(
                f.path for f in file_group 
                if f.timestamp < max_timestamp
            )
        return to_delete
    
    def clean_folder(self, folder_path: str, permanently: bool) -> int:
        files_to_delete = self.get_files_to_delete(folder_path)
        for file_path in files_to_delete:
            try:
                self.disk.remove(folder_path + "/" + file_path, permanently = permanently)
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        return len(files_to_delete)