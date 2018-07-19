# import logging
# #基础用法
# TAG = "logging tst"
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s--%(lineno)d--%(message)s"
# )
# logging.debug("this is debug level")
# logging.info("this is info level")
# logging.warning("this is warning level")
# logging.error("this is error level")


##########################################################################
import logging

logger = logging.getLogger(__name__) # add name
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


handler1 = logging.FileHandler("jixidafa.info")
handler2 = logging.StreamHandler()
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)
# 也可以在这里设置显示的level,不过在这里之后会覆盖上面的level.
# handler2.setLevel(logging.WARNING)

logger.addHandler(handler1)
logger.addHandler(handler2)

logger.debug("this is debug")
logger.info("this is info")
logger.warning("this is warning")
logger.error("this is error")

