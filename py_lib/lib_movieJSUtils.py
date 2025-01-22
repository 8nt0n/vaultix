import json

def prepare_movieJS():
     with open("../@data/movies.js", "w") as file:
        file.write("var Movies = [\n")

def add_to_movieJS(path):

    with open(f"{path}/info.streamed", "r") as file:
        Title = file.readline()[:-1]
        Path = file.readline()[:-1]
        Duration = file.readline()[:-1]
        Description = file.readline()[:-1]
        Id = file.readline()[:-1]
        next(file) # skip empty line 
        Public = file.readline()[:-1]
        Uploader = file.readline()[:-1]
        Rating = file.readline()[:-1]
        Tags = file.readline()[:-1]


        data = {
            "Title": Title,
            "Path": Path,
            "Duration": Duration,
            "Description": Description,
            "Id": Id,
            "Public": Public,
            "Uploader": Uploader,
            "Rating": Rating,
            "Tags": Tags,
        }

    with open("../@data/movies.js", "a") as file:
        json_string = json.dumps(data, indent=4)  # Convert dictionary to JSON string with indentation
        file.write(json_string)  # Add a comma and newline for appending in a list
        file.write(",\n")



def close_movieJS():
     with open("../@data/movies.js", "a") as file:
        file.write("]")