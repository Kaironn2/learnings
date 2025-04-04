from dotenv import load_dotenv
import os

from delivery_launcher import DeliveryLauncher as DL


load_dotenv()
driver = DL()

driver.login(
    username=os.getenv('username'),
    password=os.getenv('password'),
    url=os.getenv('login_url'),
)

driver.orders_page(
    orders_url=os.getenv('orders_url'),
    start_date='01/03/2025',
    end_date='30/04/2025',
)

data = driver.search_and_launch(
    order='100260860',
    delivery_date='04/04/2025',
)


print('Data:', data)
