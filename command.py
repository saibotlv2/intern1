from Commands import Creator, Intern


list_command = {
    "!info": Creator.info,
    "!exit": Creator.leave,
    "!help": Creator.help,
    "!intern": Intern.intern_info,
    "!tips": Intern.intern_tips
}

def input(line_api, event, text):
    text_split = text.split(' ', 1)
    command = text_split[0].lstrip(" ")
    text_param = text_split[1].lstrip(" ")
    try:
        if len(text_split) > 1:
            list_command[command](line_api, event, text_param)
        else:
            list_command[command](line_api, event)
        return "Yes"
    except:
        return None
