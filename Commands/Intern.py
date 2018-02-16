import json, urllib

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

# Showing internship info
def intern_info(line_api, event, text):
    result = ""

    if text == 'list':
        result = "Cara pakai: ketik {!intern<spasi>nama perusahaan}\n"\
                 "contoh: !intern bukalapak\n\n"\
                 "Company lists:\n"\
                 "- bukalapak\n"\
                 "- tokopedia\n"\
                 "- kata.ai\n"\
                 "- go-life\n"\

    elif text == 'bukalapak':
        result = "Internship / Full Time at Bukalapak\n\n"\
                 "Durasi minimal 2,5 bulan\n\n"

        with urllib.request.urlopen("https://careers.bukalapak.com/jobs") as url:
            data_bl = json.loads(url.read().decode())

        for i in range(len(data_bl)):
            for j in range(len(data_bl[i]["list"])):
                if data_bl[i]["list"][j]["type"] == "Internship":
                    result = result + ('Role: ' + data_bl[i]["list"][j]['title'] + '\n')
                    result = result + ('url: ' + data_bl[i]["list"][j]['url'] + '\n')

    elif text == 'tokopedia':
        result = "Internship / Full Time at Tokopedia\n\n"\
                 "Durasi minimal 2,5 bulan\n"\
                 "Link: https://www.tokopedia.com/careers/jobs/ \n"

    elif text == 'kata.ai':
        result = "Internship at Kata.ai\n\n"\
                 "Kirim cv ke jobs@kata.ai\n"\
                 "cc: rizqi@kata.ai \n"

    elif text == 'go-life':
        result = "Internship / Full Time at GO-LIFE\n\n"\
                 "Roles:\n"\
                 "1. Product Engineer\n"\
                 "2. UX Research\n\n"\
                 "contact: adi.p@go-jek.com\n"

    elif text == 'kata.ai':
        result = "Kirim cv ke jobs@kata.ai\n"\
                 "cc: rizqi@kata.ai \n"
    
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
