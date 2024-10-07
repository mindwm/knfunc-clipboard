from mindwm import logging
from mindwm.model.objects import Clipboard
from mindwm.knfunc.decorators import iodoc, app, clipboard

logger = logging.getLogger(__name__)

@clipboard
async def func_clipboard(
        clipboard: Clipboard):

    logger.info(clipboard)
