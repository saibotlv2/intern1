import json, urllib
from bs4 import BeautifulSoup as bs

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage
)


# Showing internship info
def intern_info(line_api, event, text):
    result = ""
    image = ""
    company = open("intern_data.json", "r")
    company_data = json.load(company)

    # for debug purposes
    print(company_data)

    if text.lower() == 'list':
        result = "Cara pakai: ketik {!intern<spasi>nama perusahaan}\n"\
                 "contoh: !intern bukalapak\n\n"\
                 "Company lists:\n\n"
        
        for i in range(len(company_data[0]["list"])):
            result = result + str(i+1) + '. ' + company_data[0]["list"][i]["company"] + '\n'
    
    else:
        for i in range(len(company_data[0]["list"])):
            if text.lower() == company_data[0]["list"][i]["company"]:
                for j in range(len(company_data[0]["list"][i]["content"])):
                    result = result + company_data[0]["list"][i]["content"][j] + '\n'
                result = result + '\n'
                if len(company_data[0]["list"][i] > 2):
                    image = company_data[0]["list"][i]["image"]

        if text.lower() == 'bukalapak':
            with urllib.request.urlopen("https://careers.bukalapak.com/jobs") as url:
                data = json.loads(url.read().decode())

            for i in range(len(data)):
                for j in range(len(data[i]["list"])):
                    if data[i]["list"][j]["type"] == "Internship":
                        result = result + ('Category: ' + data[i]["category"] + '\n')
                        result = result + ('Role: ' + data[i]["list"][j]['title'] + '\n')
                        result = result + ('url: ' + data[i]["list"][j]['url'] + '\n\n')
        
        elif text.lower() == 'tokopedia':
            url = 'https://www.tokopedia.com/careers/function/internship/'
            page = urllib.request.urlopen(url)
            soup = bs(page, 'html.parser')
            for title in soup.find_all('h4', attrs={'class': 'list-div__h4'}):
                result = result + '- ' + title.text + '\n'
    
    print(result)

    if len(image) == 0:
        line_api.reply_message(
            event.reply_token, TextSendMessage(text=result)
        )
    else:
        line_api.reply_message(
            event.reply_token, TextSendMessage(text=result),
            ImageSendMessage(
                original_content_url=image,
                preview_image_url=image
            )
        )


# Showing job sites
def intern_site(line_api, event):
    result = ""
    company = open("intern_data.json", "r")
    company_data = json.load(company)

    result = "Situs pencari lowongan kerja:\n\n"\

    for i in range(len(company_data[1]["list"])):
        result = result + str(i+1) + ". " + company_data[1]["list"][i] + '\n'
    
    line_api.reply_message(
        event.reply_token, TextSendMessage(text=result)
    )
    

# Showing internship tips
def intern_tips(line_api, event, text):
    result = ""

    if text == 'cv':
        result = "Guide: https://www.careercup.com/resume\n" \
                 "Advice (good to read): https://codeburst.io/competitive-programming-label-from-an-employers-perspective-5209d6843e2a\n" \
                 "Lumayan penting (terutama kalau ga ikut lomba/aktif di komunitas teknologi) : Side projects (project yang dikerjain sendiri, bukan dari tugas kuliah)"
    elif text == 'interview':
        result = "Mayoritas ngetes kemampuan problem solving menggunakan ilmu dari materi algoritma dan struktur data\n" \
                 "Contoh soal: Implementasikan queue menggunakan 2 buah stack, dengan queue memiliki 2 method, yaitu enqueue dan dequeue\n" \
                 "Beberapa perusahaan ngetes hal lain juga, contoh: SQL, System Design, CSS, Common technologies (co: LAMP stack)\n" \
                 "\nGood to know:\n" \
                 " - Data structures: Stack, Queue, Linkedlist, Graph, Hashtable, etc\n" \
                 " - Algorithms/Paradigm: BFS, DFS, Dynamic Programming, Greedy, etc\n" \
                 "\nStudy source:\n" \
                 " - Hackerrank - https://www.hackerrank.com/ \n" \
                 " - CS Academy - https://csacademy.com/ \n" \
                 " - Leetcode - https://leetcode.com/ \n" \
                 " - Kuliah"

    
    line_api.reply_message(
        event.reply_token, TextSendMessage(text=result)
    )
