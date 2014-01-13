#Pixelicity (working title)

Pixelicity is a site where users take control of a pixelated version of the city they live in. By visiting locations in the real world, the corresponding building gets built in the virtual world. As users explore more of the city, they can see their virtual city grow as they complete challenges and gain achievements.

## User Research

Before beginning work on any website, you should first take some time to think about your users. Who do you envision using your site, what needs will your site fulfill for your target users, and how should you best design your site to fulfill these needs?

#### 1. What problem does your application address, and how does your application address it?

Pixelicity is designed to help people living in a city, who may be relatively new to it or may have been around a while, explore and discover new places. The site is based on a game-like achievement system, where by exploring more locations in the city, users can see their virtual city grow. By turning city exploration into a game, it encourages users to go places and try things they may not have otherwise.

#### 2. What are the killer features of your application?

A system for guiding and recommending directions of exploration, to allow users to slowly branch out in to more and more of the city.

Makes exploration fun, and provides additional incentives in a game-like situation.

#### 3. Identify and briefly describe your target demographic. Who do you envision using your site?

Pixelicity is targeted at young adults living in a city, either those who have been there a few years (or more) but haven't really explored past their local neighborhood, or those who are more new to the city (college students, etc.) and looking for new places to explore.

#### 4. Develop at least one use case for your site.

A user is looking to get recommendations for completing a new challenge/getting a new achievement:

* User navigates to achievements page
* User selects achievement of interest
* Site brings up map view
* Site highlights locations of several relevant businesses which have not been visited
* User mouses over/clicks on highlighted businesses to get more information

***

## Site Design

Think hard about your most complicated page. What are the important features of this page? What usability problems may come up?

#### 1. Draw out, by hand, three different designs for this page.

**Name and Logo not final**

Design 1: Scrolling (multi-page)

This design contains the main map at the top of the page, followed by detailed information a little further down the page. The information blocks would contain links to full pages with the relevant information.

![Design 1: Scrolling (multi-page)](mockup1.png?raw=true)

Design 2: Panels (multi-page)

This design contains the main map as the bulk of the page, with detailed information available in panels that slide in and out from the edge of the screen. These panels would contain links to full pages with the relevant information.

![Design 2: Panels (multi-page)](mockup2.png?raw=true)

Design 3: Tabbed (single-page)

This design contains tabs with the main map and each of the detailed information pages. Since the detailed information takes up the entire screen when tabbed to, there would not be separate pages.

![Design 3: Tabbed (single-page)](mockup3.png?raw=true)

#### 2. Make a list of 3 pros and 3 cons for each design.

Design 1:
<table>
<tr><td width="300px">**Pros**</td><td width="300px">**Cons**</td></tr>
<tr><td width="300px">Large amount of information available concurrently</td><td width="300px">Requires scrolling</td></tr>
<tr><td width="300px">Provides complete overview</td><td width="300px">Disjointed layout, not as clean looking</td></tr>
<tr><td width="300px">Most flexible layout</td><td width="300px">Not as interactive</td></tr>
</table>
<br />

Design 2:
<table>
<tr><td width="300px">**Pros**</td><td width="300px">**Cons**</td></tr>
<tr><td width="300px">Compact, can see all information at once</td><td width="300px">Navigation methods not as obvious</td></tr>
<tr><td width="300px">Provides complete overview</td><td width="300px">Cramped on small screens</td></tr>
<tr><td width="300px">Clean, interactive layout</td><td width="300px">Can only fit small amount of information on panels</td></tr>
</table>
<br />

Design 3:
<table>
<tr><td width="300px">**Pros**</td><td width="300px">**Cons**</td></tr>
<tr><td width="300px">Doesn't require navigating between separate pages</td><td width="300px">Can only see one type of information at a time</td></tr>
<tr><td width="300px">Map gets full screen</td><td width="300px">Detailed information somewhat more constrained to size of screen</td></tr>
<tr><td width="300px">Navigation immediately visible</td><td width="300px">Less flexibility</td></tr>
</table>
<br />

#### 3. Pick the best design and mock it up using an image editing program or using HTML/CSS.

Design 2: Turns out random doodles take less time than pixel art. The real version is theoretically pixel art, and/or due for a name change.

![Illustrated Mock Up](mockup.png?raw=true)

***

## Minimal Viable Product

In agile software design, a minimal viable product (MVP), or "simplest thing that works" is a product that encapsulates the essence of your application. This is an opportunity for you to think hard about what features are essential to your application and make sure that it is implementable.

#### 1. What features do you plan to implement? How critical are they to the proper functioning of your application?

The MVP will include the core features - user accounts, a map which displays visited buildings, a (reduced) set of statistics, achievements, and other game elements, and basic location-based features.

#### 2. What features do you plan to leave out? How critical are they to the proper functioning of your application?

The MVP will not include the ability to visit other's towns, or any other social features. There will also not be some customization options and game elements which would be present in the final product. These are fun additions, but not core features of the site.

Most likely, the MVP also won't include some of the visual niceties such as an animated map.

#### 3. Are there any other aspects of your application that are reduced in your MVP?

There will be a drastically reduced set of different building types (for example, instead of "Chinese Restaurant" and "Italian Restaurant" and so on, there will just be "Restaurant").

The location-based elements will play a smaller role - for judging purposes, test accounts will be preloaded with fake data and there will likely be another way to add new visited buildings.

The MVP will likely be limited to Boston-area only.

***

## Additional Questions

#### 1. Who is in your team?

Megan Belzner - belzner@mit.edu: MIT 6-3 Class of 2016 (Undergrad), taking for credit

#### 2. Which of the themes does your application match best?

Urban Living, Exploration, and Transportation: This site encourages people to branch out and discover more of the city they live in.

#### 3. What technology do you plan to use for your server-side programming?

I plan to use Django.

#### 4. What risks do you envision preventing you from successfully implementing your idea?

This idea requires both careful interfacing with APIs (for location-based elements and for map building) and significant graphical work. Hence there is the risk of ending up with either an underdeveloped frontend (difficult interface or lack of pretty pictures) or underdeveloped backend (sloppy interfacing with APIs).

In addition, the inclusion of a location-based element requires a carefully crafted website that works equally well on a computer and on a mobile device.

Also umm I kind of don't really know Django yet.

#### 5. Are you planning to participate in the competition? If so, are you competing in the main division or the rookie division?

I'm planning on competing in the main division of the competition.