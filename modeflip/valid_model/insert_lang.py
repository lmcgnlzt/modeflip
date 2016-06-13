from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager

from modeflip.models.designer import *



local_config = get_configuration()
get_database = MongoManager(local_config, force_load=True)


dc = DesignerConfig(get_database('mf_config'))


# print dc

designer = dc.get(1)


# f = open('/Users/mli/modeflip/lang_file.txt')  # open a file
# text = f.read()    # read the entire contents, should be UTF-8 text

# print text


designer.bio = text