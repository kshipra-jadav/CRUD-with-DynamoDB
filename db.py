# For dynamodb connection

import boto3
from pprint import pprint

DB = boto3.resource('dynamodb', region_name = 'ap-south-1')

table = DB.Table('Employees')

