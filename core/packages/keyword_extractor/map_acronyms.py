import json

with open("acronyms.json", "r") as f:
    loaded_json = json.load(f)

    dic = dict({})

    for item in loaded_json:
        print item['acronym'], ' ' , item['full_word']
        dic[item['acronym']] = item['full_word']

    try:
        print dic['IOls']
    except KeyError as e:
        print "No acronym found"