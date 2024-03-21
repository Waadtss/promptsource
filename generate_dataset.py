from datasets import load_dataset, load_from_disk
from promptsource.templates import DatasetTemplates
from promptsource.templates import TemplateCollection
from promptsource import DEFAULT_PROMPTSOURCE_CACHE_HOME
import json
import os

prompts = {}

with open('prompts.txt', 'r') as f:
    for l in f:
        dataset_name = l.strip().split('\t')
        print(dataset_name)
        fout = open(dataset_name[0].replace('/', '_') + '.json', 'w', encoding='utf8')
        if len(dataset_name) == 1:
            print('len1')
            print(os.listdir(DEFAULT_PROMPTSOURCE_CACHE_HOME))
            if dataset_name[0] in os.listdir(DEFAULT_PROMPTSOURCE_CACHE_HOME):
                print('local')
                dataset = load_from_disk(os.path.join(DEFAULT_PROMPTSOURCE_CACHE_HOME, dataset_name[0]))
            else:
                dataset = load_dataset(dataset_name[0])
            prompts[dataset_name[0]] = DatasetTemplates(dataset_name[0])
        elif len(dataset_name) == 2:
            dataset = load_dataset(dataset_name[0], dataset_name[1])
            prompts[dataset_name[0]] = DatasetTemplates(dataset_name[0], dataset_name[1])
        output = {}
        splits = ['test','dev']
        count =0 
        output[splits[0]] = []
        output[splits[1]] = []
        for i in range(len(dataset)):
            if count < 100:
                split = splits[0]
            elif count ==100:
                print(count)
                split = splits[1]
            count +=1
            for p in prompts[dataset_name[0]].all_template_names:        
                    output[split].append(prompts[dataset_name[0]][p].apply(dataset[i]))

                
        
        fout.write(json.dumps(output, ensure_ascii=False, indent=2))
        fout.close()