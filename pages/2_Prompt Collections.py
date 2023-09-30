
import streamlit as st
import json
import os
from datetime import datetime
import os
import shutil
import pandas as pd
from PIL import Image

# load helper file for prompt category
dfpromptcategory = pd.read_csv('./helpers/promptcategory.csv')

# Extract the 'subtaskid' column and convert it to a list
promptcategory_list = dfpromptcategory['subtaskid'].tolist()

favicon = Image.open("images/robot-icon2.png")
st.set_page_config(page_title="Main Page", page_icon=favicon, layout="wide")

# Read the contents from the CSS file
with open("css/styles.css", "r") as f:
    css = f.read()

# Include the CSS in the Streamlit app
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


# set collections_path
collections_path = "./collections"

def generate_collection_id():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"col-{timestamp}"

from datetime import datetime

def create_empty_collection():
    collection_id = generate_collection_id()
    current_datetime = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")  # ISO 8601 format
    collection = {
        "collectionid": collection_id,
        "collectionname": "New Collection",
        "collectionusage": "",
        "collectionrelease": current_datetime,  # Set the release date to current date and time
        "collectionmodel": [],
        "userskillfocus":[],
        "systemmessage": "",
        "systemmessageusage": "",
        "usermessages": [
            {
                "id": i,
                "title": f"New Message {i}",
                "usage": "",
                "directive": "",
                "task": "",
                "lastupdatedby": "",
                "lastupdated": "",
                "promptcategory": "",
            } for i in range(1, 6)
        ]
    }
    return collection



def save_collection(collection, directory=collections_path):
    file_name = f"{collection['collectionid']}.json"
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'w') as f:
        json.dump(collection, f, indent=4)

# Get Windows username
username = os.getlogin()

# Get all the JSON files from the "collections" subfolder
#collection_files = [f for f in os.listdir(collections_path) if f.endswith('.json')]

# List the collection files and sort them by last modified time (newest first)
collection_files = sorted([f for f in os.listdir(collections_path) if f.endswith('.json')], 
                          key=lambda x: os.path.getmtime(os.path.join(collections_path, x)), 
                          reverse=True)

# Load the collections into a dictionary
collections = {}
for file in collection_files:
    with open(os.path.join(collections_path, file), 'r') as f:
        collection = json.load(f)
        collections[collection['collectionid']] = collection

# Print Title   
st.sidebar.markdown("## Edit Collection")

# Generate the selectbox options
selectbox_options = [f"{v['collectionname']} ({k})" for k, v in collections.items()]

# Create the selectbox
new_selected_collection_id = st.sidebar.selectbox('Select An Existing Collection:', selectbox_options, help="ℹ️ Select An Existing Collection allows you to quickly access a curated set of LLM prompt templates. You can choose from existing collections tailored for specific tasks, or even create your own. To keep things simple and effective, each collection contains a maximum of 5 prompt templates. This ensures that you can focus on a handful of highly relevant tasks.")

# Allow users to select a collection
#new_selected_collection_id = st.sidebar.selectbox('Select An Existing Collection:', [f"{v['collectionname']} ({k})" for k, v in collections.items()])

# Check if the selected collection has changed and reset the current tab if it has
if "selected_collection_id" in st.session_state and st.session_state.edit_collections_selected_collection_id != new_selected_collection_id:
    st.session_state.edit_collections_current_tab = None

st.session_state.edit_collections_selected_collection_id = new_selected_collection_id
# Extract the collection ID from the selected string
selected_collection_id = st.session_state.edit_collections_selected_collection_id.split(" ")[-1][1:-1]
selected_collection = collections[selected_collection_id]

# Display and edit collection details in the sidebar
collection_name = st.sidebar.text_input("Collection Name:", selected_collection['collectionname'])

# userskillfocus
# Add the "userskillfocus" input on the sidebar
# Define the available options
# Define the path to the CSV file
csv_file_path = 'helpers/userskillfocus_options.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path, header=None)

# Convert the DataFrame to a list
userskillfocus_options = df[0].tolist()

