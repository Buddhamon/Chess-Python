#!/usr/bin/python

from pymongo import MongoClient
import tornado.web

from tornado.web import HTTPError
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options

from basehandler import BaseHandler

from sklearn.neighbors import KNeighborsClassifier
import pickle
from bson.binary import Binary
import json
import numpy as np

import sys
sys.path.append('../GameModes')
import server_chess as CHESS

chess_game = CHESS.Server_Chess()

class PrintHandlers(BaseHandler):
    def get(self):
        '''Write out to screen the handlers used
        This is a nice debugging example!
        '''
        self.set_header("Content-Type", "application/json")
        self.write(self.application.handlers_string.replace('),','),\n'))

class TestServerConnection(BaseHandler):
    """
    Tests the connection between the phone and server
    """
    def get(self):
        self.write_json({"valid": True})

class SetPlayers(BaseHandler):
    """
    Given a color and a player type, sets the player
    """
    def post(self):
        data = json.loads(self.request.body.decode("utf-8"))
        w_id = data['w_id']
        b_id = data['b_id']

        global chess_game

        chess_game = CHESS.Server_Chess()
        chess_game.setup_game(white_player_id=w_id, black_player_id=b_id)
        self.write_json({"valid": True})

class RequestMoveFromAI(BaseHandler):
    """
    Gets a move, a start and end coordinate, from the AI
    """
    pass

class RequestAvailableMoves(BaseHandler):
    """
    Gets a list of available moves for a human player
    """
    pass

class UploadHumanPlayerMove(BaseHandler):
    """
    Uploads a human player move, a start and end coordinate, and returns
        a bool value if the move is valid or not
    """
    pass

class UploadGameEvaluationData(BaseHandler):
    """
    Uploads an evaluation, 1 if white winning, 0 if tied, -1 if black
        winning, and then takes the evaluation and board position and
        uploads it to the database
    """
    pass

class UpdateModelForDatasetId(BaseHandler):
    """
    Retrains the model given a dataset ID
    """
    pass


