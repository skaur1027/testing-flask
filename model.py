from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # FIXME: write a function that creates a game and adds it to the database.

    # Emptying out the existing data in case we will run it more than once
    # Game.query.delete()

    game1 = Game(name ='Tic-Tac-Toe', description = 'Must play game!')
    game2 = Game(name ='Twister', description = 'Must play game!')
    game3 = Game(name ='Monopoly', description = 'Must play game!')

    db.session.add_all([game1, game2, game3])
    db.session.commit()


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
