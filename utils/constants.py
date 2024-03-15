


class Messages:
    NO_FILE_SELECTED: str = "No File Selected"
    NO_VIDEO_SELECTED: str = "No Video Selected"


class FileInfoJSONComponents:
    # Should not change through versions.
    # If the names do change, a way to update previous JSONs and move them to the new nomenclature should be implemented.
    FILE_INFO_JSON_NAME: str = "gbxpos_file_info_json"
    BLENDER_FILE_ID_KEY: str = "blender_file_id"
    REPLAY_COLLECTION_NAME_KEY: str = "replay_collection_name"