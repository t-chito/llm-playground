from os.path import dirname, join

from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), "..", ".env.local")
load_dotenv(dotenv_path)
