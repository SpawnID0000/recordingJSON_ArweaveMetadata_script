import json
from mutagen.apev2 import APEv2
from mutagen.id3 import ID3, ID3NoHeaderError
import os

file_name = "untitled.mp3"
file_path = os.path.join(os.getcwd(), file_name)


# # Read the APEv2 tags from the file
# apev2_tags = APEv2(file_path)

# # Convert APEv2 tags to dictionary with strings
# tags = {key: str(value) for key, value in apev2_tags.items()}


try:
    # Read the ID3 tags from the file
    id3_tags = ID3(file_path)
except ID3NoHeaderError:
    # Handle the case where the file has no ID3 header
    id3_tags = {}

# Convert ID3 tags to a dictionary with strings
tags = {key: str(value) for key, value in id3_tags.items()}







# # Define a function to map the tags to the custom JSON format
# def transform_tags(tags):
#     transformed_data = {
#         "description": f"{tags['ARTIST']} - {tags['TITLE']}",
#         "image": "https_url_of_image_on_ardrive", # Replace with the actual URL
#         "name": "artistMBID_recordingMBID",  # Replace with the actual name
#         "attributes": [
#             {"customAttribute01": "artistMBID", "value": "replace_with_artistMBID"},
#             {"customAttribute02": "recordingMBID", "value": "replace_with_recordingMBID"},
#             {"customAttribute03": "AcoustID", "value": "replace_with_AcoustID"},
#             {"customAttribute04": "Track_Artist", "value": tags['ARTIST']},
#             {"customAttribute05": "Track_Title", "value": tags['TITLE']},
#             {"customAttribute06": "Year_of_First_Release", "value": tags['YEAR']},
#             {"customAttribute07": "Country_of_Primary_Release", "value": "replace_with_country"},
#             {"customAttribute08": "Label", "value": tags['PUBLISHER']},
#             {"customAttribute09": "Area", "value": "replace_with_area"},
#             {"customAttribute10": "Length", "value": tags['DURATION']},
#             {"customAttribute11": "Version", "value": "0000"},
#             {"customAttribute12": "Revision", "value": "0000"},
#             {"customAttribute13": "Format_BitDepth_SampleRate_Bitrate_xBR_QualitySetting_Source_AdditionalInfo", "value": "replace_with_format_info"},
#             # Add more attributes here
#         ]
#     }
#     return transformed_data


# Define a function to map the tags to the custom JSON format
def transform_tags(tags):
    transformed_data = {
        "description": f"{tags.get('TPE1', [''])} - {tags.get('TIT2', [''])}",
        "image": "https_url_of_image_on_ardrive",  # Replace with the actual URL
        "name": "artistMBID_recordingMBID",  # Replace with the actual name
        "attributes": [
            {"customAttribute01": "artistMBID", "value": "replace_with_artistMBID"},
            {"customAttribute02": "recordingMBID", "value": "replace_with_recordingMBID"},
            {"customAttribute03": "AcoustID", "value": "replace_with_AcoustID"},
            {"customAttribute04": "Track_Artist", "value": tags.get('TPE1', [''])},
            {"customAttribute05": "Track_Title", "value": tags.get('TIT2', [''])},
            #{"customAttribute06": "Year_of_First_Release", "value": tags.get('TOR', [''])},
            {"customAttribute07": "Year_of_First_Release", "value": "2023"},
            {"customAttribute07": "Country_of_Primary_Release", "value": "replace_with_country"},
            #{"customAttribute08": "Label", "value": tags.get('TPUB', [''])},
            {"customAttribute08": "Label", "value": "replace_with_label"},
            {"customAttribute09": "Area", "value": "replace_with_area"},
            #{"customAttribute10": "Length", "value": tags.get('TLE', [''])},
            {"customAttribute10": "Length", "value": "replace_with_length"},
            {"customAttribute11": "Version", "value": "0000"},
            {"customAttribute12": "Revision", "value": "0000"},
            #{"customAttribute13": "Format_BitDepth_SampleRate_Bitrate_xBR_QualitySetting_Source_AdditionalInfo", "value": "replace_with_format_info"},
            {"customAttribute13": "Format_BitDepth_SampleRate_Bitrate_xBR_QualitySetting_Source_AdditionalInfo", "value": "MP3_44p1kHz_320kbps_CBR_q5"},
            # Add more attributes here
        ]
    }
    return transformed_data










# Transform the tags
transformed_data = transform_tags(tags)

# Define the JSON file path
#json_file_path = os.path.join(os.getcwd(), file_name.replace(".wv", ".json"))
json_file_path = os.path.join(os.getcwd(), file_name.replace(".mp3", ".json"))

# Write the transformed data to a JSON file
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(transformed_data, json_file, ensure_ascii=False, indent=4)

print(f"Transformed metadata written to {json_file_path}")
