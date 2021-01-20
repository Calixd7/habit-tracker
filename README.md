# Habit Tracker

For this project, you will build a Django application that you can use to help track and reinforce daily habits.

You should create this project using [the Momentum Django template](https://github.com/momentumlearn/django-project-template). You can get started by running the following commands:

```
django-admin startproject --template=https://github.com/momentumlearn/django-project-template/archive/main.zip --name=Pipfile project .
pipenv install
pipenv shell
cp project/.env.sample project/.env
./manage.py makemigrations
./manage.py migrate
```

This project requires the use of [PostgreSQL](https://www.postgresql.org/) as its database, and must be deployed to [Heroku](https://www.heroku.com/). You should set both of those up first thing.
## Project specifications

* Your project should have registration and login.
* Users should be able to create a new habit tracker. Each habit should have a name and a target or goal. What is this "target"? Each habit should have a daily number of some action you want to do. Some examples:
  * I want to walk 1000 steps daily
  * I want to write 100 lines of code daily
  * I want to talk to 2 new people each day
  * I want to read 200 pages daily
  * I want to sleep 8 hours daily
* Once you have habits, you should be able to make a daily record of your activity on each habit. That record should contain a date and a number for that date.
* A user can only have one record per day per habit. You will need to use the [`constraints` option for models](https://docs.djangoproject.com/en/3.1/ref/models/constraints/) with `UniqueConstraint` to make the habit records unique by user, habit, and day.
* Optimally, users can edit/update records and add records for previous days.
* The URL for creating and updating a record should be the same and should use the habit primary key, year, month, and day in the URL. (You can put the form for creating and updating on this page or elsewhere, as your user interface dictates. This specification is in regards to the URL that makes the change in the database via POST.)
* On the detail page for a habit, you should be able to see all the records for that habit in an HTML table. Show the user whether they met their goal for that day visually somehow -- maybe via colors. Think about accessibility here -- how would a user that can't see know whether they met their goal each day?
* Make your interface as easy to use as possible. Think about what makes the most sense to enter and review data quickly. Consider using a calendar to show records.

### Some stretch goals for this project

* Add a line chart to the detail page for a habit showing your records for the last 30 days.
* On the detail page for a habit, show the best day for that habit, and the average day for that habit.
* When you list the records for a habit, show any days that don't have a record that are between the first and last record. For example, if there's a record for June 28 and a record for June 30, show June 29 as well and highlight that it has missing data. Provide a way to fill in that data easily.
* Add the ability to have "negative habits." These habits should have a goal you want to get under. For example:
  * I want to watch less than 60 minutes of TV daily
  * I want to eat less than 15 jellybeans a day
  * I want to say less than 3 curse words a day
* If a user is missing a record for a habit for the previous day, show them a message on their dashboard that lets them know and asks them to put in the record. Make it easy to jump from that message to the form to enter the data.
* Add a public dashboard for each user with data about their habits and recent statistics.

### How much of this is JavaScript?

You can make your forms a lot more usable by adding JavaScript -- to begin with, you can have a button for making a record that then shows a form without reloading the page.

If you want to add charts to your habits, you'll definitely need JavaScript. Check out [Chart.js](https://www.chartjs.org/).

## Rubric
### Completion

1. (Unsatisfactory) Does not allow for habit and record creation, does not automatically assign habits to users (via request.user) and records to habits (via URL), or does not show record history in date order.
2. (Satisfactory) Allows for creation of habits and records with automatic assignment to parent models. Shows history of records in date order (forwards or backwards). Does not allow for multiple records for the same habit per day. Allows for update and deletion of records.
3. (Exemplary) Some stretch features added.

### Design

1. (Unsatisfactory) Is not styled.
2. (Satisfactory) Has CSS via hand-written stylesheet or framework to make the site usable.
3. (Exemplary) Care taken with design features to make the site easy to use and/or accessible. Has intelligent defaults throughout the application.

### Django usage

1. (Unsatisfactory) Does not store data via models, does not use forms, or does not use GET and POST for views correctly.
2. (Satisfactory) Has User, Habit, and Record models (or equivalent), uses forms for all data entry, standard use of views and URLs.
3. (Exemplary) Writes custom functionality in views, uses Django queries to get aggregated values.

