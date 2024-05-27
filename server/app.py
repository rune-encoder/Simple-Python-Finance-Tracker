from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)
transactions = []

@app.route("/")
