from Commands import Creator, Intern


list_command = {
    "!info": Creator.info,
    "!exit": Creator.leave,
    "!intern": Intern.intern_info,
    "!tips": Intern.intern_tips
}

def input(line_api, event, text):
    text_split = text.split(' ', 1)
    command = text_split[0].lstrip(" ")
    try:
        if len(text_split) > 1:
            list_command[command](line_api, event, text_split[1])
        else:
            list_command[command](line_api, event)
        return "Yes"
    except:
        return None