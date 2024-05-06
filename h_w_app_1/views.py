from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import logging

logger = logging.getLogger('page_views')


def home(request):
    html = """
    <h1>Добро пожаловать на мой первый Django сайт!</h1>
    <p>Здесь вы найдете информацию о моем первом Django проекте.</p>
    """
    # Сохраняем данные о посещении страницы в логи
    logger.info('Посещение главной страницы')
    return HttpResponse(html)


def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Я - разработчик, создающий свой первый Django сайт.</p>
    """
    # Сохраняем данные о посещении страницы в логи
    logger.info('Посещение страницы "О себе"')
    return HttpResponse(html)
