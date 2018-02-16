import json, urllib

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)


# Showing internship info
def intern_info(line_api, event, text):
    result = ""
    company = open("../intern_data.json", "r")
    company_data = json.load(company)

    if text.lower() == 'list':
        result = "Cara pakai: ketik {!intern<spasi>nama perusahaan}\n"\
                 "contoh: !intern bukalapak\n\n"\
                 "Company lists:\n\n"
        
        for i in range(len(company_data)):
            result = result + str(i+1) + '. ' + company_data[i]["company"] + '\n'
    
    else:
        for i in range(len(company_data)):
            if text.lower() == company_data[i]["company"]:
                for j in range(len(company_data[i]["content"])):
                    result = result + company_data[i]["content"][j] + '\n'
                result = result + '\n'

        if text.lower() == 'bukalapak':
            with urllib.request.urlopen("https://careers.bukalapak.com/jobs") as url:
                data = json.loads(url.read().decode())

            for j in range(len(data)):
                for k in range(len(data[j]["list"])):
                    if data[j]["list"][k]["type"] == "Internship":
                        result = result + ('Category: ' + data[j]["category"] + '\n')
                        result = result + ('Role: ' + data[j]["list"][k]['title'] + '\n')
                        result = result + ('url: ' + data[j]["list"][k]['url'] + '\n\n')

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
