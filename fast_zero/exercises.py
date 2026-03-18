from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app_exercise = FastAPI()


@app_exercise.get(
    '/exercicio-html',
    response_class=HTMLResponse,
    status_code=HTTPStatus.OK,
)
def read_exercise_html():
    return """
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <h1> Olá Mundo </h1>
    </body>
"""
