
import bpy, json, tempfile



def has_json(packed_json_name: str):
    return packed_json_name in bpy.data.texts


def read_json(packed_json_name: str):
    if packed_json_name in bpy.data.texts:
        packed_text_block = bpy.data.texts[packed_json_name]
        
        return json.loads(packed_text_block.as_string())
    
    print("Packed JSON data \"" + packed_json_name + "\" not found.")
    return None


def write_json(packed_json_name: str, json_data):

    # # Create a temporary file to write JSON data
    # temp_json_file = tempfile.NamedTemporaryFile(mode="w", delete=False)
    # temp_json_file_path = temp_json_file.name
    # temp_json_file.write(json.dumps(json_data))
    # temp_json_file.close()

    # # Pack the JSON file into .blend
    # bpy.ops.file.pack_all(files=[{packed_json_name: temp_json_file_path}])

    # # Remove temporary JSON file
    # temp_json_file.delete
    
    json_text = bpy.data.texts.new(packed_json_name)
    json_text.write(json.dumps(json_data))