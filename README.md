## MOMA Art Data Visualization ##
## Summary ##
A website ith multiple pages showcasing data visualizations on the Moma Art Collection's database of artists. <br/>

## Visualizations: ##
<img src="/images/MOMA_Artist_Death_Dates.png" width = 500> </br>
<img src="/images/MOMA_Artist_Nationalities.png" width = 500> </br>
<img src="/images/MOMA_Artist_NationalitiesWOUSA.png" width = 500> </br>
<img src="/images/CompositeArtistsGender.png" width = 500> </br>


## Methods: ##
-A csv contianing all Moma artists, Moma Artists.csv, is read in. <br/>
-Rows with Null values for gender are dropped. <br/>
<img src="/images/HTML_screenshots/HTML_deaths.png" width = 500> </br>
-Create a bar chart for artists deaths vs. years of death. <br/>

<img src="/images/HTML_screenshots/HTML_birth.png" height=500></br>
<img src="/images/HTML_screenshots/HTML_birth_abroad.png" height=500> </br>
-Create a bar chart for artists' birthplace; create and additional one excluding artists born in America. <br/>
<img src="/images/HTML_screenshots/HTML_gender.png" height=200> </br>
<img src="/images/HTML_screenshots/HTML_gender_overall.png" height=200> </br>
<img src="/images/HTML_screenshots/HTML_HTML_gender_USJAPBRAMEX.png" height=200> </br>
-Plot a pie chart for overall artists' genders; create additional gender pie charts for the United States, Mexico, Japan, and Brazil. <br/>
-All visualizations are plotted with colors utilized in HTML and CSS. <br/>
-All visualizations are plotted with transparent backagrounds. <br/>

## Conclusions: ##

-The model predicted every image in the training set accurately. <br/>
-We received a mean accuracy score of 1.00, a perfect score.v<br/>
-We believe the data source lacks variability, give the model no room for error when test on images not too different from the images <br/>
-When utilizing the model to predict the fruit classification of images outside the dataset, the model was found to be highly erroneous.<br/>

## Data Source: ##
Artist Data is sourced from the Museum of Modern Art (MoMA) Collection<br/>
<img src="/images/HTML_screenshots/HTML_data.png" width=500>
-A snapshot of the dataset displayed through HTML. </br>

https://github.com/MuseumofModernArt/collection <br/>


