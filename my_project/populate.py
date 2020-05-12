import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_project.settings')

import django
django.setup()

import random
from my_app.models import Topic, Webpage, AccessRecord, Name
from faker import Faker

fakegen = Faker()
#topics = ['Search','Social', 'Media', 'Marketplace']

# def add_topic():
#     t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
#     t.save()
#     return t

def populate(N = 5):

    for entry in range(N):

        # top = add_topic()
        fake_name = fakegen.name().split()
        # fake_url = fakegen.url()
        # fake_date = fakegen.date()
        f_name = fake_name[0]
        l_name = fake_name[1]

        # webpg = Webpage.objects.get_or_create(topic = top,url = fake_url,name = fake_name)[0]

        # acc_rec = AccessRecord.objects.get_or_create(name = webpg,date = fake_date)[0]
        
        name_list = Name.objects.get_or_create(first_name = f_name, last_name = l_name)[0]


if __name__ == "__main__":
    print("It's Working!!!!") 
    populate(20)
    print("Process Over!!!")