# 文章を生成

import json
dic = open("markov-blog.json" , "r")
dic = json.load(dic)

tweets_list = []
import random
def word_choice(sel):
    keys = sel.keys()
    ran = random.choice(list(keys))
    return ran

def make_sentence(dic):
    ret = []
    if not "@" in dic: return "no dic"
    top = dic["@"]
    while True:
        w1 = word_choice(top)
        w2 = word_choice(top[w1])
        if not (w1 is type(None) or w2 is type(None)):
            break
    ret.append(w1)
    ret.append(w2)
    while True:
        w3 = word_choice(dic.get(w1).get(w2))
        ret.append(w3)
        if w3 == "。": break
        w1, w2 = w2, w3
    tweets_list.append(ret)
    return "".join(ret)


while True:#一文のみ
    s = make_sentence(dic)
    if len(s) < 140:
        break


#文章をツイート
import twitter

auth = twitter.OAuth(consumer_key="O1iiUPGO486AcOAFFAVHMYWzf",
consumer_secret="BoNVzXxbccEgtIl167b6DlrreEkFm2NaVheQCpOhE90X8aYmvw",
token="1011200951057649664-qApVJyG0uS5wWrIgE6k2dsHhERzc6k",
token_secret="KUn5VLZr3AGeUoFE5Npd83ovQZy0lh1sKUjgFPHpubsp6")

t = twitter.Twitter(auth=auth)

#ツイートのみ
status = s  #投稿するツイート
t.statuses.update(status=status) #Twitterに投稿




