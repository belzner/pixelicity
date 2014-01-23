#Pixelicity

Pixelicity is a website designed to encourage you to explore the place you live. Alongside Mayr and some other quirky characters, you'll work to bring the city from a sparse wasteland to a bustling metropolis.

#### 1. Did any of your answers to Milestone 1 change (particularly the Additional Questions, your idea for your site, or team members)? Write the numbers for the questions whose answers have changed, and their new answers.

User Research question (2): What are the killer features of your application?

Provides a fun, quirky cast of characters alongside which to explore one's city, encouraging commitment to the site through a desire to see what will happen next.

#### 2. Which features are implemented? To what extent are they complete?

* Login System: Lacking some security features and generalized stupid-proofing, but otherwise fully functional
* Collecting Buildings: Framework in place, limited set of locations and location types (graphics, etc)
* Achievements System: Framework in place, limited set of achievements available, does not yet update asynchronously
* Statistics System: Framework in place, limited set of statistics available, does not yet update asynchronously
* Intro Sequence: Fully implemented

#### 3. Are there any features you wanted to include in your MVP from Milestone 1 that are not complete? If so, which are they?

* Geolocation Elements: Determined to be not as feasible/useful as initially believed

#### 4. What additional features do you wish to implement? How far along on those features are you?

* Collecting Residents: At certain milestones, new Pixen residents should move in. Currently in the brainstorming phase, though coding side should require only minor modifications to existing frameworks
* Customization: Low priority, would include things such as customizing map appearance or creating an avatar
* Social Features: Low priority, would involve visiting other's maps
* Mobile Site: Some content is responsive, but not all

#### 5. What technologies are you using for the back-end? Include any frameworks if relevant.

I'm using Django for the backend.

#### 6. What technologies are you using for the front-end? Include Javascript frameworks such as jQuery, templating frameworks such as Handlebars.js, and other client-side frameworks such as Ember.js or Backbone.js.

I'm using jQuery and a tiny bit of Bootstrap if that counts.

#### 7. What is the main browser you are targeting? Must be one of our supported browsers.

I'm targeting Chrome, though it appears to work fine in Firefox too.

#### 8. What implementation unknown / risks are you still facing? Consider this an exercise of imagination, not a test of confidence.

The value of Pixelicity is almost entirely based on the quirky personality realized by the buildings and residents, hence it is important that there is a sufficient sampling of both to get the right impression across. This involves significant writing and graphical work to create the personalities of these characters and locations, so I still run the risk of not being able to include enough such elements.