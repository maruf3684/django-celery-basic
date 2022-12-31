from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    #operation
    for i in range (1):
        print(i , "number")
    return "Done"
    
@shared_task(bind=True)
def send_mail_func(self,data):
    print("MAIL SEND",data)


 ### def send_mail_func(self,data):