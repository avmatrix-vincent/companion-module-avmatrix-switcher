
class SC2020_12G_Preferences(object):
    _color_space_list = ["RGB", "YUV422", "YUV444", "YUV420"]

    _pid = 7    # sc2020_12G：7

    _sdi_sfp_out_src=["SDI/SFP In","HDMI In"]  # setting
    _sdi_sfp_out_src_sdi = ["SDI In","HDMI In"]
    _sdi_sfp_out_src_sfp = ["SFP In","HDMI In"]

    _hdmi_out_src=["HDMI In","SDI/SFP In"]  # setting
    _hdmi_out_src_sdi = ["HDMI In", "SDI In"]  # setting
    _hdmi_out_src_sfp = ["HDMI In", "SFP In"]  # setting

    _hdmi_out_range=["FULL","Limited"]    # setting
    _3g_sdi_out = ["Level-B","Level-A"]     # setting
    _hdmi_out_color_space=["RGB 4:4:4","YCbCr 4:2:2","YCbCr 4:4:4","YCbCr 4:2:0"] # setting
    _sdi_sfp_in_mode = ["SFP In","SDI In"]  # setting
    _hdmi_in_format =[]
    _sdi_sfp_in_format = []
    format_list=["No Signal","720x480i","720x576i",
                 "1280x720P","1920x1080i","1920x1080P",
                 "2048x1080i","2048x1080P","3840x2160p ",
                 "4096x2160p"]
    fresh_rate_list = ["No Signal","","23.98",
                       "24","47.95","25/50",
                       "29.97/59.94","30/60","48",
                       "50","59.94","60"]

    _hdmi_in_range = ["FULL","Limited"]
    _hdmi_in_color =["RGB 4:4:4","YCbCr 4:2:2","YCbCr 4:4:4","YCbCr 4:2:0"]
    _sdi_in_range = ["FULL","Limited"]
    _sdi_in_color =["RGB 4:4:4","YCbCr 4:2:2","YCbCr 4:4:4","YCbCr 4:2:0"]  # 跟hdmi 合并一个了  这个展暂时使用
    _dip_pc_flag = ["DIP switch control","Upper-level computer control"]
    _fan_speed = ["20%","30%","40%","50%","60%","70%","80%","90%","100%"]
    _mcu_temperature=0  # 保留
    _fpga_temperature = 0 # 保留
    _color_metry =["Rec.709","Rec.BT2020"]   # setting
    _hdmi_in_color_depth=["8bit","10bit","12bit"]

    _control_tag=["DIP","PC"]

    """
    _pid
    """
    @staticmethod
    def get_pid():
        return SC2020_12G_Preferences._pid

    """
    _control_tag
    """
    @staticmethod
    def get_control_tag_by_index(index):
        if index >= len(SC2020_12G_Preferences._control_tag):
            return "Unknow"

        return SC2020_12G_Preferences._control_tag[index]

    """
    format_list
    """
    @staticmethod
    def get_format_list_by_index(index):
        if index >= len(SC2020_12G_Preferences.format_list):
            return "Unknow"

        return SC2020_12G_Preferences.format_list[index]

    """
    fresh_rate_list
    """
    @staticmethod
    def get_fresh_rate_list_by_index(index):
        if index >= len(SC2020_12G_Preferences.fresh_rate_list):
            return "Unknow"

        return SC2020_12G_Preferences.fresh_rate_list[index]



    """
    _hdmi_in_color_depth
    """
    @staticmethod
    def get_hdmi_in_color_depth_by_index(index):
        if index >= len(SC2020_12G_Preferences._hdmi_in_color_depth):
            return "Unknow"

        return SC2020_12G_Preferences._hdmi_in_color_depth[index]

    """
    _sdi_sfp_out_src
    """
    @staticmethod
    def get_sdi_sfp_out_src():
        return SC2020_12G_Preferences._sdi_sfp_out_src

    @staticmethod
    def get_sdi_sfp_out_by_index(index):
        if index >= len(SC2020_12G_Preferences._sdi_sfp_out_src):
            return "Unknow"

        return SC2020_12G_Preferences._sdi_sfp_out_src[index]

    @staticmethod
    def get_index_by_sdi_sfp_out(source:str):
        if source in SC2020_12G_Preferences._sdi_sfp_out_src:
            index = SC2020_12G_Preferences._sdi_sfp_out_src.index(source)
            return index
        else:
            return 0xFF


    """
    _hdmi_out_src
    """
    @staticmethod
    def get_hdmi_out_src():
        return SC2020_12G_Preferences._hdmi_out_src

    @staticmethod
    def get_hdmi_out_src_by_index(index):
        if index >= len(SC2020_12G_Preferences._hdmi_out_src):
            return "Unknow"

        return SC2020_12G_Preferences._hdmi_out_src[index]

    @staticmethod
    def get_index_by_hdmi_out_src(source: str):
        if source in SC2020_12G_Preferences._hdmi_out_src:
            index = SC2020_12G_Preferences._hdmi_out_src.index(source)
            return index
        else:
            return 0xFF


    """
    _hdmi_out_range
    """
    @staticmethod
    def get_hdmi_out_range():
        return SC2020_12G_Preferences._hdmi_out_range

    @staticmethod
    def get_hdmi_out_range_by_index(index):
        if index >= len(SC2020_12G_Preferences._hdmi_out_range):
            return "Unknow"

        return SC2020_12G_Preferences._hdmi_out_range[index]

    @staticmethod
    def get_index_by_hdmi_out_range(source: str):
        if source in SC2020_12G_Preferences._hdmi_out_range:
            index = SC2020_12G_Preferences._hdmi_out_range.index(source)
            return index
        else:
            return 0xFF

    """
    _3g_sdi_out
    """
    @staticmethod
    def get_3g_sdi_out():
        return SC2020_12G_Preferences._3g_sdi_out

    @staticmethod
    def get_3g_sdi_out_by_index(index):
        if index >= len(SC2020_12G_Preferences._3g_sdi_out):
            return "Unknow"

        return SC2020_12G_Preferences._3g_sdi_out[index]

    @staticmethod
    def get_index_by_3g_sdi_out(source: str):
        if source in SC2020_12G_Preferences._3g_sdi_out:
            index = SC2020_12G_Preferences._3g_sdi_out.index(source)
            return index
        else:
            return 0xFF

    """
    _hdmi_out_color_space
    """
    @staticmethod
    def get_hdmi_out_color():
        return SC2020_12G_Preferences._hdmi_out_color_space

    @staticmethod
    def get_hdmi_out_color_by_index(index):
        if index >= len(SC2020_12G_Preferences._hdmi_out_color_space):
            return "Unknow"

        return SC2020_12G_Preferences._hdmi_out_color_space[index]

    @staticmethod
    def get_index_by_hdmi_out_color(source: str):
        if source in SC2020_12G_Preferences._hdmi_out_color_space:
            index = SC2020_12G_Preferences._hdmi_out_color_space.index(source)
            return index
        else:
            return 0xFF

    """
    _hdmi_in_color
    """
    @staticmethod
    def get_hdmi_in_color():
        return SC2020_12G_Preferences._hdmi_in_color

    @staticmethod
    def get_hdmi_in_color_by_index(index):
        if index >= len(SC2020_12G_Preferences._hdmi_in_color):
            return "Unknow"

        return SC2020_12G_Preferences._hdmi_in_color[index]

    @staticmethod
    def get_index_by_hdmi_in_color(source: str):
        if source in SC2020_12G_Preferences._hdmi_in_color:
            index = SC2020_12G_Preferences._hdmi_in_color.index(source)
            return index
        else:
            return 0xFF

    """
    _sdi_sfp_in_mode
    """
    @staticmethod
    def get_sdi_sfp_in_mode():
        return SC2020_12G_Preferences._sdi_sfp_in_mode

    @staticmethod
    def get_sdi_sfp_in_mode_by_index(index):
        if index >= len(SC2020_12G_Preferences._sdi_sfp_in_mode):
            return "Unknow"

        return SC2020_12G_Preferences._sdi_sfp_in_mode[index]

    @staticmethod
    def get_index_by_sdi_sfp_in_mode(source: str):
        if source in SC2020_12G_Preferences._sdi_sfp_in_mode:
            index = SC2020_12G_Preferences._sdi_sfp_in_mode.index(source)
            return index
        else:
            return 0xFF

    """
    _color_metry
    """
    @staticmethod
    def get_color_metry():
        return SC2020_12G_Preferences._color_metry

    @staticmethod
    def get_color_metry_by_index(index):
        if index >= len(SC2020_12G_Preferences._color_metry):
            return "Unknow"

        return SC2020_12G_Preferences._color_metry[index]

    @staticmethod
    def get_index_by_color_metry(source: str):
        if source in SC2020_12G_Preferences._color_metry:
            index = SC2020_12G_Preferences._color_metry.index(source)
            return index
        else:
            return 0xFF


    """
    _fan_speed
    """
    @staticmethod
    def get_fan_speed():
        return SC2020_12G_Preferences._fan_speed

    @staticmethod
    def get_fan_speed_by_index(index):
        if index >= len(SC2020_12G_Preferences._fan_speed):
            return "Unknow"

        return SC2020_12G_Preferences._fan_speed[index]

    @staticmethod
    def get_index_by_fan_speed(source: str):
        if source in SC2020_12G_Preferences._fan_speed:
            index = SC2020_12G_Preferences._fan_speed.index(source)
            return index
        else:
            return 0xFF