# Extract the current value of the "collectionmodel" key
current_collection_userskillfocus = selected_collection["userskillfocus"]
print(f"Value in skillfocus: {current_collection_userskillfocus}")
# Create the multi-select list in the sidebar with the current values pre-selected
selected_userskillfocus_options = st.sidebar.multiselect(
    "Select User Skill Focus:",
    userskillfocus_options,
    default=current_collection_userskillfocus,
    help = "ℹ️ User Skill Focus refers to the specialized skill sets you can choose to hone using our LLM-powered tasks. By selecting a specific 'User Skill Focus,' you tailor the LLM engine to generate tasks that are highly relevant to your chosen area, be it data engineering, technical documentation, business communication, or any other field. This ensures that you're not just completing tasks, but also enhancing specific skills that are critical to your professional growth."
)

# Update the "collectionmodel" key with the selected options
selected_collection["userskillfocus"] = selected_userskillfocus_options

collection_usage = st.sidebar.text_area("Collection Usage:", selected_collection['collectionusage'])
system_message = st.sidebar.text_area("__:orange[System Message: (How the model should behave)]__", selected_collection['systemmessage'],height = 120)
system_message_usage = st.sidebar.text_area("System Message Usage:", selected_collection['systemmessageusage'], height = 120)
collection_release = st.sidebar.text_input("Collection Release Date:", selected_collection['collectionrelease'],disabled=True)


# collectionmodel
# Add the "collectionmodel" input on the sidebar
# Define the available options
options = ['gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4', 'gpt-4-32k', 'not specified']

# Extract the current value of the "collectionmodel" key
current_collection_model = selected_collection["collectionmodel"]

# Create the multi-select list in the sidebar with the current values pre-selected
selected_options = st.sidebar.multiselect(
    "Select Tested Models On This Collection:",
    options,
    default=current_collection_model
)

# Update the "collectionmodel" key with the selected options
selected_collection["collectionmodel"] = selected_options

# Update the selected_collection with edited values
selected_collection['collectionname'] = collection_name
selected_collection['collectionusage'] = collection_usage
selected_collection['collectionrelease'] = collection_release
selected_collection['systemmessage'] = system_message
selected_collection['systemmessageusage'] = system_message_usage
selected_collection['userskillfocus'] = selected_userskillfocus_options

# Display tab buttons for each prompt in the selected collection
tabs = [message["title"] for message in selected_collection["usermessages"]]


st.markdown("## Selected Prompt")


# Allow users to select a prompt by clicking on a tab button

# Create a list of titles with IDs for the selectbox
titles_with_ids = [f"{msg['title']} ({msg['id']})" for msg in selected_collection['usermessages']]

# Initialize session state variables if they are not already initialized
if 'edit_collections_current_tab' not in st.session_state:
    st.session_state.edit_collections_current_tab = "default_value"  # Replace 'default_value' with the initial value you want to set

# Now you can safely access st.session_state.edit_collections_current_tab
tab = st.session_state.edit_collections_current_tab if "current_tab" in st.session_state and st.session_state.edit_collections_current_tab in titles_with_ids else titles_with_ids[0]

# Get the current tab from the session state or use the first tab if not set
tab = st.session_state.edit_collections_current_tab if "current_tab" in st.session_state and st.session_state.edit_collections_current_tab in titles_with_ids else titles_with_ids[0]

# Display the selectbox with the titles and IDs
tab = st.selectbox("Select a prompt template from this collection:", titles_with_ids, index=titles_with_ids.index(tab))

# Update the session state with the selected tab
st.session_state.edit_collections_current_tab = tab


# Extract the ID from the selected option
selected_id = int(tab.split(" ")[-1][1:-1])

# Find the user message with the matching ID
selected_prompt = next(message for message in selected_collection["usermessages"] if message["id"] == selected_id)


st.markdown(f"__Title:__ {selected_prompt['title']}", help="This is the title given to the prompt template.")
st.markdown(f"__Usage:__ {selected_prompt['usage']}", help="This is a description about when to use this prompt.")
with st.expander("Expand Directive Information"):
    st.markdown(f"__Directive:__ {selected_prompt['directive']}", help="Main instructions such as format, expected output.")
with st.expander("Expand Task Information"):
    st.markdown(f"__Task:__ {selected_prompt['task']}", help="Actual Data Input and Context information.")
st.markdown(f"__Prompt Category:__ {selected_prompt['promptcategory']}", help="Pre-trained models can execute many tasks. This label identifies the actual LLM task. The prompt template provides a default category.")

