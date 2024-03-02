import pandas as pd
from db_config import get_redis_connection
import json
import requests

# Function to retrieve data from the API
def get_artist_data(artist_name):
    url = f"https://www.theaudiodb.com/api/v1/json/2/search.php?s={artist_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve data from the API")
        return None

r = get_redis_connection()

## r.flushall()
import redis
import json


# Sample data to insert
data = {
    "idArtist": "111236",
    "strArtist": "Phantom",
    "strLabel": "Parlophone",
    "intFormedYear": "1996",
    "strCountry": "London, England",
    "strGenre": "Alternative Rock",
    "members": [
        {"name": "Chris Martin", "role": "Vocalist and Pianist"},
        {"name": "Jonny Buckland", "role": "Guitarist"},
        {"name": "Guy Berryman", "role": "Bassist"},
        {"name": "Will Champion", "role": "Drummer"}
    ],
    "albums": [
        {"title": "Parachutes", "year": "2000"},
        {"title": "A Rush of Blood to the Head", "year": "2002"},
        {"title": "X&Y", "year": "2005"},
        {"title": "Viva la Vida or Death and All His Friends", "year": "2008"},
        {"title": "Mylo Xyloto", "year": "2011"}
    ]
}


# Insert data into Redis
r.json().set('artists:info:phantom', '.', json.dumps(data))


# Retrieve data from Redis
json_data = r.json().get('artists:info:phantom')
data = json.loads(json_data)

# Extract fields
id_artist = data['idArtist']
artist_name = data['strArtist']
label = data['strLabel']
formed_year = data['intFormedYear']
country = data['strCountry']
genre = data['strGenre']
members = data['members']
albums = data['albums']

print(f"Artist ID: {id_artist}")
print(f"Artist Name: {artist_name}")
print(f"Label: {label}")
print(f"Formed Year: {formed_year}")
print(f"Country: {country}")
print(f"Genre: {genre}")

print("\nMembers:")
for member in members:
    print(f"- {member['name']}: {member['role']}")

print("\nAlbums:")
for album in albums:
    print(f"- {album['title']} ({album['year']})")

# Sample data for the second artist
data_artist2 = {
    "idArtist": "222",
    "strArtist": "Shadow",
    "strLabel": "Universal Music",
    "intFormedYear": "2005",
    "strCountry": "Los Angeles, USA",
    "strGenre": "Indie Rock",
    "members": [
        {"name": "John Smith", "role": "Lead Vocalist"},
        {"name": "Emily Johnson", "role": "Guitarist"},
        {"name": "Michael Brown", "role": "Bassist"},
        {"name": "Sarah White", "role": "Drummer"}
    ],
    "albums": [
        {"title": "Shadows in the Dark", "year": "2010"},
        {"title": "Echoes of Silence", "year": "2013"},
        {"title": "Midnight Dreams", "year": "2017"}
    ]
}

# Insert data for the second artist into Redis
r.json().set('artists:info:shadow', '.', json.dumps(data_artist2))

# Sample data for the third artist
data_artist3 = {
    "idArtist": "333",
    "strArtist": "Blaze",
    "strLabel": "Sony Music",
    "intFormedYear": "2012",
    "strCountry": "Berlin, Germany",
    "strGenre": "Electronic",
    "members": [
        {"name": "Emma Schmidt", "role": "Lead Vocalist and Keyboardist"},
        {"name": "Max Müller", "role": "Synthesizer"},
        {"name": "Sophia Wagner", "role": "DJ and Producer"}
    ],
    "albums": [
        {"title": "Neon Nights", "year": "2015"},
        {"title": "Electric Dreams", "year": "2018"},
        {"title": "Future Fusion", "year": "2021"}
    ]
}

# Insert data for the third artist into Redis
r.json().set('artists:info:blaze', '.', json.dumps(data_artist3))

# Retrieve data for the second artist from Redis
json_data_artist2 = r.json().get('artists:info:shadow')
data_artist2 = json.loads(json_data_artist2)

# Extract fields for the second artist
id_artist2 = data_artist2['idArtist']
artist_name2 = data_artist2['strArtist']
label2 = data_artist2['strLabel']
formed_year2 = data_artist2['intFormedYear']
country2 = data_artist2['strCountry']
genre2 = data_artist2['strGenre']
members2 = data_artist2['members']
albums2 = data_artist2['albums']

# Print information for the second artist
print(f"Artist ID: {id_artist2}")
print(f"Artist Name: {artist_name2}")
print(f"Label: {label2}")
print(f"Formed Year: {formed_year2}")
print(f"Country: {country2}")
print(f"Genre: {genre2}")

print("\nMembers:")
for member in members2:
    print(f"- {member['name']}: {member['role']}")

print("\nAlbums:")
for album in albums2:
    print(f"- {album['title']} ({album['year']})")

# Retrieve data for the third artist from Redis
json_data_artist3 = r.json().get('artists:info:blaze')
data_artist3 = json.loads(json_data_artist3)

# Extract fields for the third artist
id_artist3 = data_artist3['idArtist']
artist_name3 = data_artist3['strArtist']
label3 = data_artist3['strLabel']
formed_year3 = data_artist3['intFormedYear']
country3 = data_artist3['strCountry']
genre3 = data_artist3['strGenre']
members3 = data_artist3['members']
albums3 = data_artist3['albums']

# Print information for the third artist
print(f"\nArtist ID: {id_artist3}")
print(f"Artist Name: {artist_name3}")
print(f"Label: {label3}")
print(f"Formed Year: {formed_year3}")
print(f"Country: {country3}")
print(f"Genre: {genre3}")

print("\nMembers:")
for member in members3:
    print(f"- {member['name']}: {member['role']}")

print("\nAlbums:")
for album in albums3:
    print(f"- {album['title']} ({album['year']})")

# Retrieve data from the API
artist_name = "coldplay"
artist_data = get_artist_data(artist_name)

if artist_data:
    print("\nArtist Data:")
    print("------------")
    for key, value in artist_data.items():
        print(f"{key}: {value}")
else:
    print("Failed to retrieve artist data from the API")

import matplotlib.pyplot as plt

# Matplotlib Chart: Distribution of albums released over the years
album_years = [int(album['year']) for album in albums]
album_titles = [album['title'] for album in albums]

plt.figure(figsize=(10, 6))
plt.bar(album_titles, album_years, color='skyblue')
plt.xlabel('Album Titles')
plt.ylabel('Release Year')
plt.title('Distribution of Albums Released Over the Years')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Aggregation: Calculate the average formed year of all the artists retrieved from the API
formed_years = [int(artist['intFormedYear']) for artist in artist_data['artists']]
average_formed_year = sum(formed_years) / len(formed_years)
print(f"Average Formed Year of Artists: {average_formed_year:.2f}")

# Search: Retrieve artist information from Redis based on user input
artist_name_to_search = input("Enter artist name to search: ")
artist_info_json = r.json().get(f"artists:info:{artist_name_to_search.lower()}")
if artist_info_json:
    artist_info = json.loads(artist_info_json)
    print("\nArtist Information:")
    for key, value in artist_info.items():
        print(f"{key}: {value}")
else:
    print(f"Artist '{artist_name_to_search}' not found in Redis.")
