# UW5-Back-end

Background 

During the Covid-19 first lockdown my friend from University of Warwick have taken a responsibility to transform old sport website of his University into modern app. He had basic knowledge of React Native and front-end, however needed support for back-end. That is where I came in, when he discussed with me this issue, I was trilled to be part of this journey as during the first lockdown we had nothing else do to. Begun to research about the back-end framework that should provide and hold the necessary data for React Native, Django Rest Framework API (Python Framework) turned out to be the suitable option. Hence, to learn and enhance knowledge on this framework I have completed an Udemy Django Rest Framework crash course as well as Traverse Django Course from YouTube and below is description of the backend that I implemented. 

Original APP is now available in App Store and Play Store: https://play.google.com/store/apps/details?id=com.uw5.warwick5aside&gl=GB

Note: Few aspects has been removed from this reposistory comparing to original one reason being confidentiality. 

How it operates:

Our intial plan was to that I make the backend and and provide the ncecessary details to the front-end throguh the use of API, where he can fetch those data to present on the screen for user.

Below image is what I implemented, where the admin can make changes and view all the data, on the left you can see all the tables which I have impletedmented (ref: databasetables/models.py)

![WebDjango](https://user-images.githubusercontent.com/45140799/111701441-c2a0ea00-8832-11eb-9e87-90a7d9cb05c0.PNG)

I have used a Framework within Django called Django Rest Framwork, which allowed us to transfor our data into json format so it can easily be formatted and fetched by React Native, below we have used Postman software to test our urls for json data. Where we could only access it with autherization key, making it secure from unauthorized users, (ref: databasetables/serializers.py and databasetables/views.py)


![PostManApiori](https://user-images.githubusercontent.com/45140799/111702297-f29cbd00-8833-11eb-9a99-c215b8c695f9.png)


Finally, we have fetched the data using the url and authorised key which allowed us to reveive all the data into front-end instantly.


![IMG_82292](https://user-images.githubusercontent.com/45140799/111702815-be75cc00-8834-11eb-9f90-9471f737c877.jpg)

