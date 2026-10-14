test_settings = {
    'theme': 'light', 
    'lang': 'spanish',
    'notifications': 'on',
}

def add_setting(settings, val_tuple):
    key, value = val_tuple
    key = key.lower()
    value = str(value).lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, val_tuple):
    key, value = val_tuple
    key = key.lower()
    value = str(value).lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    elif key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    elif key not in settings:
        return "Setting not found!"

def view_settings(settings):
    if settings == {}:
        return "No settings available."
    else:
        settings_list = [f"{key.capitalize()}: {value}" for key, value in settings.items()]
        return "Current User Settings:\n" + "\n".join(settings_list) + '\n'
