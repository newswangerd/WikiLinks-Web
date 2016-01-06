from app import app 

from itter_search import GraphSearch
from db_lib_sqlite import DB_Connection
from sqlite3 import OperationalError
import os



@app.route('/')
@app.route('/apps/wikilinks/')



def index():
	db = os.path.join(os.path.dirname(__file__), 'wiki_links.db')
	conn = DB_Connection(db)
	search = GraphSearch(conn)
	
	path = search.get_path(29944, 42131)
	
	out = ""
	for i in path:
		out += i + " -> "
	return out
