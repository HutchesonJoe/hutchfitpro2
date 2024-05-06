#!/usr/bin/python3
"""
Joe Hutcheson
Models for Flask server
"""

from extensions import db

class Client(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  age = db.Column(db.Integer)
  goal = db.Column(db.String(25))
  client_exercises = db.relationship('ClientExercise', backref='client_exercise', lazy=True)

class Exercise(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.Text)
  weight = db.Column(db.Integer)
  client_exercises = db.relationship('ClientExercise', backref='client_exercise', lazy=True)

class ClientExercise(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
  exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
  weight = db.Column(db.Integer)