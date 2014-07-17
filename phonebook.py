import json

def output_formatting(name_string):
    capitalized = [ind_name.capitalize()
        for ind_name in name_string.split(' ')]
    formatted_output = capitalized[0] + ' ' + capitalized[1]
    return formatted_output

def create(filename):
    phonebook_dict = {}
    with open(filename, 'w') as new_file:
        json.dump(phonebook_dict, new_file)
    return 'Created phonebook %s in the current directory.' % filename

def lookup(name, filename):
    try: 
        phonebook = json.load(open(filename))
        matching_entries = ''
        for entry in phonebook:
            if name.lower() in entry:
                matching_entries += (output_formatting(entry) + ' ' +
                    phonebook[entry] + '\n')
        return matching_entries
    except:
        return 'Error: That phonebook does not exist.'

def reverse_lookup(phone_number, filename):
    phonebook = json.load(open(filename))
    #Ryan reversed the phonebook dict and stored it that way so it's hashable.
    #(Time vs. space)
    for name, number in phonebook.iteritems():
        if number == phone_number:
            return output_formatting(name) + ' ' + phone_number
    return 'Error: that phone number does not exist.'

def add_number(name, phone_number, filename):
    phonebook = json.load(open(filename))
    if name.lower() not in phonebook:
        phonebook[name.lower()] = phone_number
        json.dump(phonebook, open(filename, 'w'), indent=2)
        return '%s added.' % (name)
    else:
        return 'Error: that name already exists.'

def change_number(name, phone_number, filename):
    phonebook = json.load(open(filename))
    if name.lower() in phonebook:
        phonebook[name.lower()] = phone_number
        json.dump(phonebook, open(filename, 'w'), indent=2)
        return '%s changed.' % (name)
    else:
        return 'Error: that name does not exist.'

def remove_number(name, filename):
    phonebook = json.load(open(filename))
    if name.lower() in phonebook:
        del phonebook[name.lower()]
        json.dump(phonebook, open(filename, 'w'), indent=2)
        return '%s removed.' % (name)
    else:
        return 'Error: that name does not exist.'

