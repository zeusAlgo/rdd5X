import praw as p
import torch
import torch.nn
from transformers import GPT2Tokenizer
from transformers import GPTNeoForCausalLM

map = {'clientId': '9EMA9bZJNOr-3jDNFPR8Ug', 'clientSecret': 'DjcpA3XYXiO3O0eH0sEwrrF_xkzx8w',
       'userAgent': 'web:placetimely532:1(by u/PlaceTimely532)',
       'username': 'PlaceTimely532', 'password': 'zZEKHwSTzDgCCq9'}
rd, readOnly = p.Reddit(client_id=map['clientId'], client_secret=map['clientSecret'],
                        user_agent=map['userAgent'], username=map['username'], password=map['password']), \
               p.Reddit(client_id=map['clientId'], client_secret=map['clientSecret'], user_agent=map['userAgent'])
sub = rd.subreddit('gaming')


def commEnum(reqComm):
    for idx, comment in enumerate(sub.comments(limit=reqComm), 1):
        print(idx, comment.body)


def postEnum(reqPosts):
    for idx, post in enumerate(sub.hot(limit=reqPosts), 1):
        print(idx, post.title)
        if idx == reqPosts: print('--')


def genNeo(prompt):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    tokenizer, model = GPT2Tokenizer.from_pretrained('EleutherAI/gpt-neo-2.7B'), \
                       GPTNeoForCausalLM.from_pretrained('EleutherAI/gpt-neo-2.7B').to(device)
    tokenize = tokenizer.encode(prompt, return_tensors='pt').to(device)
    decoder = model.generate(tokenize, temperature=10, max_length=100).to(device)
    print("Output:\n" + 80 * '-')
    print(tokenizer.decode(decoder[0], skip_special_tokens=True))


def genJ(prompt):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    tokenizer, model = GPT2Tokenizer.from_pretrained('EleutherAI/gpt-neo-2.7B'), \
                       GPTNeoForCausalLM.from_pretrained('EleutherAI/gpt-neo-2.7B').to(device)
    tokenize = tokenizer.encode(prompt, return_tensors='pt').to(device)
    decoder = model.generate(tokenize, temperature=10, max_length=100).to(device)
    print("Output:\n" + 80 * '-')
    print(tokenizer.decode(decoder[0], skip_special_tokens=True))


def decode():
    for idx, post in enumerate(sub.stream.submissions()):
        if idx == 0:
            print(post.title)
            genJ(post.title)
        else:
            break


decode()


def comment():
    for idx, post in enumerate(sub.stream.submissions()):
        if idx == 0:
            gen(post)
            string = post
            post.reply('Antón Castillo will feel like a real and credible threat. He is more of a satirical mash-up '
                       'of Franco and Castro. He is certainly a bad guy with a vision for his country that he holds '
                       'above all—even family, as he often reminds his son and protégé, Diego—but there is a '
                       'two-dimensional vibe I just can not shake.')
        else:
            break


postEnum(3)
commEnum(3)
# comment()
