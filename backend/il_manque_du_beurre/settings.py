import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_USER = os.getenv('DATABASE_USER', 'postgres')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'database')
DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'postgres')
DATABASE_TEST_NAME = os.getenv('DATABASE_TEST_NAME', 'postgres_test')
