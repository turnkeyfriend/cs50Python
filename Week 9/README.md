# My CS50P Final Project - Assfynd

# A simple State Forest (NY) database

My final project is a web scraper/database builder/trip planning helper. It was broken into 3 distinct parts, all of which ended up becoming a jumbled mess at the end. Read on to have a vague idea of what should be happening.

My program uses the Beautiful Soup python module to look at the NYS DEC State Recreation Lands website. It will look at that site and extract the URLs for the 9 regions of New York. This is important to have, as without it, the next step would be impossible. Maybe.

The program then uses Beautiful Soup yet again to look at each region's html code and will pull out the names and URLs of every state forest on those pages. It ignores Multiple Use Areas and only grabs State Forest info. It will create a database in the same folder calle state_forests.db using the SQLite3 module. In this database will be the name and URL of each forest.

From there, the program will once again use Beautiful Soup to scrub through the website of each State Forest to find out if camping is permitted on the lands. If it is (if there is a camping section), it will pull out the camping info which can included the number of designated sites if there are any, or just info on where camping is permitted on forests lands. This also gets put into the database.

The program then uses the Google Maps Places API to do a search using every forest name from the database. With this it will pull the latitude and longitude coordinates and place them in the database. With this informaiton, it will use the Google Maps Distance Matrix API to find the driving distance from my town to each State Forest. This distance also goes in the database.

A quick recap: Info is pulled from the NYS DEC site for every state forest in New York. Afterward, we have a database filled with the Name, URL, Lat/Long Coordinates, Driving Distance, and camping info (if camping is permitted).

With this information, the program moves on to create a GUI interface using the tkinter python module. There is a dropdown box to select a region, and whichever region is selected will have its forests listed in a listbox below it. There are two buttons at the top to sort the list by anem or by driving distance. When a forest in the list is selected, the text box on the right will fill with camping information if that forest has camping allowed. Pretty neat, huh?

And for my final trick, I would need to know how to get to these forests once I pick one to head out to. When double clicking on a forest in the list, the program will form an URL and, using the webbrowser module, open a new browser window (or a tab if a window is already open). This tab will load a google maps page with directions on how to get to the selected forest, based on the coordinates which were pulled from the Place API.
