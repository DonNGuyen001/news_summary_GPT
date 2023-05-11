import os
import json 
import openai
openai.api_key = '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'
list_str= openai.Model.list()

def write_list(a_list):
    print("Started writing list data into a json file")
    with open("../../PycharmProjects/pythonProject/chatGPT_Model.json", "w") as fp:
        json.dump(a_list, fp)
        print("Done writing JSON data into .json file")

write_list (list_str)