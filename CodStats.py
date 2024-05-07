import easyocr
from PIL import Image


def extract_table_from_image(image_path):
    # Load the image

    # Perform OCR on the image
    reader = easyocr.Reader(["en"])
    result = reader.readtext(image_path)

    players_data = []
    player = {}
    for detection in result:
        text = detection[1]
        if "#" in text:
            if player:  # If player data already exists, append to the list
                players_data.append(player)
            player = {"Player": text}  # Start a new player
        elif "Score" not in player:
            player["Score"] = int(text)
        elif "Kills" not in player:
            player["Kills"] = int(text)
        elif "Time" not in player:
            player["Time"] = text
        elif "Deaths" not in player:
            player["Deaths"] = int(text)
    if player:  # Append the last player data
        players_data.append(player)

    return players_data


# Path to the image containing the table
image_path = "example4.png"

# Extract table data from the image
table_data = extract_table_from_image(image_path)

# Print the extracted table data
for player_data in table_data:
    print(player_data)
