#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import pymysql

app = Flask(__name__)
api = Api(app)

conn = pymysql.connect('localhost', 'root', '', 'tpt_dua')
curs = conn.cursor(pymysql.cursors.DictCursor)

class Root(Resource):
	def get(self):
		return {'pesan': 'Halaman Utama REST API Kelompok Almay / Benny / Iqbal / Kiki / Rommy'}

class FilmsSelectAll(Resource):
	def get(self):
		sql = "SELECT * FROM cinemas"
		curs.execute(sql)
		results = curs.fetchall()
		respons = jsonify(results)
		return respons

class FilmsSelectIds(Resource):
	def get(self, id):
		sql = "SELECT * FROM cinemas WHERE id = %s"
		curs.execute(sql, id)
		results = curs.fetchall()
		respons = jsonify(results)
		return respons

class FilmsInsert(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('title', type=str)
		parser.add_argument('year', type=str)
		parser.add_argument('director', type=str)
		args = parser.parse_args()
		title = args['title']
		year = args['year']
		director = args['director']
		sql = "INSERT INTO cinemas(title, year, director) VALUES(%s, %s, %s)"
		val = (title, year, director)
		curs.execute(sql, val)
		conn.commit()
		return {'pesan': 'Insert Berhasil'}

class FilmsUpdate(Resource):
	def put(self, id):
		parser = reqparse.RequestParser()
		parser.add_argument('title', type=str)
		parser.add_argument('year', type=str)
		parser.add_argument('director', type=str)
		args = parser.parse_args()
		title = args['title']
		year = args['year']
		director = args['director']
		sql = "UPDATE cinemas SET title = %s, year = %s, director = %s WHERE id = %s"
		val = (title, year, director, id)
		curs.execute(sql, val)
		conn.commit()
		return {'pesan': 'Update Berhasil'}

class FilmsDelete(Resource):
	def delete(self, id):
		sql = "DELETE FROM cinemas WHERE id = %s"
		curs.execute(sql, id)
		conn.commit()
		return {'pesan': 'Delete Berhasil'}

class FilmsTitle(Resource):
	def get(self, title):
		sql = "SELECT * FROM cinemas WHERE title = %s"
		curs.execute(sql, title)
		results = curs.fetchall()
		respons = jsonify(results)
		return respons

class FilmsYear(Resource):
	def get(self, year):
		sql = "SELECT * FROM cinemas WHERE year = %s"
		curs.execute(sql, year)
		results = curs.fetchall()
		respons = jsonify(results)
		return respons

class FilmsDirector(Resource):
	def get(self, director):
		sql = "SELECT * FROM cinemas WHERE director = %s"
		curs.execute(sql, director)
		results = curs.fetchall()
		respons = jsonify(results)
		return respons

api.add_resource(Root, '/')
api.add_resource(FilmsSelectAll, '/films')
api.add_resource(FilmsSelectIds, '/films/<int:id>')
api.add_resource(FilmsInsert, '/films')
api.add_resource(FilmsUpdate, '/films/<int:id>')
api.add_resource(FilmsDelete, '/films/<int:id>')
api.add_resource(FilmsTitle, '/films/<string:title>')
api.add_resource(FilmsYear, '/year/<string:year>')
api.add_resource(FilmsDirector, '/director/<string:director>')

if __name__ == '__main__':
	app.run(debug=True)
