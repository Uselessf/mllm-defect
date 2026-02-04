import json
a=json.load(open('datasets/surface defect detection/grpo3/grpo_with_support_list.json'))
for k,v in a.items():
    if len(v['support'])!=5:
        print(k)