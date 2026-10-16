from globals import relative_path, load_menu_config

menu_config = load_menu_config(relative_path('res/json/cue01_menu_config.json'))

# 获取菜单信息
MENUS = menu_config["menus"]
TRANSLATIONS = menu_config["translations"]

''' 获取一级菜单翻译（单个ListWidget项）'''
def get_menu_translation(lang, menu):
    return TRANSLATIONS.get(lang, {}).get("menus", {}).get(menu, menu)

''' 获取二级菜单翻译（单个tab 标题）'''
def get_item_translation(lang, item):
    return TRANSLATIONS[lang]["items"].get(item, item)

''' 通过下标获取 语言 索引 '''
def get_language_key_by_index(index):
    current_language = "en"
    if index == 1:
        current_language = "zh"
    else:
        current_language = "en"
    return current_language

''' 外部通过此函数传入语言index获取一级菜单列表 '''
def get_menu_list(index):
    menu_keys = list(MENUS.keys())
    current_language = get_language_key_by_index(index)    
    return [get_menu_translation(current_language, menu) for menu in menu_keys]

''' 外部通过此函数传入 语言index、一级菜单名 获取二级菜单列表'''
def get_items_list(index, menu_key):
    items = MENUS[menu_key]["items"]
    current_language = get_language_key_by_index(index)
    return [get_item_translation(current_language, item) for item in items]

''' 根据一级菜单的英文值，获取这个值对应所有语言翻译的字符串 组成的列表 '''
def get_all_language_menus_by_key(menu_key):
    """
    获取translations中所有语言的menus下的menu_key对应的翻译值
    :param menu_key: menus下的四个key之一
    :param translation_dict: translations字典
    :return: 包含所有语言翻译值的列表
    """
    translations_list = []
    for translations in TRANSLATIONS.values():
        translated_value = translations.get("menus", {}).get(menu_key, menu_key)
        translations_list.append(translated_value)
    return translations_list

# 常用，备用
CUE01_MENU_1 = get_menu_list(0) # 英文一级菜单
CUE01_MENU_1_CH = get_menu_list(1) # 中文一级菜单
# 英文二级菜单
CUE01_MENU_2_INPUT = get_items_list(0, "INPUT")
CUE01_MENU_2_OUTPUT = get_items_list(0, "OUTPUT")
CUE01_MENU_2_KEYING = get_items_list(0, "KEYING")
CUE01_MENU_2_SYSTEM = get_items_list(0, "SYSTEM")
# 中文二级菜单
CUE01_MENU_2_INPUT_CH = get_items_list(1, "INPUT")
CUE01_MENU_2_OUTPUT_CH = get_items_list(1, "OUTPUT")
CUE01_MENU_2_KEYING_CH = get_items_list(1, "KEYING")
CUE01_MENU_2_SYSTEM_CH = get_items_list(1, "SYSTEM")

###############################################################################
SC2030_MENU = ["Setting"]
SC7030_MENU = ["Setting","System"]
SC7018_MENU = ["Setting"]
SC1112_1221_MENU = ["Setting"]
SC2020_12G_MENU = ["Setting"]
SD1242_4K_MENU = ["EDID Setting"]
# UC1218_4K_MENU = ["Audio", "EDID", "Video Setting", "System"]
UC1218_4K_MENU = ["Audio", "EDID", "System"]
MIVIDCON_SH_CROSS_MENU = ["IO CONFIG", "VIDEO CONFIG", "AUDIO CONFIG", "SYSTEM INFO"]
SHARK_H4K_MENU = ["Input Status", "Switcher"]
DEFAULT_MENU = ["Unsupported"]

SC2030_MENU_CH = ["设置"]
SC7030_MENU_CH = ["输入输出设置","版本信息"]
SC7018_MENU_CH = ["输入设置"]
SC1112_1221_MENU_CH = ["输出设置"]
SC2020_12G_MENU_CH = ["设备设置"]
SD1242_4K_MENU_CH = ["EDID设置"]
# UC1218_4K_MENU_CH = ["音频", "EDID", "视频设置", "系统"]
UC1218_4K_MENU_CH = ["音频", "EDID", "系统"]
MIVIDCON_SH_CROSS_MENU_CH = ["接口配置", "视频配置", "音频配置", "系统信息"]
SHARK_H4K_MENU_CH = ["输入状态", "切换台"]
DEFAULT_MENU_CH = ["未支持"]
