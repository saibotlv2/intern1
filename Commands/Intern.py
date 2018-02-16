import json

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

def intern_info(line_api, event, text):
    text = ""

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
