from civitai_api import api
from civitai_api.models.images import NsfwLevel
import httpx
from gospeed_api.models.create_a_batch_of_tasks import TaskUrl, CreateABatchOfTasks, CreateABatchOfTasks_Response
from gospeed_api.models.create_a_task import CreateTask_DownloadOpt
from gospeed_api.models.get_task_info import GetTaskInfo_Response
from gospeed_api.models import TASK_STATUS
from gospeed_api.models.delete_a_task import DeleteATask_Response
import os
from gospeed_api.index import GospeedClient
from pydantic import ValidationError

postIds = [
    "11060953",
    "11059742"
]
gospeed_client = GospeedClient('http://127.0.0.1:9999/')
httpx_client = httpx.Client(proxy="http://127.0.0.1:17890")

for postId in postIds:
    try:
        response_data = api.get_images_v1(httpx_client, postId=[postId], nsfw=[NsfwLevel.X.value])
    except ValidationError as exc:
        print(repr(exc.errors(include_input=True)))
    addrs = []
    for item in response_data.items:
        # source img address
        addrs.append(item.url)
    
    taskUrls = []
    for addr in addrs:
        taskUrls.append(TaskUrl(url=addr))
    opt = CreateTask_DownloadOpt(path=os.path.join(os.path.dirname(__file__), postId))
    tasks = CreateABatchOfTasks(reqs=taskUrls, opt=opt)
    res_data = gospeed_client.create_a_batch_of_tasks(data=tasks)
