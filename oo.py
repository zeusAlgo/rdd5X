import praw as p
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

map = {'clientId': '9EMA9bZJNOr-3jDNFPR8Ug', 'clientSecret': 'DjcpA3XYXiO3O0eH0sEwrrF_xkzx8w',
       'userAgent': 'web:placetimely532:1(by u/PlaceTimely532)',
       'username': 'PlaceTimely532', 'password': 'zZEKHwSTzDgCCq9'}
rd, readOnly = p.Reddit(client_id=map['clientId'], client_secret=map['clientSecret'],
                        user_agent=map['userAgent'], username=map['username'], password=map['password']), \
               p.Reddit(client_id=map['clientId'], client_secret=map['clientSecret'], user_agent=map['userAgent'])
sub = rd.subreddit('gaming')


def commEnum(reqComm):
    for idx, comment in enumerate(sub.comments(limit=10), 1):
        print(idx, comment.body)


def postEnum(reqPosts):
    for idx, post in enumerate(sub.hot(limit=reqPosts), 1):
        print(idx, post.title)
        if idx == 5: print('--')


def gen(prompt):
    device = 'cuda' if torch.cuda.device(1) else 'cpu'
    print(f'Using {device}')

    tokenizer = GPT2Tokenizer.from_pretrained("gpt2-xl")

    model = GPT2LMHeadModel.from_pretrained("gpt2-xl", pad_token_id=tokenizer.eos_token_id).to(device)
    input_ids = tokenizer.encode('I love sex.', return_tensors='pt').to(device)
    greedy_output = model.generate(input_ids, max_length=50)
    print("Output:\n" + 100 * '-')
    print(tokenizer.decode(greedy_output[0], skip_special_tokens=True))


for idx, post in enumerate(sub.stream.submissions()):
    if idx == 0:
        gen(post)
    else:
        break


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


postEnum(5)
commEnum(5)
# comment()
