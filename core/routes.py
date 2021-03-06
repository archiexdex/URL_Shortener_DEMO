import json
from datetime import datetime
from core.models import ShortUrls
from core import app, db
from flask import render_template, request, flash, redirect, url_for, jsonify, Response
from core.utils import *

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        #short_id = request.form['custom_id']

        #if short_id and ShortUrls.query.filter_by(short_id=short_id).first() is not None:
        #    flash('Please enter different custom id!')
        #    return redirect(url_for('index'))

        if not url:
            flash('The URL is required!')
            return redirect(url_for('index'))
        short_id = generate_short_id(url, 6)

        # Check the short_id does not exist
        while not ShortUrls.query.filter_by(short_id=short_id):
            short_id = generate_short_id(url, 6)

        new_link = ShortUrls(
            original_url=url, short_id=short_id, created_at=datetime.now())
        db.session.add(new_link)
        db.session.commit()
        short_url = request.host_url + short_id

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    url = request.form["url"]
    result, status = validate_url(url)
    if status != 200:
        return Response(json.dumps(result), status=status, content_type="application/json")

    short_id = generate_short_id(url, 6)
    # Check the short_id does not exist
    while not ShortUrls.query.filter_by(short_id=short_id):
        short_id = generate_short_id(url, 6)
    # Insert DB
    new_link = ShortUrls(
        original_url=url, short_id=short_id, created_at=datetime.now())
    try:
        db.session.add(new_link)
        db.session.commit()
    except:
        # TODO: maintain the response and error for db insertion
        pass
    short_url = request.host_url + short_id

    result = {"short_url": short_url}
    return Response(json.dumps(result), status=200, content_type="application/json")

@app.route('/<short_id>')
def redirect_url(short_id):
    result = ShortUrls.query.filter_by(short_id=short_id)
    link = result.first()
    if link:
        return redirect(link.original_url)
    else:
        flash('Invalid URL')
        return redirect(url_for('index'))
