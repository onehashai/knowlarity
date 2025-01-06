from . import __version__ as app_version

app_name = "knowlarity"
app_title = "Knowlarity"
app_publisher = "Abhishek Chougule"
app_description = "Knowlarity Integration"
app_email = "abhishek.c@onehash.ai"
app_license = "MIT"

# doc_events = {
#     "Contact": {
#         "onload": "knowlarity.api.onload"
#     }
# }
app_include_js = ["/assets/knowlarity/js/contact.js","/assets/knowlarity/js/lead.js","/assets/knowlarity/js/patient.js","/assets/knowlarity/js/customer.js"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/knowlarity/css/knowlarity.css"
# app_include_js = "/assets/knowlarity/js/knowlarity.js"

# include js, css files in header of web template
# web_include_css = "/assets/knowlarity/css/knowlarity.css"
# web_include_js = "/assets/knowlarity/js/knowlarity.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "knowlarity/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "knowlarity.utils.jinja_methods",
#	"filters": "knowlarity.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "knowlarity.install.before_install"
# after_install = "knowlarity.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "knowlarity.uninstall.before_uninstall"
# after_uninstall = "knowlarity.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "knowlarity.utils.before_app_install"
# after_app_install = "knowlarity.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "knowlarity.utils.before_app_uninstall"
# after_app_uninstall = "knowlarity.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "knowlarity.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
    "cron": {
	"1-59 * * * *":[
				"knowlarity.api.get_call_history"
		]
	}
#	"all": [
#		"knowlarity.tasks.all"
#	],
#	"daily": [
#		"knowlarity.tasks.daily"
#	],
#	"hourly": [
#		"knowlarity.tasks.hourly"
#	],
#	"weekly": [
#		"knowlarity.tasks.weekly"
#	],
#	"monthly": [
#		"knowlarity.tasks.monthly"
#	],
}

# Testing
# -------

# before_tests = "knowlarity.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "knowlarity.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "knowlarity.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["knowlarity.utils.before_request"]
# after_request = ["knowlarity.utils.after_request"]

# Job Events
# ----------
# before_job = ["knowlarity.utils.before_job"]
# after_job = ["knowlarity.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"knowlarity.auth.validate"
# ]
