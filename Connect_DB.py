import pymysql
from flask import Flask, redirect, render_template

def insert_email(email):
    conn = pymysql.connect(host='localhost', user='root', password ='asd', db='testDB',port =3306, charset='utf8')
    curs = conn.cursor()
    query = """insert into testDB(email) values (%s)"""
    email = (email, )
    curs.executemany(query, email)
    conn.commit()
    conn.close()
