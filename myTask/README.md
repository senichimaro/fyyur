# TODO Checklist Fyyur

Fully functioning site that is at least capable of doing the following, if not more, using a PostgreSQL database:

* creating new venues, artists, and creating new shows.
* searching for venues and artists.
* learning more about a specific artist or venue.



## Main Files: Project Structure

1. [ ] `app.py` -- (Missing functionality.) -- **Defines routes and controllers** which handle data and renders views to the user.

2. [x] Models in `app.py` -- (Missing functionality.) -- Defines the data models that set up the database tables.

3. [x] `config.py` -- (Missing functionality.) -- Stores configuration variables and instructions, separate from the main application code. This is where you will need to connect to the database.


## Instructions

1. Connect to database and backend.
2. **TODOS**
    * [x] 1. Connect to a database in `config.py`.
    * [x] 2. Using SQLAlchemy, set up models
    * [ ] 3. Implement form submissions for creating new Venues, Artists, and Shows. There should be proper constraints, powering the `/create` endpoints that serve the create form templates, to avoid duplicate or nonsensical form submissions. Submitting a form should create proper new records in the database.
    * [ ] 4. Implement the controllers for listing venues, artists, and shows. Note the structure of the mock data used. We want to keep the structure of the mock data.
    * [ ] 5. Implement search, powering the `/search` endpoints that serve the application's search functionalities.
    * [ ] 6. Serve venue and artist detail pages, powering the `<venue|artist>/<id>` endpoints that power the detail pages.

#### Data Handling with `Flask-WTF` Forms
The starter codes use an interactive form builder library called [Flask-WTF](https://flask-wtf.readthedocs.io/). This library provides useful functionality, such as form validation and error handling. You can peruse the Show, Venue, and Artist form builders in `forms.py` file. The WTForms are instantiated in the `app.py` file. For example, in the `create_shows()` function, the Show form is instantiated from the command: `form = ShowForm()`. To manage the request from Flask-WTF form, each field from the form has a `data` attribute containing the value from user input. For example, to handle the `venue_id` data from the Venue form, you can use: `show = Show(venue_id=form.venue_id.data)`, instead of using `request.form['venue_id']`.

Acceptance Criteria
-----

1. The web app should be successfully connected to a PostgreSQL database. A local connection to a database on your local computer is fine.
2. There should be no use of mock data throughout the app. The data structure of the mock data per controller should be kept unmodified when satisfied by real data.
3. The application should behave just as before with mock data, but now uses real data from a real backend server, with real search functionality. For example:
  * when a user submits a new artist record, the user should be able to see it populate in /artists, as well as search for the artist by name and have the search return results.
  * I should be able to go to the URL `/artist/<artist-id>` to visit a particular artist’s page using a unique ID per artist, and see real data about that particular artist.
  * Venues should continue to be displayed in groups by city and state.
  * Search should be allowed to be partial string matching and case-insensitive.
  * Past shows versus Upcoming shows should be distinguished in Venue and Artist pages.
  * A user should be able to click on the venue for an upcoming show in the Artist's page, and on that Venue's page, see the same show in the Venue Page's upcoming shows section. (assumption: artist creates venues)

4. Define the models in a different file to follow [Separation of Concerns](https://en.wikipedia.org/wiki/Separation_of_concerns) design principles. You can refactor the models to a new file, such as `models.py`.
  * The right _type_ of relationship and parent-child dynamics between models should be accurately identified and fit the needs of this particular application.
  * The relationship between the models should be accurately configured, and referential integrity amongst the models should be preserved.






## Sample Data


Four Fives
Lucena
avenida sol
+34 111 111 111
https://www.facebook.com/

https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/styles/480/public/media/image/2015/10/524042-analisis-rock-band-4.jpg?itok=LNCy91q-

https://learnenglishteens.britishcouncil.org/


Lorem Ipsum is simply dummy text of the printing and typesetting industry.






#### Venue Create
('name', 'Four Fives'),
('city', 'Armn'),
('state', 'AL'),
('address', 'Acasd'),
('phone', ''),
('genres', 'Rock n Roll'),
('facebook_link', ''),
('image_link', ''),
('website_link', ''),
('seeking_description', '')])



#### Artist Create
('name', 'Bottles'),
('city', 'Chicago'),
('state', 'AL'),
('address', 'Acasd'),
('phone', ''),
('genres', 'Rock n Roll'),
('facebook_link', ''),
('image_link', ''),
('website_link', ''),
('seeking_description', '')])




## Pending
* --- not understand ---
* TODO: on unsuccessful db insert, flash an error instead.






















































































//
