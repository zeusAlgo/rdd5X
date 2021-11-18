import praw as p
import transformers as t
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import AutoModelForCausalLM, AutoTokenizer

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
    model = AutoModelForCausalLM.from_pretrained("gpt2-xl")
    tokenizer = AutoTokenizer.from_pretrained("gpt2-xl")
    inputs = tokenizer(prompt, add_special_tokens=False, return_tensors="pt")["input_ids"]

    prompt_length = len(tokenizer.decode(inputs[0]))
    outputs = model.generate(inputs, max_length=250, do_sample=True, top_p=0.95, top_k=60)
    generated = prompt + tokenizer.decode(outputs[0])[prompt_length + 1:]
    print(generated)


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
