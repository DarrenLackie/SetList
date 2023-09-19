# Band SetList App

A band wants to be able to manage their setlist by adding a number of songs to the `City` that they are playing in.  


## MVP

The band should be able to create a `Gig` with a name, date, venue, set-time and a `Song`. A song will have a title, the album that it's from and a running time. A band will be able to add numerous songs to each individual `Gig` and view them as a list (their set-list for that `Gig`). The band will be able to see which songs they will play in each `Gig` and click onto each song for more information. 

## EXTENSIONS

- Each `Song` has a running time which when selected will reduce the amount of time in the set-time so that a band can't play too long.
- Date and time could be handled as date type instead of as strings
- Prevent a song from being added twice
- Be able to access each album and list all songs on that album. 