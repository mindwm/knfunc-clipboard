from mindwm import logging
from mindwm.model.objects import Clipboard
from mindwm.knfunc.decorators import iodoc, app, clipboard

logger = logging.getLogger(__name__)

@clipboard
async def func_clipboard(
        clip_board: Clipboard,
        uuid: str,
        time: int,
        data: str,
        username: str,
        hostname: str,
        traceparent: str,
        graph):

    logger.info(f"uuid: {uuid}, time: {time}, data: {data}, traceparent: {traceparent}")

    traceparent = traceparent

    user = graph.User(username=username, traceparent=traceparent).merge()
    host = graph.Host(hostname=hostname, traceparent=traceparent).merge()
    graph.UserHasHost(source=user, target=host, traceparent=traceparent).merge()

    clip_board_graph = graph.Clipboard(  
        uuid = uuid,
        time = time,
        data = data
    ).create()

    graph.HostHasClipboard(source = host, target = clip_board_graph, traceparent = traceparent).merge()

    logger.info(clip_board_graph)
