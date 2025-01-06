import requests
import frappe
import json
from datetime import date
        
# @frappe.whitelist()
# def onload(doc, method):
#     frappe.require("/assets/knowlarity/js/contact.js")

@frappe.whitelist()
def get_contact(userid):        
    temp=None
    con=frappe.db.get_list('Contact',fields=['name','user'],filters={'user':userid})
    for i in con:
        doc=frappe.get_doc('Contact',i.name)
        if doc.phone or doc.mobile_no:
            if doc.phone:
                temp=doc.phone
            else:
                temp=doc.mobile_no
        else:
            if doc.get('phone_nos'):
                for j in doc.get('phone_nos'):
                    temp=j.phone

    if temp:
        make_call(temp)
        #22-07-2023
        # get_call_details(temp)
        # get_call_history()
    else:
        frappe.msgprint('Number not available !')


# To Make a Call MrAbhi -----------------------------------------------------------------------------------
@frappe.whitelist()
def make_call(primary_mobile):
  
    if len(primary_mobile)==10:
        primary_mobile="+91"+primary_mobile
    if len(primary_mobile)==12:
        primary_mobile="+"+primary_mobile
    if len(primary_mobile)<10:
        frappe.msgprint('Invalid Mobile Number !')
   
    km=frappe.db.get_list("Knowlarity User Mapping",fields=['name','user','agent_number','caller_id'],filters={'user':frappe.session.user})
    kas=frappe.get_doc("Knowlarity Settings")
    if km:
        for k in km:
            cell_number=k.agent_number
            caller_id=k.caller_id

        #  For Auto Agent Assign / Get Available Agent ----------------------------------------------

        url = "https://kpi.knowlarity.com/Basic/v1/account/agent"

        payload = {}
        headers = {
        'Authorization': kas.authorization,
        'x-api-key': kas.x_api_key
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        
        response_data = json.loads(str(response.text))
        objects_list = response_data["objects"]
        
        mapped_output = []
        for obj in objects_list:
            if obj["status"] == "Available" and obj["is_active"]=="true":
                mapped_obj = {
                    "phone": obj["phone"],
                    "status": obj["status"],
                    "country_code": obj["country_code"],
                    "is_active": obj["is_active"],
                }
                mapped_output.append(mapped_obj)
        
        if mapped_output:   
            if len(cell_number)==12:
                cell_number='+'+cell_number
            if len(cell_number)==10:
                cell_number='+91'+cell_number
            if len(cell_number)<10:
                frappe.throw("Invalid Mobile Number !")
            agent_number=cell_number
            lst=[]
            for item in mapped_output:
                phone=f"{item['phone']}"
                country_code=f"{item['country_code']}"

                lst.append(country_code+phone)
            # frappe.msgprint(str(lst))
            if agent_number in lst:
                frappe.msgprint('Connecting to Agent !')
            else:
                if kas.auto_agent_assign==1:
                    agent_number=lst[0]
                else:
                    frappe.msgprint('Mapped Agent Not Available !')

        else:
            frappe.msgprint('No Agents Available !')

        #--------------------------------------------------------------------------------------

        url = "https://kpi.knowlarity.com/Basic/v1/account/call/makecall"

        k_number = str(kas.k_number)
        # caller_id = str(kas.caller_id)

        # frappe.msgprint(str(k_number)+'  '+str(agent_number)+'  '+str(primary_mobile)+'  '+str(caller_id))

        payload = "{\r\n  \"k_number\": \"" + k_number + "\",\r\n  \"agent_number\": \""+agent_number+"\",\r\n  \"customer_number\": \""+primary_mobile+"\",\r\n  \"caller_id\": \""+caller_id+"\"\r\n}"
        headers = {
        'Authorization': kas.authorization,
        'x-api-key': kas.x_api_key,
        'Content-Type': 'text/plain'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        #22-07-2023
        # get_call_history()
    else:
        frappe.msgprint('Knowlarity User Mapping not found !')
        
#---------------------------------------------------------------------------------------------------


# For Todays Call Details --------------------------------------------------------------------------

@frappe.whitelist()
def get_call_details(primary_mobile):
    get_call_history()
    today = date.today()
    formatted_date = today.strftime("%Y-%m-%d")

    if len(primary_mobile)==10:
        primary_mobile="+91"+primary_mobile
    if len(primary_mobile)==12:
        primary_mobile="+"+primary_mobile
    if len(primary_mobile)<10:
        frappe.msgprint('Invalid Mobile Number !')
    
    count=1
    msg = ""

    km=frappe.db.get_list("Knowlarity User Mapping",fields=['name','user','agent_number','caller_id'],filters={'user':frappe.session.user})
    if km:
        for l in km:
            filters = {
            'start_time': ['>', f"{formatted_date} 00:00:01+05:30"],
            'agent_number':l.agent_number
            }
            kl=frappe.db.get_list('Knowlarity Call Logs',fields=['name','customer_number','uuid','agent_number','start_time','call_duration'],filters=filters)
            if kl:
                for i in kl:
                    msg+= f"<strong>{count}.  </strong>&nbsp&nbsp<strong>Customer Number:</strong> {i.customer_number}<br>"
                    msg+= f"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<strong>UUID:</strong> {i.uuid}<br>"
                    msg+= f"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<strong>Agent Number:</strong> {i.agent_number}<br>"
                    msg+= f"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<strong>Start Time:</strong> {i.start_time}<br>"
                    msg+= f"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<strong>Call Duration:</strong> {i.call_duration}<br>"
                    msg+= "<hr>"
                    msg+= "<br>"

                count+=1
                    
                frappe.msgprint(msg, title="Today's Calls:", indicator="green")
            else:
                frappe.msgprint("No calls found today.", title="Today's Calls:", indicator="blue")

#-----------------------------------------------------------------------------------------------------


# All Call History -----------------------------------------------------------------------------------

@frappe.whitelist()
def get_call_history():
    
    today = date.today()
    formatted_date = today.strftime("%Y-%m-%d")
      
    kas=frappe.get_doc("Knowlarity Settings")

    url = "https://kpi.knowlarity.com/Basic/v1/account/calllog?start_time="+formatted_date+"%2000%3A00%3A01%2B05%3A30&end_time="+formatted_date+"%2023%3A59%3A59%2B05%3A30"

    payload = {}
    headers = {
    'Authorization': kas.authorization,
    'x-api-key': kas.x_api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response_data = json.loads(str(response.text))
    objects_list = response_data["objects"] 

    mapped_output = []
    for obj in objects_list: 
            mapped_obj = {
                "customer_number": obj["customer_number"],
                "uuid": obj["uuid"],
                "agent_number": obj["agent_number"],
                "start_time": obj["start_time"],
                "call_recording": obj["call_recording"],
                "call_duration": obj["call_duration"],
            }
            mapped_output.append(mapped_obj)
   
    if mapped_output:
        for item in mapped_output:
            cn=f"{item['customer_number']}"
            uuid=f"{item['uuid']}"
            st=f"{item['start_time']}"
            an=f"{item['agent_number']}"
            cd=f"{item['call_duration']}"
            cr=f"{item['call_recording']}"
            
            post_call_history(cn,uuid,st,an,cd,cr)

#---------------------------------------------------------------------------------------------------


# Post in Knwlarity Logs Doctype -------------------------------------------------------------------

@frappe.whitelist()
def post_call_history(cn,uuid,st,an,cd,cr):   
        current_site = frappe.local.site
        kas=frappe.get_doc("Knowlarity Settings")
        kch=frappe.db.get_list("Knowlarity Call Logs",fields=['name','customer_number','start_time'],filters={'customer_number':cn,"start_time":st})
        if kch:
            pass
        else:

            # km=frappe.db.get_list("Knowlarity User Mapping",fields=['name','user','agent_number','caller_id'],filters={'user':frappe.session.user})
            # for j in km:
            #     if str(j.agent_number)==str(an)[-13:]:
            
            new_knowlarity_call_logs = frappe.new_doc("Knowlarity Call Logs")
    
            new_knowlarity_call_logs.customer_number = cn
            new_knowlarity_call_logs.uuid = uuid
            new_knowlarity_call_logs.start_time = st
            new_knowlarity_call_logs.agent_number = str(an)[-13:]
            new_knowlarity_call_logs.call_recording = cr
            new_knowlarity_call_logs.status = str(an)[:-14]
            new_knowlarity_call_logs.call_duration = cd
            
        
            new_knowlarity_call_logs.insert()

#-------------------------------------------------------------------------------------------------------