# Allow users to edit the values in the main window
st.markdown("## Edit Selected Prompt")
new_title = st.text_area("__Edit Title:__", selected_prompt['title'])
new_usage = st.text_area("__Edit Usage:__", selected_prompt['usage'])
new_directive = st.text_area("__:orange[Edit Directive: (Main instructions such as format, expected output)]__", selected_prompt['directive'])
new_task = st.text_area("__:orange[Edit Task: (Actual Data Input and Context information)]__", selected_prompt['task'])

try:
    default_index = promptcategory_list.index(selected_prompt['promptcategory'])
except ValueError:
    default_index = 0  # Default index if the value is not found

new_promptcategory = st.selectbox("__Edit Prompt Category:__", promptcategory_list, index=default_index)

# Create two columns
col1, col2, col3 = st.columns(3)



# Provide a "Save" button to save the edited prompt back to the collection
if col1.button("Save Collection"):
    selected_prompt['title'] = new_title
    selected_prompt['usage'] = new_usage
    selected_prompt['directive'] = new_directive
    selected_prompt['task'] = new_task
    
    # save the last updated time is today date and time
    selected_prompt['lastupdated'] =  datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    # save the last updated by is equal to the logged in user name
    selected_prompt['lastupdatedby'] = username
    
    # save the last updated  promptcategory
    selected_prompt['promptcategory'] = new_promptcategory
    
    
    # Save the collection with the same filename from which it was read
    original_filename = None
    for file in collection_files:
        with open(os.path.join("collections", file), 'r') as f:
            collection = json.load(f)
            if collection['collectionid'] == selected_collection['collectionid']:
                original_filename = file
                break
    
    if original_filename:
        with open(os.path.join("collections", original_filename), 'w') as f:
            json.dump(selected_collection, f)
        # In the code block that handles the "Save" button:
        st.session_state.edit_collections_save_prompt_success = True
        st.experimental_rerun()

    else:
        st.error(f"Failed to find the original filename called {selected_collection['collectionid']}.json")
    
# Add a button to allow users to add a new collection
if col2.button('New Collection'):
    # Create an empty collection
    new_collection = create_empty_collection()
    # Save the new collection as a JSON file
    save_collection(new_collection, "collections")
    # Reload the collections
    collection_files = [f for f in os.listdir("collections") if f.endswith('.json')]
    collections = {}
    for file in collection_files:
        with open(os.path.join("collections", file), 'r') as f:
            collection = json.load(f)
            collections[collection['collectionid']] = collection
    # Select the new collection
    st.session_state.edit_collections_selected_collection_id = f"{new_collection['collectionname']} ({new_collection['collectionid']}"
    selected_collection_id = new_collection['collectionid']
    # In the code block that handles the "Add New Collection" button:
    st.session_state.edit_collections_add_collection_success = True
    st.experimental_rerun()

# Add a button to allow users to delete the selected collection
if col3.button('Archive This Collection'):
    # Delete the collection from the JSON file
    original_filename = None
    for file in collection_files:
        with open(os.path.join("collections", file), 'r') as f:
            collection = json.load(f)
            if collection['collectionid'] == selected_collection['collectionid']:
                original_filename = file
                break

    if original_filename:
        # Create the "collectionsarchives" folder if it does not exist
        os.makedirs("collectionsarchives", exist_ok=True)
        # Move the file to the "collectionsarchives" folder
        shutil.move(os.path.join("collections", original_filename), os.path.join("collectionsarchives", original_filename))
        # Remove the collection from the collections dictionary
        del collections[selected_collection['collectionid']]
        # Update the session state with a message indicating that the collection was deleted
        st.session_state.edit_collections_collection_deleted_message = f"Collection {selected_collection['collectionid']} was archived."
        # Repaint the screen
        st.experimental_rerun()

    else:
        st.error(f"Failed to find the original filename called {selected_collection['collectionid']}.json")

# In the main part of the app, after calling st.experimental_rerun():
if getattr(st.session_state, 'add_collection_success', False):
    st.sidebar.success("New Collection saved successfully.")
    st.session_state.edit_collections_add_collection_success = False  # Reset the flag

if getattr(st.session_state, 'save_prompt_success', False):
    st.success("Prompt saved successfully.")
    st.session_state.edit_collections_save_prompt_success = False  # Reset the flag
    
# In the main part of the app, after calling st.experimental_rerun():
if getattr(st.session_state, 'collection_deleted_message', False):
    st.sidebar.success(st.session_state.edit_collections_collection_deleted_message)
    st.session_state.edit_collections_collection_deleted_message = False  # Reset the flag