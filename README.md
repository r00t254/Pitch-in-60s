# Pitch-In-60s
# Author
Mary Auma
# Description
This is a flask application that allows users to post in 60 seconds pitches and also allows other users  to comment and upvote or downvote a pitch. It also enable the users to sign up in the applications
# Live Link
# User Story
.View pitches from the different categories. 

.Register to be allowed to log in to the application

.Comment on the different pitches posted py other uses.

.See the pitches posted by other uses.

.Vote on s pitch they have viwed by giving it a upvote or a downvote
# Behaviour Driven Development
Behaviour| Input |	Output

Load the page"""""	On page load-----	Get all posts, Select between signup and login

Select SignUp""""""	Email,Username,Password --------	Redirect to login

Select Login """"""" Username and password	-----Redirect to page with app pitches based on categories and commenting section

Select comment button	""""""Comment------	Form that you input your comment

Click on submit	""""""	'''''Redirect to all comments tamplate with your comment and other comments

# Developments
python3.8 manage.py server

.Testing the application

python3.8 manage.py test
# Technology Used
Flask

Python 3.8

Heroku
