#!/usr/bin/env python3


from models import Task

class DBStorage:


    def get(self, task_id):
        task = Task.query.get(task_id)
        return task

    def delete(self, task_id):
        task = self.get(task_id)
        if task:
            try:
                db.session.delete(task)
                db.session.commit()
                return True
            except SQLAlchemyError as e:
                db.session.rollback()
        return False
