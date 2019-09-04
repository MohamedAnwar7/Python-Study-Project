import pymongo

client = pymongo.MongoClient()  # Establish Connection
db = client['pymongo_test']  # Create or Access a database
col = db['customers']  # create or Access database collection (Table)

posts_data = [
    {'_id': 1, 'name': 'khaled', 'job': 'engineer'},
    {'_id': 2, 'name': 'ahmed', 'job': 'sales manger'}
]
# insert one or multiple Documents (records/rows)
""" result = col.insert_many(posts_data)
print('inserted id :{}'.format(result.inserted_ids)) """

# find one data from table (collection)
""" result = col.find_one()
print(result) """

# find all data
""" for x in col.find({},{'_id':0}): # second param decide which fields to include in the result
    print(x) """
# filter result using query
""" query = {'name': {'$gt': 'h'}}  # name start with h or greater
for filterd in col.find(query):
    print(filterd) """
# using RegEx
RgQuery = {"name": {"$regex": "^a"}} #select name starts with a letter 

for reg in col.find(RgQuery):
    print(reg)
