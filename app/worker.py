from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger
from dotenv import load_dotenv
import os

load_dotenv(".env")

celery = Celery('tasks', broker = os.environ.get("CELERY_BROKER_URL"))

log = get_task_logger(__name__)

@celery.task
def delivery_date(name, order_number):
    
    sleep(3 * order_number)

    log.info(f"Order Complete!")
    
    return {"message": f"Hi {name}, Your order will be delivered on {3*order_number} ",
            "order_number": order_number}