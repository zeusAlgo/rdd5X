import praw as p
import torch
from transformers import GPTJForCausalLM, GPTNeoForCausalLM, AutoTokenizer, AutoModelForCausalLM

map = {'clientId': '9EMA9bZJNOr-3jDNFPR8Ug', 'clientSecret': 'DjcpA3XYXiO3O0eH0sEwrrF_xkzx8w',
       'userAgent': 'web:placetimely532:1(by u/PlaceTimely532)',
       'username': 'PlaceTimely532', 'password': 'zZEKHwSTzDgCCq9'}
rd, readOnly = p.Reddit(client_id=map['clientId'], client_secret=map['clientSecret'],
                        user_agent=map['userAgent'], username=map['username'], password=map['password']), \
               p.Reddit(client_id=map['clientId'], client_secret=map['clientSecret'], user_agent=map['userAgent'])
sub = rd.subreddit('boxing')


def commEnum(reqComm):
    for idx, comment in enumerate(sub.comments(limit=reqComm), 1):
        print(idx, comment.body)


def postEnum(reqPosts):
    for idx, post in enumerate(sub.hot(limit=reqPosts), 1):
        print(idx, post.title)
        if idx == reqPosts: print('--')


def gen(tokens):
    device, gptJ = 'cuda', 'EleutherAI/gpt-j-6B'
    tokenizer, model = AutoTokenizer.from_pretrained(gptJ), \
                       GPTJForCausalLM.from_pretrained(gptJ, torch_dtype=torch.float16).to(device)

    tokenize = tokenizer.encode(tokens, return_tensors='pt').to(device)
    decoder = model.generate(tokenize, temperature=1, max_length=60).to(device)
    inf = tokenizer.batch_decode(decoder)[0][len(tokens):].strip()
    print(f'-' * 80 + '\n', inf, '\n' + 80 * '-')
    return inf
# TODO: get fully parameterized model functional


def decode():
    for idx, post in enumerate(sub.stream.submissions()):
        if idx == 0:
            print(f'Comment == {post.title}')
            gen(post.title)
        else:
            break
# TODO: ensure reply is grammatically correct sentence


def comment():
    for idx, post in enumerate(sub.stream.submissions()):
        if idx == 0:
            print(post.title)
            post.reply(gen(post.title))
        else:
            break


postEnum(3)
commEnum(3)
decode()
# comment()
