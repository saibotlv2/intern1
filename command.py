from Commands import Creator, Intern, Beasiswa


list_command = {
    "!info": Creator.info,
    "!exit": Creator.leave,
    "!help": Creator.help,
    "!beasiswa": Beasiswa.bea_info,
    "!webcarikerja": Intern.intern_site,
    "!intern": Intern.intern_info,
    "!tips": Intern.intern_tips
}

def input(line_api, event, text):
    text_split = text.split(' ', 1)
    command = text_split[0].lstrip(" ")
    text_param = ""
    try:
        if len(text_split) > 1:
            text_param = text_split[1].lstrip(" ")
            list_command[command](line_api, event, text_param)
        else:
            list_command[command](line_api, event)
        return "Yes"
    except:
        return None
