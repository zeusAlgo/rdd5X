import praw as p
import torch
from transformers import GPT2Tokenizer, GPTJForCausalLM, GPTNeoForCausalLM, AutoTokenizer, AutoModelForCausalLM

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


def genJ(prompt):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    tokenizer, model = AutoTokenizer.from_pretrained('EleutherAI/gpt-j-6B'), \
                       GPTJForCausalLM.from_pretrained('EleutherAI/gpt-j-6B', torch_dtype=torch.float16).to(device)
    tokenize = tokenizer.encode(prompt, return_tensors='pt').to(device)
    decoder = model.generate(tokenize, temperature=1, max_length=80).to(device)
    print(f"Output:\n" + 80 * '-', {tokenizer.batch_decode(decoder)[0]}, "\n" + 80 * '-')


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
            genJ(post)
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
