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


def gen():

    model = AutoModelForCausalLM.from_pretrained("gpt2-xl")
    tokenizer = AutoTokenizer.from_pretrained("gpt2-xl")

    # Padding text helps XLNet with short prompts - proposed by Aman Rusia in https://github.com/rusiaaman/XLNet-gen#methodology
    PADDING_TEXT = """In 1991, the remains of Russian Tsar Nicholas II and his family
    (except for Alexei and Maria) are discovered.
    The voice of Nicholas's young son, Tsarevich Alexei Nikolaevich, narrates the
    remainder of the story. 1883 Western Siberia,
    a young Grigori Rasputin is asked by his father and a group of men to perform magic.
    Rasputin has a vision and denounces one of the men as a horse thief. Although his
    father initially slaps him for making such an accusation, Rasputin watches as the
    man is chased outside and beaten. Twenty years later, Rasputin sees a vision of
    the Virgin Mary, prompting him to become a priest. Rasputin quickly becomes famous,
    with people, even a bishop, begging for his blessing. <eod> </s> <eos>"""

    prompt = "Today the weather is really nice and I am planning on "
    inputs = tokenizer(PADDING_TEXT + prompt, add_special_tokens=False, return_tensors="pt")["input_ids"]

    prompt_length = len(tokenizer.decode(inputs[0]))
    outputs = model.generate(inputs, max_length=250, do_sample=True, top_p=0.95, top_k=60)
    generated = prompt + tokenizer.decode(outputs[0])[prompt_length + 1:]
    print(generated)


def comment():
    for idx, post in enumerate(sub.stream.submissions()):
        if idx == 0:

            post.reply('Antón Castillo will feel like a real and credible threat. He is more of a satirical mash-up '
                       'of Franco and Castro. He is certainly a bad guy with a vision for his country that he holds '
                       'above all—even family, as he often reminds his son and protégé, Diego—but there is a '
                       'two-dimensional vibe I just can not shake.')
        else:
            break


postEnum(5)
commEnum(5)
gen()
# comment()
