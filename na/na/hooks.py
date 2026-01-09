app_name = "na"
app_title = "silling"
app_publisher = "ahmed"
app_description = "coffe 77"
app_email = "alhraryahmed110@gmail.com"
app_license = "mit"

app_include_css = "/assets/na/css/custom_workspace.css"
app_include_js = "/assets/na/js/custom_workspace.js"

fixtures = [
    {"doctype": "Custom Field"},
    {"doctype": "Client Script"},
    #{"doctype": "Workspace"},
    {"doctype": "Custom HTML Block"},
    {"doctype": "Report"},
    {"doctype": "Workflow"},
    {"doctype": "Workflow State"},
    {"doctype": "Workflow Action"},
    {"doctype": "Web Page"},
]

doc_events = {
    "Item": {
        "validate": "na.utils.set_item_description"
    }
}
