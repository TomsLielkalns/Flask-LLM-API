import csv
import io
import os
import json

def parse_file(file, abort):
    """
    Assuming json comes in the format:
    {"text": "sample text"}
    Assuming csv comes in the format:
      A
    1 text
    2 sample text
    """

    try:
        content = file.read()
        _, ext = os.path.splitext(file.filename)
        
        match ext:
            case ".txt":
                return content.decode("utf-8")
            case ".csv":
                text_parts = []
                csv_reader = csv.DictReader(io.StringIO(content.decode("utf-8")))
                for row in csv_reader:
                    if "text" in row:
                        text_parts.append(row["text"])
                if not text_parts:
                    abort(400, description="CSV file does not contain a 'text' column")
                return " ".join(text_parts)
            case ".json":
                data = json.loads(content.decode("utf-8"))
                if "text" not in data:
                    abort(400, description="JSON file does not contain a 'text' key")
                return data["text"]
            case _:
                abort(400, description="Unsupported file type. Please upload a .txt, .csv, or .json file.")
            
    except Exception as e:
        abort(400, description=f"Error processing file: {e}")