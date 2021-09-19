from typing import List, Optional

import flask
import more_itertools

from models.category_model import Category
from models.video_model import Video
from services import video_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class PlayViewModel(ViewModelBase):
    def __init__(self, video_id: str):
        super().__init__()

        self.video_id = video_id
        self.video: Optional[Video] = video_service.video_by_id(video_id)
