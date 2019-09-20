from database import db
from datetime import datetime


# SQLalchemy Model for each solution in the database
class MarioModel(db.Model):
  __tablename__ = 'mario'

  index = db.Column(db.Integer, primary_key=True, autoincrement=True)
  time_log = db.Column(db.DateTime, default=datetime.utcnow)
  size = db.Column(db.String(8))
  grid = db.Column(db.PickleType)
  solution = db.Column(db.PickleType)

  def __init__(self, size, grid, solution):
    self.time_log = datetime.now()
    self.size = size
    self.grid = grid
    self.solution = solution

  def json(self):
    return {
      'time_log': self.time_log,
      'size': self.size,
      'grid': self.grid,
      'solution': self.solution
    }

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()
