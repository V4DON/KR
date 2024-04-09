from django.shortcuts import render
import sqlite3


def index(request):
    return render(request, 'index.html')


def first_page(request):
    return render(request, 'index.html')

def second_page(request):
    c = sqlite3.connect('identifier.db')
    cur = c.cursor()
    cur.execute("SELECT invent,adres from magaz")
    test = cur.fetchall()
    return render(request, 'main.html', {'test': test})