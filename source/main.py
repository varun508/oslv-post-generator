from page1 import *
from page2 import *
from project import *
import requests
import json
import re

data = get_project_data('liyasthomas/postwoman')

create_page_1(data)
create_page_2(data)

