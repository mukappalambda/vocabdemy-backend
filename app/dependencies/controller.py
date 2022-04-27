def get_controller(database, controller):
    def _get_controller():
        db = database.sessions_local()
        try: 
           yield controller(db)
        finally:
            db.close()
    return _get_controller