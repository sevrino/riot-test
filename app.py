# -*- coding:utf-8 -*- 
"""
The GNU GENERAL PUBLIC LICENSE
Copyright (c) 2019-2020 sevrino All rights reserved. 
"""
import json
import requests as r

key = ""

name = input("소환사명 입력 : ")

summoner = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + key

with open("./json/id.json", "wb") as file:
    response = r.get(summoner)
    file.write(response.content)

try:
    with open("./json/id.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
        id = data["id"]
except KeyError:
    print("올바르지 않은 소환사명을 입력하셨거나, 존재하지 않는 소환사명을 입력하셨습니다.")

tier = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + id + "?api_key=" + key

with open("./json/info.json", "wb") as file:
    response = r.get(tier)
    file.write(response.content)

with open("./json/info.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)
    solo_tier = data[0]["tier"]
    solo_rank = data[0]["rank"]

print("솔로 랭크 : " + solo_tier + " " + solo_rank)