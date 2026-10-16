

class SC1112_12G_Preferences(object):
    _color_space_list = ["RGB", "YUV422", "YUV444", "YUV420"]
    
    @staticmethod
    def get_color_space_list():
        return SC1112_12G_Preferences._color_space_list
    
    @staticmethod
    def get_color_space_by_index(index):
        if index >= len(SC1112_12G_Preferences._color_space_list):
            return "Unknow"
        
        return SC1112_12G_Preferences._color_space_list[index]