import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

topic = os.environ.get("TOPIC")
group = os.environ.get("GROUP")
bootstrap_servers = os.environ.get("BOOTSTRAP_SERVER")