from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse
from flask import Flask
import psycopg2
class Servidor():
    @csrf_exempt
    @api_view(['GET'])
    def Consultar(request):
        try:
         connection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = 'root',
            database = 'proxmox'
         )
         cursor = connection.cursor()
         cursor.execute("SELECT * FROM public.\"Pelicula\" ORDER BY id ASC ")
         rows = cursor.fetchall()
         pelicula=[]
         for row in rows :
            id= int(row[0])
            nombrePelicula=str(row[1])
            genero=str(row[2])
            pelicula.append([id,nombrePelicula,genero])
        except Exception as e:
            print(e)
        jsondata= json.dumps(pelicula)
        data = {'result':jsondata}
        resp = JsonResponse(data)
        resp['Accces-Control-Allow-Origin'] = '*'
        return resp
        