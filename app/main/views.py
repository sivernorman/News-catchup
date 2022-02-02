from flask import render_template,request,redirect,url_for
from ..request import get_sources,get_articles
from . import main

@main.route('/')
def index():

    business = get_sources('business')
    health  = get_sources('health')
    sports = get_sources('sports')
    technology = get_sources('technology')
    

    title = 'Home, Welcome to the best online News catch-up  Center'

    return render_template('index.html',title = title, business = business,health = health, sports = sports,technology = technology)

