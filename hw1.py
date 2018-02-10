import collections
import datetime
import json
import os
from pattern.en import sentiment,positive

def task1():
    print "hello world"

def task2():
    items=[1,2,3,4,5]
    print items

def task3():
    print("TASK 3:")
    with open('task3.data','r') as fout:
        x = fout.read().split()
    items1 = x[:5]
    print(map(int, items1))
    items2 = x[5:]
    print(map(int, items2))
    fout.close()

def task4():
    print("TASK 4:")
    data = collections.OrderedDict()
    data['school'] = 'UAlbany'
    data['address'] = '1400 Washington Ave, Albany, NY 12222'
    data['phone'] = '(518) 442-3300'
    for x in data.items():
        print(x)
    for x in data.keys():
        print(x+ ":" +data[x])

def task5():
    print("TASK 5:")
    data = collections.OrderedDict()
    data['school'] = 'UAlbany'
    data['address'] = '1400 Washington Ave, Albany, NY 12222'
    data['phone'] = '(518) 442-3300'
    print json.dumps(data);
    with open('task5.data','w') as fout:
        json.dump(data,fout)
    fout.close()
    dataFromFile = json.load(open('task5.data','r'),object_pairs_hook=collections.OrderedDict)
    for k,v in dataFromFile.items():
        print(k+ ":" +v)

def task6():
    print("TASK 6:")
    listItems=[1,2,3,4,5]
    data = collections.OrderedDict()
    data['school'] = 'UAlbany'
    data['address'] = '1400 Washington Ave, Albany, NY 12222'
    data['phone'] = '(518) 442-3300'
    with open('task6.data', 'w') as fout:
        fout.write(json.dumps(listItems))
        fout.write("\n")
        fout.write(json.dumps(data))
    with open('task6.data', 'r') as fout:
        while True:
            newData = fout.readline()
            if not newData:
                break
            newData = newData.replace('\n','')
            newData = json.loads(newData,object_pairs_hook=collections.OrderedDict)
            if type(newData) == list:
                print(newData)
            if type(newData) == collections.OrderedDict:
                for k,v in newData.items():
                    print(k + ":" + v)
    fout.close()

def task7():
    print("TASK 7:")
    for line in open('CrimeReport.txt', 'r').readlines():
        tweet = json.loads(line)
        print(tweet['id'])

def task8():
    print("TASK 8:")
    tweets = []
    for line in open('CrimeReport.txt', 'r').readlines():
        tweet = json.loads(line)
        tweets.append(tweet)
    sorted_tweets = sorted(tweets,key=lambda item:datetime.datetime.strptime(item['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
    f = open('task8.data','w')
    for tweet in sorted_tweets[-10:]:
        f.write(json.dumps(tweet)+ '\n')
    f.close()


def task9():
    print("TASK 9:")
    directory = 'task9-output'
    if not os.path.exists(directory):
        os.makedirs(directory)
    tweets = []
    for line in open('CrimeReport.txt', 'r').readlines():
        tweet = json.loads(line)
        tweets.append(tweet)
    for tweet in tweets:
        #print(tweet['created_at'])
        stringTime = datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
        fileName = str(stringTime.month)+'-'+str(stringTime.day)+'-'+str(stringTime.year)+'-'+str(stringTime.hour)+'.txt'
        with open('task9-output/'+fileName,'a') as fout:
            fout.write(json.dumps(tweet)+'\n')
            fout.close()

def task10():
    print("TASK 10:")
    tweets = []
    for line in open('CrimeReport.txt', 'r').readlines():
        tweet = json.loads(line)
        tweets.append(tweet)
        print sentiment(tweet['text']).assessments
        if positive(tweet['text'],threshold=0.1):
            with open('positive-sentiment-tweets.txt','a') as fp:
                fp.write(json.dumps(tweet)+'\n')
            fp.close()
        else:
            with open('negative-sentiment-tweets.txt','a') as fn:
                fn.write(json.dumps(tweet)+'\n')
            fn.close()


def task11():
    print("TASK 11:")


if __name__ == '__main__':
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()
    task11()