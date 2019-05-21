# The Open Cookbook

A full stack CRUD application that allows users to register and log in to create, edit, update and delete recipes.

This application uses Python on the back-end with the Flask web framework, and uses MongoDB for the database. It also uses the Materialize framework on the front-end.

Built for Milestone Project no.4 in the Full Stack Software Development bootcamp at Code Institute, in the Data Centric Development module.

The live project can be viewed [here](http://the-open-cookbook.herokuapp.com/).


## UX
 
This application was built to allow users create and share recipes, as well as updating and deleting them as necessary. The application provides a registration page for new users to register on the site, and a log in page to sign in after they have registered. Any visitor can browse the recipes created on the site but logged in users, aside from adding, editing and deleting recipes, can upvote recipes using the "like" button system.

When viewing all the recipes on the site the user can search recipes by name user a free text input and can sort all recipes available on the site by alphabetical order, ascending or descending, or by cuisine type using a cuisine select drop-down menu. There is also a reset button to reset your browsing filter or sorting to reset the list back to its default state.

##### User Stories

As a user I can:
- register as a user on the site
- log in to the site once registered
- add new recipes to the site (when logged in)
- edit recipes I create on the site (when logged in)
- delete any recipes I created on the site (when logged in)
- view a list of recipes stored on the site
- see how many upvotes a recipe has received
- search the list of recipes by a recipe name
- filter the list of recipes by cuisine type
- sort the list of recipes with highest number of 'likes' first
- sort the list of recipes in alphabetical order, either ascending or descending
- click on a recipe to see information about the recipe
- click on a 'like' button to upvote a recipe  (when logged in)
- see the ingredients for a selected recipe
- see a list of allergens applicable to a recipe, if any
- read the method for preparing the recipe
- see what type of cuisine a recipe relates to

This site was built on the basis of ideas from initial wireframes created in Adobe XD and exported image files for these can be seen below. These image files as well as the XD project file can be found in the main project folder:

![wireframe prototype 1](design/AndroidMobile–1@2x.png)
![wireframe prototype 2](design/AndroidMobile–2@2x.png)
![wireframe prototype 3](design/AndroidMobile–3@2x.png)

The initial designs were based on the idea that a very basic login feature would be used but as the project developed I decided to implement a slightly more sophisticated user registration and authorisation feature and the original designs were also improved upon as the front-end of the project was being built. The improvements were made for the benefit of User Experience and to make the application more visually appealing as it was being styled throughout development.

## Features
 
##### Existing Features
- Feature 1 - The **User Registration and User Login** feature hashes user passwords so user's passwords are not stored in the application database as simple text strings as they are entered by the user when registering. This means that even by viewing the database documents you will not be able to see a user's password. The Registration form and Login forms use a lot of HTML validation including Regex pattern detection to ensure that usernames and password etc are all entered in the correct format. These forms also provide dynamic helper text to let a user know if there are any problems with anything they have entered in one of the fields, or if everything is ok. Usernames also have to be unique and the application will check through the database to ensure usernames aren't already taken before a new user can be registered.
- Feature 2 - **User Authorisation** built within the application ensures that visitors to the site cannot access URL routes for adding, updating or deleting recipes and will be redirected to the Login page if any of these URLs are entered in the browser address bar. Also, once a user is logged in they will only be able to Edit/Update or Delete recipes only created by them alone. They will not be able to do the same to recipes created by other users. The option to log out of the site is available to users who are logged into an active session.
- Feature 3 - The feature for **Adding Recipes** will be available for users who are logged in and is accessed by the 'Add' button in the bottom right-hand corner of the UI. This will take the user to a full page form that will allow them to submit detailed information about a new recipe as well as adding an image (a remotely hosted image, added by URL) dynamically adding and removing ingredients and steps in the recipe method. Again, this form provides helper text assistance to users to let them know if there are problems with entries in form fields or whether everything is ok.
- Feature 4 - When **Browsing Recipes** in the application a user can search recipe names by entering a search string in the provided text field and this will then search for recipes whose name includes the query string. There is a drop-down menu of cuisine types so a user can filter the recipe list by recipes only matching the selected cuisins. In addition to that there are sorting buttons to sort all recipes in the application by ascending and descending alphabetical order, as well as by the most 'liked' recipes.
- Feature 5 - The **Like** feature allows users who are logged in to 'Like' any recipe. This is counted as a upvote for the recipe and allows all recipes in the application to be sorted on a 'most liked' basis. If the user has 'liked' a recipe by mistake or just decides to remove their upvote they can click the 'like' button again to remove their vote.

##### Future Features
- Feature 1 - A User Dashboard is an idea that I have to allow users who are logged in to the application to simply visit their dashboard where it will simply provide a list of all recipes they have created on the site, a list of other users' recipes on the site which they have 'liked' and perhaps maybe further additional sub-features where they can view some statistics about the application in terms or recipes across the who application or just their activity, edit their own user details or change their password, etc. 
- Feature 2 - A password reset feature would be a useful feature to be built that will allow a user to reset their password when they unfortunately forget the password they entered when they registered to use the application. 
- Feature 3 - When browsing recipes on the site it could be useful to provide a feature where recipes could be filtered by the ingredients they contain. For example, a user may want to only see recipes containing Chicken. This feature could be added to the search/filter/sort menu options.

## Technologies Used

Languages, frameworks, libraries, and any other tools used to construct this project. 

- HTML 5
    - This project uses **HTML** to structure the content of the website.
- CSS 3
    - The project uses **CSS** to add additional styling to the site and refine responsive beahviour using media queries.
- [Materialize](https://materializecss.com/)
    - This project uses **Materialize** to provide the front-end grid framework and support responsive behaviour.
- JavaScript
    - The project uses **JavaScript** to add and remove content dynamically and to initialise Materialize components.
- [jQuery](https://jquery.com/)
    - This project uses **jQuery** to assist in making asynchronous requests for and also to simplify DOM node selection and manipulation.
- [Python](https://www.python.org/)
    - This project uses **Python** as the server-side programming language to provide back-end logic and serve dynamic web pages to the browser.
- [Flask](http://flask.pocoo.org/)
    - This project uses **Flask** as the back-end framework to simplify configuration of the application and routing, to render HTML templates, work with client requests  and to assist with user session management.
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
    - This project uses **Flask-PyMongo** to connect the application to MongoDB and for retrieving, inserting, updating and deleting data to and from the database.
- [MongoDB](https://www.mongodb.com/)
    - This project uses **MongoDB**, and more specifically MongoDB Atlas, as it's database system used to store data about users and recipes.

## Testing

This project was developed incrementally with continuous use of `console.log` statement in JavaScript and the `print()` function in Python to repeatedly check the changes made in the application and to ensure all changes to source code were providing the desired outcome in the browser. The site was build using Google Chrome browser (version 74) and then later tested in other browsers; FireFox (version 66) and Edge (version 42).

This project was tested for responsiveness using the Chrome Developer Tools mobile device simulator. It was also viewed on physical Samsung Galaxy A5 (2017) mobile device to ensure good responsive behaviour. The site was also tested in Mozilla Firefox (version 66) and Microsoft Edge (version 42) browsers to ensure appearance and functionality of the site was as expected across all 3 of these browsers.

All of the following routes were checked using the W3C Validation Tool [here](http://validator.w3.org), and both HTML and CSS files passed without error:
- http://online-cookbook-kes2401.c9users.io/
- http://online-cookbook-kes2401.c9users.io/login
- http://online-cookbook-kes2401.c9users.io/add_recipe
- http://online-cookbook-kes2401.c9users.io/edit_recipe/{recipe_id}/
- http://online-cookbook-kes2401.c9users.io/recipe/{recipe_id}/
- http://online-cookbook-kes2401.c9users.io/signup

There are a number of forms used on this application to accept user input including the login form, signup form, search and filter forms on the recipe list page and on the add and edit recipe pages. Various forms and levels of HTML validation has been used on form inputs to verify inputs to each form field. These forms were tested while being developed to ensure that the validation was having the desired effect and providing the desired outcome.

The site was also audited with Chrome Dev Tools' Lighthouse, with no throttling, and the results were good and were as follows on the audit report:

| Performance | Accessibility | Best Practices | SEO |
| :---------: | :------------:|:--------------:|:---:|
| 100         | 78            | 64             | 75  |

(_Progressive Web App audit scoring has been removed as the site was not intended to operate as a PWA_.)

While the Best Practices score was not as high as I would have liked it to be the main issue with the score relates to the application not being served by HTTPS. The application is hosted on Heroku and I understand SSL certificates are only provided for on paid dynos, whereas this application is currently being hosted on a free dyno.



...


## Deployment

GitHub was used for version control throught the development of the application and to host the code by pushing all code to the repo on GitHub.

This project was then deployed to Heroku to host the live application, following the steps below:

1. Log in to [Heroku](https://www.heroku.com/) and create a new app called 'the-open-cookbook'
2. Log in to Heroku in the CLI
3. Add the remote Heroku repo
4. Create the requirements.txt file by running `pip3 freeze --local > requirements.txt` in the CLI
5. Create a Procfile by running `echo web: python run.py > Procfile` in the CLI
6. Start a web process on Heroku by running `heroku ps:scale web=1` in the CLI
7. Set environment variables in Heroku for IP, PORT and MONGO_URI
8. Restart all dynos on Heroku

The live project can be viewed [here](http://the-open-cookbook.herokuapp.com/).


## Credits

##### Acknowledgements

- The Authorisation function used on routes requiring user log in was based on code from a Flask Snippet written by Alex Abbott which can be found [here](http://flask.pocoo.org/snippets/98/)
- The pagination feature used on the recipe list in this application was based on a coding tutorial by David Acosta which can be found [here](https://www.youtube.com/watch?v=Xznn-ggD0GU) on YouTube
- All initial recipes (of which there are ten), including their images, were recipes taken from the BBC GoodFood website which can be found [here](https://www.bbcgoodfood.com/recipes)