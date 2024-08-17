from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
	__tablename__ = 'todos'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100),  nullables=False)
	content = db.Column(db.String(200), nullable=False
	completed = db.Column(db.Boolean, default=False)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)


	def __ref__(self):
		return f"<Todos {self.title}>"
