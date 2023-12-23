---
title: "Alert"
linkTitle: "Alert"
weight: 3
bookFlatSection: true
---
# [Alert](#Alert)
An Alert, a set of Events, is the smallest unit to manage incidents.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## Alert





**Alert Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Alert#create) | [CreateAlertRequest](Alert#createalertrequest) | [AlertInfo](Alert#alertinfo) |
| [**update**](./Alert#update) | [UpdateAlertRequest](Alert#updatealertrequest) | [AlertInfo](Alert#alertinfo) |
| [**assign_user**](./Alert#assign_user) | [AssignUserRequest](Alert#assignuserrequest) | [AlertInfo](Alert#alertinfo) |
| [**update_state**](./Alert#update_state) | [UpdateAlertStateRequest](Alert#updatealertstaterequest) | [AlertInfo](Alert#alertinfo) |
| [**delete**](./Alert#delete) | [AlertRequest](Alert#alertrequest) | [Empty](Alert#empty) |
| [**get**](./Alert#get) | [AlertRequest](Alert#alertrequest) | [AlertInfo](Alert#alertinfo) |
| [**list**](./Alert#list) | [AlertQuery](Alert#alertquery) | [AlertsInfo](Alert#alertsinfo) |
| [**stat**](./Alert#stat) | [AlertStatQuery](Alert#alertstatquery) | [Struct](Alert#struct) |



    
<br>

### create

Creates a new Alert. Alerts generated with `create` method are made in a manual way. Manually made Alerts can be used for Notifications.



> **POST** /monitoring/v1/alert/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateAlertRequest](./Alert#createalertrequest)

* **title** (string)   `Required` 


* **project_id** (string)   `Required` 


* **description** (string)  


* **assignee** (string)  


* **urgency** (AlertUrgency)  





{{< highlight json >}}
{
     "title": "sample test",
     "description": "This is a description of sample.",
     "urgency": "HIGH",
     "project_id": "project-123456789012",
     "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[AlertInfo](#ALERTINFO)
* **alert_number** (int32)   `Required` 

* **alert_id** (string)   `Required` 

* **title** (string)   `Required` 

* **state** (AlertState)   `Required` 

* **description** (string)   `Required` 

* **assignee** (string)   `Required` 

* **urgency** (AlertUrgency)   `Required` 

* **severity** (string)   `Required` 

* **rule** (string)   `Required` 

* **image_url** (string)   `Required` 

* **resource** (AlertResource)   `Required` 

* **provider** (string)   `Required` 

* **account** (string)   `Required` 

* **additional_info** (Struct)   `Required` 

* **escalation_step** (int32)   `Required` 

* **escalation_ttl** (int32)   `Required` 

* **triggered_by** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **webhook_id** (string)   `Required` 

* **escalation_policy_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **acknowledged_at** (string)   `Required` 

* **resolved_at** (string)   `Required` 

* **escalated_at** (string)   `Required` 



{{< highlight json >}}
{
     "alert_number": 104053,
     "alert_id": "alert-123456789012",
     "title": "sample test",
     "state": "TRIGGERED",
     "description": "This is a description of sample.",
     "urgency": "HIGH",
     "severity": "NONE",
     "escalation_step": 1,
     "additional_info": {},
     "triggered_by": "user1@email.com",
     "escalation_policy_id": "ep-123456789012",
     "project_id": "project-123456789012",
     "domain_id": "domain-123456789012",
     "created_at": "2022-01-01T01:43:08.566Z",
     "updated_at": "2022-01-01T01:43:08.566Z",
     "escalated_at": "2022-01-01T01:43:54.464Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Alert. You can make changes in Alert settings, including the `title`, `description`, `responder`, `state`, and `urgency`. The `responder` of the Alert is a User who is assigned to respond to the Alert.



> **POST** /monitoring/v1/alert/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateAlertRequest](./Alert#updatealertrequest)

* **alert_id** (string)   `Required` 


* **title** (string)  


* **state** (string)  


* **description** (string)  


* **reset_description** (bool)  


* **urgency** (AlertUrgency)  


* **project_id** (string)  





{{< highlight json >}}
{
     "alert_id": "alert-123456789012",
     "state": "ACKNOWLEDGED",
     "urgency": "LOW",
     "description": "[updating]This is a description of sample.",
     "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[AlertInfo](#ALERTINFO)
* **alert_number** (int32)   `Required` 

* **alert_id** (string)   `Required` 

* **title** (string)   `Required` 

* **state** (AlertState)   `Required` 

* **description** (string)   `Required` 

* **assignee** (string)   `Required` 

* **urgency** (AlertUrgency)   `Required` 

* **severity** (string)   `Required` 

* **rule** (string)   `Required` 

* **image_url** (string)   `Required` 

* **resource** (AlertResource)   `Required` 

* **provider** (string)   `Required` 

* **account** (string)   `Required` 

* **additional_info** (Struct)   `Required` 

* **escalation_step** (int32)   `Required` 

* **escalation_ttl** (int32)   `Required` 

* **triggered_by** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **webhook_id** (string)   `Required` 

* **escalation_policy_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **acknowledged_at** (string)   `Required` 

* **resolved_at** (string)   `Required` 

* **escalated_at** (string)   `Required` 



{{< highlight json >}}
{
     "alert_number": 104053,
     "alert_id": "alert-123456789012",
     "title": "sample test",
     "state": "TRIGGERED",
     "description": "This is a description of sample.",
     "urgency": "HIGH",
     "severity": "NONE",
     "escalation_step": 1,
     "additional_info": {},
     "triggered_by": "user1@email.com",
     "escalation_policy_id": "ep-123456789012",
     "project_id": "project-123456789012",
     "domain_id": "domain-123456789012",
     "created_at": "2022-01-01T01:43:08.566Z",
     "updated_at": "2022-01-01T01:43:08.566Z",
     "escalated_at": "2022-01-01T01:43:54.464Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### assign_user





> **POST** /monitoring/v1/alert/assign-user
>





 {{< tabs " assign_user " >}}



 {{< tab "Response Example" >}}

[AlertInfo](#ALERTINFO)
* **alert_number** (int32)   `Required` 

* **alert_id** (string)   `Required` 

* **title** (string)   `Required` 

* **state** (AlertState)   `Required` 

* **description** (string)   `Required` 

* **assignee** (string)   `Required` 

* **urgency** (AlertUrgency)   `Required` 

* **severity** (string)   `Required` 

* **rule** (string)   `Required` 

* **image_url** (string)   `Required` 

* **resource** (AlertResource)   `Required` 

* **provider** (string)   `Required` 

* **account** (string)   `Required` 

* **additional_info** (Struct)   `Required` 

* **escalation_step** (int32)   `Required` 

* **escalation_ttl** (int32)   `Required` 

* **triggered_by** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **webhook_id** (string)   `Required` 

* **escalation_policy_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **acknowledged_at** (string)   `Required` 

* **resolved_at** (string)   `Required` 

* **escalated_at** (string)   `Required` 



{{< highlight json >}}
{
     "alert_number": 104053,
     "alert_id": "alert-123456789012",
     "title": "sample test",
     "state": "TRIGGERED",
     "description": "This is a description of sample.",
     "urgency": "HIGH",
     "severity": "NONE",
     "escalation_step": 1,
     "additional_info": {},
     "triggered_by": "user1@email.com",
     "escalation_policy_id": "ep-123456789012",
     "project_id": "project-123456789012",
     "domain_id": "domain-123456789012",
     "created_at": "2022-01-01T01:43:08.566Z",
     "updated_at": "2022-01-01T01:43:08.566Z",
     "escalated_at": "2022-01-01T01:43:54.464Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update_state

Updates the state of an Alert via callback URL by creating a temporary `access_key` while generating a Notification about the Alert.
+noauth







 {{< tabs " update_state " >}}

 {{< tab "Request Example" >}}



[UpdateAlertStateRequest](./Alert#updatealertstaterequest)

* **alert_id** (string)   `Required` 


* **access_key** (string)   `Required` 


* **state** (string)   `Required` 





{{< highlight json >}}
{
     "alert_id": "alert-123456789012",
     "access_key": "1q2w3e4r5t6y7u8i9o0p",
     "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[AlertInfo](#ALERTINFO)
* **alert_number** (int32)   `Required` 

* **alert_id** (string)   `Required` 

* **title** (string)   `Required` 

* **state** (AlertState)   `Required` 

* **description** (string)   `Required` 

* **assignee** (string)   `Required` 

* **urgency** (AlertUrgency)   `Required` 

* **severity** (string)   `Required` 

* **rule** (string)   `Required` 

* **image_url** (string)   `Required` 

* **resource** (AlertResource)   `Required` 

* **provider** (string)   `Required` 

* **account** (string)   `Required` 

* **additional_info** (Struct)   `Required` 

* **escalation_step** (int32)   `Required` 

* **escalation_ttl** (int32)   `Required` 

* **triggered_by** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **webhook_id** (string)   `Required` 

* **escalation_policy_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **acknowledged_at** (string)   `Required` 

* **resolved_at** (string)   `Required` 

* **escalated_at** (string)   `Required` 



{{< highlight json >}}
{
     "alert_number": 104053,
     "alert_id": "alert-123456789012",
     "title": "sample test",
     "state": "TRIGGERED",
     "description": "This is a description of sample.",
     "urgency": "HIGH",
     "severity": "NONE",
     "escalation_step": 1,
     "additional_info": {},
     "triggered_by": "user1@email.com",
     "escalation_policy_id": "ep-123456789012",
     "project_id": "project-123456789012",
     "domain_id": "domain-123456789012",
     "created_at": "2022-01-01T01:43:08.566Z",
     "updated_at": "2022-01-01T01:43:08.566Z",
     "escalated_at": "2022-01-01T01:43:54.464Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific Alert and remove it from the list of Alerts. You must specify the `alert_id` of the Alert to delete.



> **POST** /monitoring/v1/alert/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[AlertRequest](./Alert#alertrequest)

* **alert_id** (string)   `Required` 





{{< highlight json >}}
{
     "alert_id": "alert-123456789012",
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Alert. Prints detailed information about the Alert.



> **POST** /monitoring/v1/alert/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[AlertRequest](./Alert#alertrequest)

* **alert_id** (string)   `Required` 





{{< highlight json >}}
{
     "alert_id": "alert-123456789012",
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[AlertInfo](#ALERTINFO)
* **alert_number** (int32)   `Required` 

* **alert_id** (string)   `Required` 

* **title** (string)   `Required` 

* **state** (AlertState)   `Required` 

* **description** (string)   `Required` 

* **assignee** (string)   `Required` 

* **urgency** (AlertUrgency)   `Required` 

* **severity** (string)   `Required` 

* **rule** (string)   `Required` 

* **image_url** (string)   `Required` 

* **resource** (AlertResource)   `Required` 

* **provider** (string)   `Required` 

* **account** (string)   `Required` 

* **additional_info** (Struct)   `Required` 

* **escalation_step** (int32)   `Required` 

* **escalation_ttl** (int32)   `Required` 

* **triggered_by** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **webhook_id** (string)   `Required` 

* **escalation_policy_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **acknowledged_at** (string)   `Required` 

* **resolved_at** (string)   `Required` 

* **escalated_at** (string)   `Required` 



{{< highlight json >}}
{
     "alert_number": 104053,
     "alert_id": "alert-123456789012",
     "title": "sample test",
     "state": "TRIGGERED",
     "description": "This is a description of sample.",
     "urgency": "HIGH",
     "severity": "NONE",
     "escalation_step": 1,
     "additional_info": {},
     "triggered_by": "user1@email.com",
     "escalation_policy_id": "ep-123456789012",
     "project_id": "project-123456789012",
     "domain_id": "domain-123456789012",
     "created_at": "2022-01-01T01:43:08.566Z",
     "updated_at": "2022-01-01T01:43:08.566Z",
     "escalated_at": "2022-01-01T01:43:54.464Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Alerts. You can use a query to get a filtered list of Alerts.



> **POST** /monitoring/v1/alert/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[AlertQuery](./Alert#alertquery)

* **query** (Query)  


* **alert_number** (int32)  


* **alert_id** (string)  


* **title** (string)  


* **state** (AlertState)  


* **assignee** (string)  


* **urgency** (AlertUrgency)  


* **severity** (string)  


* **resource_id** (string)  


* **provider** (string)  


* **account** (string)  


* **triggered_by** (string)  


* **workspace_id** (string)  


* **project_id** (string)  


* **webhook_id** (string)  


* **escalation_policy_id** (string)  





{{< highlight json >}}
{
   "query": {}, 
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[AlertsInfo](#ALERTSINFO)
* **results** (AlertInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
     "results": [
     {
     "alert_number": 104057,
     "alert_id": "alert-987654321098",
     "title": "Notification of access to the bastion Host",
     "state": "TRIGGERED",
     "description": "SSH Access to stargate-dev from adm",
     "urgency": "LOW",
     "severity": "INFO",
     "resource": {
     "resource_id": "server-123456789012",
     "resource_type": "inventory.Server",
     "name": "stargate-dev"
     },
     "escalation_step": 1,
     "escalation_ttl": 1,
     "additional_info": {
     "host": "[]",
     "user": "user1"
     },
     "triggered_by": "webhook-123456789012",
     "webhook_id": "webhook-123456789012",
     "escalation_policy_id": "ep-123456789012",
     "project_id": "project-123456789012",
     "domain_id": "domain-123456789012",
     "created_at": "2022-01-01T02:46:35.934Z",
     "updated_at": "2022-01-01T02:46:35.934Z",
     "escalated_at": "2022-01-01T02:46:35.979Z"
     },
     {
     "alert_number": 104056,
     "alert_id": "alert-123456789999",
     "title": "Notification of access to the bastion Host",
     "state": "TRIGGERED",
     "description": "SSH Access to stargate-dev from user3@email.com",
     "urgency": "LOW",
     "severity": "INFO",
     "resource": {
     "resource_id": "server-123456789012",
     "resource_type": "inventory.Server",
     "name": "stargate-dev"
     },
     "escalation_step": 1,
     "escalation_ttl": 1,
     "additional_info": {
     "user": "user3@email.com",
     "host": "['111.111.111.11']"
     },
     "triggered_by": "webhook-123456789012",
     "webhook_id": "webhook-123456789012",
     "escalation_policy_id": "ep-123456789012",
     "project_id": "project-123456789012",
     "domain_id": "domain-123456789012",
     "created_at": "2022-01-01T02:46:31.391Z",
     "updated_at": "2022-01-01T02:46:31.391Z",
     "escalated_at": "2022-01-01T02:46:31.553Z"
     }
     ],
     "total_count": 21283
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /monitoring/v1/alert/stat
>






    


<br>
<br>

## Message



### AlertInfo
* **alert_number** (int32)   `Required` 

    
* **alert_id** (string)   `Required` 

    
* **title** (string)   `Required` 

    
* **state** (AlertState)   `Required` 

    
* **description** (string)   `Required` 

    
* **assignee** (string)   `Required` 

    
* **urgency** (AlertUrgency)   `Required` 

    
* **severity** (string)   `Required` 

    
* **rule** (string)   `Required` 

    
* **image_url** (string)   `Required` 

    
* **resource** (AlertResource)   `Required` 

    
* **provider** (string)   `Required` 

    
* **account** (string)   `Required` 

    
* **additional_info** (Struct)   `Required` 

    
* **escalation_step** (int32)   `Required` 

    
* **escalation_ttl** (int32)   `Required` 

    
* **triggered_by** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **webhook_id** (string)   `Required` 

    
* **escalation_policy_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    
* **acknowledged_at** (string)   `Required` 

    
* **resolved_at** (string)   `Required` 

    
* **escalated_at** (string)   `Required` 

    <br>

### AlertQuery
* **query** (Query)  

    
* **alert_number** (int32)  

    
* **alert_id** (string)  

    
* **title** (string)  

    
* **state** (AlertState)  

    
* **assignee** (string)  

    
* **urgency** (AlertUrgency)  

    
* **severity** (string)  

    
* **resource_id** (string)  

    
* **provider** (string)  

    
* **account** (string)  

    
* **triggered_by** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    
* **webhook_id** (string)  

    
* **escalation_policy_id** (string)  

    <br>

### AlertRequest
* **alert_id** (string)   `Required` 

    <br>

### AlertResource
* **resource_id** (string)   `Required` 

    
* **resource_type** (string)   `Required` 

    
* **name** (string)   `Required` 

    <br>

### AlertStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### AlertsInfo
* **results** (AlertInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### AssignUserRequest
* **alert_id** (string)   `Required` 

    
* **assignee** (string)   `Required` 

    <br>

### CreateAlertRequest
* **title** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **description** (string)  

    
* **assignee** (string)  

    
* **urgency** (AlertUrgency)  

    <br>

### UpdateAlertRequest
* **alert_id** (string)   `Required` 

    
* **title** (string)  

    
* **state** (string)  

    
* **description** (string)  

    
* **reset_description** (bool)  

    
* **urgency** (AlertUrgency)  

    
* **project_id** (string)  

    <br>

### UpdateAlertStateRequest
* **alert_id** (string)   `Required` 

    
* **access_key** (string)   `Required` 

    
* **state** (string)   `Required` 

    <br>
