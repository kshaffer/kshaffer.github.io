import yaml
import json
import os

new_filename = 'jekyll_to_ghost.json'

file_list = []
for f in os.listdir('./'):
    if '.md' in f or '.markdown' in f:
        file_list.append(f)

json_object = {}
json_object['db'] = []
posts_object = {}
posts_object['data'] = {}
posts_object['data']['posts'] = []

for filename in file_list:
    original = open(filename, 'r', encoding='utf-8')
    parsed = ''

    for line in original:
        parsed += line

    parsed = parsed.split('---\n')
    header = yaml.load(parsed[1])
    header['content'] = parsed[2]

    post_object = {
    "id": 0,
    "title": "",
    "slug": "",
    "markdown": "",
    "html": "",
    "image": "",
    "featured": 0,
    "page": 0,
    "status": "published",
    "language": "en_US",
    "meta_title": "",
    "meta_description": "",
    "author_id": 1,
    "created_at": "",
    "created_by": 1,
    "updated_at": "",
    "updated_by": 1,
    "published_at": "",
    "published_by": 1
    }

    post_object['title'] = post_object['og_title'] = post_object['twitter_title'] = header['title']
    post_object['meta_title'] = header['title']
    try:
        post_object['meta_description'] = post_object['og_description'] = post_object['twitter_description'] = header['short_description']
    except:
        post_object['meta_description'] = post_object['og_description'] = post_object['twitter_description'] = ''
    try:
        post_object['created_at'] = post_object['updated_at'] = post_object['published_at'] = str(header['modified'])
    except:
        post_object['created_at'] = post_object['updated_at'] = post_object['published_at'] = str(header['date'])
    post_object['markdown'] = header['content']
    try:
        post_object['image'] = post_object['og_image'] = post_object['twitter_image'] = header['image']['feature']
    except:
        post_object['image'] = post_object['og_image'] = post_object['twitter_image'] = ''

    posts_object['data']['posts'].append(post_object)

json_object['db'].append(posts_object)

with open(new_filename, 'w') as new_file:
    # new_file.write(str(header))
    json.dump(json_object, new_file, indent = 4)
