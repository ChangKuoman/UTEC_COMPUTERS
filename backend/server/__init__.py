from distutils.log import error
import json
from select import select
from flask import (
    Flask,
    abort,
    jsonify,
    request
)
from flask_cors import CORS
from models import setup_db, User, MotherBoard, Component, Compatible