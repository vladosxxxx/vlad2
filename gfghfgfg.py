import os
import sys

этот_фаил = __file__

эта_папка = os.path.dirname(этот_фаил)
папка_выше = os.path.dirname(эта_папка)
sys.path.append(папка_выше)

from tools.все_подрят import *
print(цветной_терминал("rfhbxytdsq хирный тест",  стиль = "жкт"))