def add_setting(settings_dict, kv_tuple):
  key, value = kv_tuple
  key = key.lower()
  value = value.lower()
  if key in settings_dict.keys():
    return f"Setting '{key}' already exists! Cannot add a new setting with this name."
  else:
    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings_dict, kv_tuple):
  key, value = kv_tuple
  key = key.lower()
  value = value.lower()
  if key in settings_dict.keys():
    settings_dict[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"
  else:
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_dict, key):
  key = key.lower()
  if key in settings_dict.keys():
    del settings_dict[key]
    return f"Setting '{key}' deleted successfully!"
  else:
    return f"Setting not found!"

def view_settings(settings_dict):
  if settings_dict:
    return "Current User Settings:\n" + "\n".join([f"{key.capitalize()}: {value}" for key, value in settings_dict.items()]) + "\n"
  else:
    return "No settings available."

test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
add_setting(test_settings, ('scrolling', 'enabled'))
print(view_settings(test_settings))

update_setting(test_settings, ('theme', 'light'))
print(view_settings(test_settings))

print(update_setting({'theme': 'light'}, ('volume', 'high')))

delete_setting(test_settings, 'scrolling')
print(view_settings(test_settings))

print(view_settings({}))