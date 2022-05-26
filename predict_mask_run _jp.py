import torch
import argparse
from transformers import BertTokenizer, BertModel, BertForMaskedLM


import logging
logging.basicConfig(level=logging.INFO)

parser=argparse.ArgumentParser()
parser.add_argument('--short',  default='short-text.txt', help='beam serach', type=str,required=True)
#parser.add_argument('--vis', default='visual_context_label.txt', help='visual_context from ResNet', type=str,required=True)
parser.add_argument('--output', default='', help='', type=str,required=True)
args = parser.parse_args()

# 家の中に[MASK]はいるのか
# 人
# 0.200
# 男
# 0.143
# 犬
# 0.072
# 君
# 0.068
# 女

tokenizer = BertTokenizer.from_pretrained('cl-tohoku/bert-large-japanese')




file1 = []
with open(args.short,'rU') as f1:
    for line1 in f1:
       file1.append(line1.rstrip())

output_path = args.output

result=[]
# print caltion score to file
f=open(output_path, "w")
for i in range(len(file1)):
    temp =[]
    text  = file1[i]

    model = BertForMaskedLM.from_pretrained('cl-tohoku/bert-large-japanese')
    input_ids = tokenizer.encode(text, return_tensors="pt")
    masked_index = torch.where(input_ids == tokenizer.mask_token_id)[1][0].tolist()
    #model.eval()


    # For japanese
    result = model(input_ids)
    pred_ids = result[0][:, masked_index].topk(1).indices.tolist()[0]
    for pred_id in pred_ids:
        output_ids = input_ids.tolist()[0]
        output_ids[masked_index] = pred_id
        print(tokenizer.decode(output_ids))



    result= file1[i]+','+str(tokenizer.decode(output_ids))

    f.write(result)
    f.write('\n')
    print(result)

f.close()


