# ohsiha
Ohjelmallinen sisällönhallinta 2020 harkkatyö

2020-04-17 GitHub @katrii 

Spotify API project

This is a Django-Python application made for Programmatic Content Management course 
(Ohjelmallinen sisällönhallinta) at Tampere University, Spring 2020.

- The folder "projekti" contains the basic project files. 
- In the folder "accounts" files needed for user authentication system and registration can be found. 
- The folder "ohjelma" contains the main application files.

The application utilizes Spotify API and Spotipy Python library to search for Spotify tracks.
In this case, tracks' feature analysis is applied for 100 tracks each year, from 1980 to 2019. 
Based on this data, visualizations are shown to the user. 
The application shows the average development of certain track features over time. 
Year overviews based on the average features is also offered. 

Framework: 		Django 3.0.5
Python version:		Python 3.8.1
Database: 		SQLite
Front-end component library: 	Bootstrap (https://getbootstrap.com/)
Chart visualizations: 		Highcharts (https://www.highcharts.com/)
