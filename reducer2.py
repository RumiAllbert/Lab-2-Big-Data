import boto3
import sys
 
dynamodb = boto3.resource('dynamodb', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")

wordcount = {}
 
for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue
 
    try:
        wordcount[word] = wordcount[word]+count
    except:
        wordcount[word] = count
 
for word in wordcount.keys():
    print('%s\t%s' % ( word, wordcount[word]))
    table = dynamodb.Table('rumilab2')
    table.put_item(
    Item={
        'word': word,
        'count': word[word]
    }
)






