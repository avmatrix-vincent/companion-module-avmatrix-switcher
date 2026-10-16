import re


class ChromeConfig:

    fetch_resolution_ratio_list = [
        (720, 480),
        (720, 576),
        (1280, 720),
        (1920, 1080),
        (3840, 2160),
        (4096, 2160)
    ]

    def __init__(self):
        self.using_luma = False
        self.using_chroma = False
        self.__current_ratio_index = 3

    def set_current_ratio_index(self, index):
        self.__current_ratio_index = index

    def set_ratio_by_format(self, format):
        value = int(re.match(r"^(\d+)\w", format).group(1))
        print("Current Input Format3:", value)
        if value == 480:
            chroma_config.set_current_ratio_index(0)
        elif value == 576:
            chroma_config.set_current_ratio_index(1)
        elif value == 720:
            chroma_config.set_current_ratio_index(2)
        elif value == 1080:
            chroma_config.set_current_ratio_index(3)
        elif value == 2160:
            chroma_config.set_current_ratio_index(4)
        elif value == 4096:
            chroma_config.set_current_ratio_index(5)

    # 获取当前采样分辨率
    def get_fetch_resolution_ratio(self):
        return self.fetch_resolution_ratio_list[self.__current_ratio_index]


chroma_config = ChromeConfig()
# chroma_config.set_ratio_by_format("1080I60")
