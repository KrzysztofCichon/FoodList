App to generate menu and shopping list for desired number of days

The goal is to create an application, which is capable of creating a simple diet/menu/shopping list for desired timeframe.

There are  milestones defined by the creator right now:

1. Basic functionality - initial commit
2. Ability to create a menu (4 meals a day) for timeframe selected by user (current max 14), goal is to make every day unique. App should be able to save it's output into a pdf file, after user confirms in app, that generated menu suits him. After confirmation, app should save it's output to a file and open the file before termination.
3. Using a database (PostgreSQL) as a storage of meal lists and ingredients. At this point app should be able to generate a complete shopping list for a user. Also user can define for how many consecutive days meal of any type can be used (for purposes of not wasting ingredients, or for convienience and less time spent in a kitchen). Maximum timeframe will be extended up to 30 days, but the goal is to keep meals unique as long as it is possible. Also User can define how often he want's to go shopping - app will generate shopping list for every visit in a shop.,
4. Hosting an app with Django framework. Further functionalities to be defined.