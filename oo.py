import praw as p
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers import GPTJForCausalLM
import torch.nn
import torch.distributed

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
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f'Using {torch.cuda.get_device_name()}')

    # tokenizer = GPT2Tokenizer.from_pretrained("gpt2-xl")
    # model = GPT2LMHeadModel.from_pretrained("gpt2-xl", pad_token_id=tokenizer.eos_token_id).to(device)
    # input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)
    # greedy_output = model.generate(input_ids, max_length=100).to(device)
    # print("Output:\n" + 100 * '-')
    # print(tokenizer.decode(greedy_output[0], skip_special_tokens=True))

    tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-j-6B")
    model = GPT2LMHeadModel.from_pretrained("EleutherAI/gpt-j-6B", pad_token_id=tokenizer.eos_token_id)

    torch.cuda.set_device(0)
    torch.distributed.init_process_group(
        backend='nccl', world_size=0, init_method='...'
    )
    model = torch.nn.parallel.DistributedDataParallel(model, device_ids=[0], output_device=0)




    model = torch.nn.parallel.DistributedDataParallel(model)
    model.to(device)
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    greedy_output = model.generate(input_ids, max_length=100)
    print("Output:\n" + 100 * '-')
    print(tokenizer.decode(greedy_output[0], skip_special_tokens=True))


for idx, post in enumerate(sub.stream.submissions()):
    if idx == 0:
        print(post.title)
        gen(post.title)
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
