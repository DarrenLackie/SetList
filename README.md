## dependencies
Python3<br>
PostgreSQL<br>
SqlAlchemy<br>

## start guide
pip3 install flask<br>
pip3 install flask-sqlalchemy<br>
pip3 install python-dotenv<br>
pip3 install flask-migrate<br>
pip3 install psycopg2<br>
createdb setlist_app<br>
brew install postgresql@14 (MacOS)<br>

### in app.py
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://<your_postgres_username>@localhost:5432/setlist_app"

## Making it run
flask db upgrade<br>
flask seed<br>
flask run<br>



<!-- you should add a readme, it should contain the following -->
<!-- 1. context to the program, what is this, when did you do it, what are the technoglies used/what is needed to run the app-->
<!-- 2. some screen shots of the app, even better a youtube video, even even better host it online but that's like a whole project of it's own -->
<!-- 3. a _STEP_ by _STEP_ guide on how to get the app running, think my mum should be able to do it if she knew how to use terminal-->
