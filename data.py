from news.models import NBANewsModel
import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test"]
collection = db['news']
result = collection.find()
print(result)


try:
    i = 0
    while True:
        NBANewsModel.objects.create(
            publish_date=result[i]['time'],
            title=result[i]['title'],
            content=result[i]['article'],
        )
        i = i + 1
except IndexError:
    print('Done')
