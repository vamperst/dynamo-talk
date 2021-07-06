import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime

dao = BaseDAO('table1')

for i in range(10):
    dao.put_item({'xpto':str(i)})
