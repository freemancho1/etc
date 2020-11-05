import os, sys
path = os.path.abspath(__file__+'/../..')
if path not in sys.path:
    sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DATA_MODELING.settings")

import django 
import random
import pandas as pd 
from datetime import datetime

django.setup()

from modeling.models import *

predict_oks = REAL_PAYLOAD_RESULT.objects\
    .filter(completed_date__range=(datetime(2020,10,22,14),datetime(2020,10,23,23)),
            model_id__gt=0, predict_result='공격')\
    .exclude(type_code_id__in=[13, 19, 31, 23, 25])
predict_oks_list = list(predict_oks)
random.shuffle(predict_oks_list)
predict_oks_file = []
for item in predict_oks_list[:200]:
    obj = {'id': item.id, 'signature': item.type_code.description, 
           'payload': item.payload_ascii, 'predict': '공격'}
    predict_oks_file.append(obj)
predict_oks_pd = pd.DataFrame(predict_oks_file)
predict_oks_pd.to_excel('./predict_ok.xlsx', index=True, header=True)

predict_nos = REAL_PAYLOAD_RESULT.objects\
    .filter(completed_date__range=(datetime(2020,10,22,14),datetime(2020,10,23,23)),
            model_id__gt=0, predict_result='정상')\
    .exclude(type_code_id__in=[13, 19, 31, 23, 25])
predict_nos_list = list(predict_nos)
random.shuffle(predict_nos_list)
predict_nos_file = []
for item in predict_nos_list[:100]:
    obj = {'id': item.id, 'signature': item.type_code.description, 
           'payload': item.payload_ascii, 'predict': '정상'}
    predict_nos_file.append(obj)
predict_nos_pd = pd.DataFrame(predict_nos_file)
predict_nos_pd.to_excel('./predict_no.xlsx', index=True, header=True)
