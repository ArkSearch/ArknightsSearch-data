import os

cwd = os.getcwd()

# 输出数据
data_path = os.path.join(cwd, 'data')
hash_path = os.path.join(cwd, 'hash')
# 游戏数据
gamedata_path = os.path.join(cwd, 'gamedata')
resource_path = os.path.join(gamedata_path, '%s', 'gamedata')

story_path = os.path.join(resource_path, 'story')
excel_path = os.path.join(resource_path, 'excel')
handbook_info_path = os.path.join(excel_path, 'handbook_info_table.json')
stage_path = os.path.join(excel_path, 'stage_table.json')
story_table_path = os.path.join(excel_path, 'story_table.json')
roguelike_topic_path = os.path.join(excel_path, 'roguelike_topic_table.json')
story_review_path = os.path.join(excel_path, 'story_review_table.json')
activity_path = os.path.join(excel_path, 'activity_table.json')
char_path = os.path.join(excel_path, 'character_table.json')

support_language = ['zh_CN', 'ja_JP', 'en_US']

invalid_story_id = ['act1vautochess','level_act1vautochess_entry']