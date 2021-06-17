# -*- coding: UTF-8 -*-

"""
    @create: 2020-09-15 12:12
    @author: by aries
    @description: None
    
"""
import json


class GetJsonText:
    def get_json_text(self, js, key):
        response_data = json.loads(js)
        json_text = response_data[key]
        return json_text

    def get_json_text_by_list(self, js, key):
        keys = key[:]
        text = []
        response_data = json.loads(js)
        for i in range(len(keys)):
            json_text = response_data[keys[i]]
            text.append(json_text)
        return text
