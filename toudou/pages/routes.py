from datetime import datetime

from flask import render_template

from toudou.pages import pages

@pages.route('/', methods=['GET'])
@pages.route('/home', methods=['GET'])
@pages.route('/index', methods=['GET'])
def home():
    title = 'Toudou - Home'
    year = datetime.utcnow().year
    return render_template('pages/home.html', title=title, year=year)


@pages.route('/about-us', methods=['GET'])
def about_us():
    title = 'Toudou - About us'
    year = datetime.utcnow().year
    return render_template('pages/about-us.html', title=title, year=year)
