from dataclasses import dataclass
from dataset_tool.models.media_file import MediaFile


@dataclass(frozen=True)
class ImageFile(MediaFile):
    pass
