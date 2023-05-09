---
title: "Alert"
linkTitle: "Alert"
weight: 3
bookFlatSection: true
---
# [Alert](#Alert)
desc: An Alert, a set of Events, is the smallest unit to manage incidents.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## Alert





**Alert Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Alert#create) | [CreateAlertRequest](Alert#createalertrequest) | [AlertInfo](./Alert#alertinfo) |
| [**update**](./Alert#update) | [UpdateAlertRequest](Alert#updatealertrequest) | [AlertInfo](./Alert#alertinfo) |
| [**update_state**](./Alert#update_state) | [UpdateAlertStateRequest](Alert#updatealertstaterequest) | [AlertInfo](./Alert#alertinfo) |
| [**merge**](./Alert#merge) | [MergeAlertRequest](Alert#mergealertrequest) | [AlertInfo](./Alert#alertinfo) |
| [**snooze**](./Alert#snooze) | [SnoozeAlertRequest](Alert#snoozealertrequest) | [AlertInfo](./Alert#alertinfo) |
| [**add_responder**](./Alert#add_responder) | [AlertResponderRequest](Alert#alertresponderrequest) | [AlertInfo](./Alert#alertinfo) |
| [**remove_responder**](./Alert#remove_responder) | [AlertResponderRequest](Alert#alertresponderrequest) | [AlertInfo](./Alert#alertinfo) |
| [**add_project_dependency**](./Alert#add_project_dependency) | [AlertProjectDependencyRequest](Alert#alertprojectdependencyrequest) | [AlertInfo](./Alert#alertinfo) |
| [**remove_project_dependency**](./Alert#remove_project_dependency) | [AlertProjectDependencyRequest](Alert#alertprojectdependencyrequest) | [AlertInfo](./Alert#alertinfo) |
| [**delete**](./Alert#delete) | [AlertRequest](Alert#alertrequest) | [Empty](./Alert#empty) |
| [**get**](./Alert#get) | [GetAlertRequest](Alert#getalertrequest) | [AlertInfo](./Alert#alertinfo) |
| [**list**](./Alert#list) | [AlertQuery](Alert#alertquery) | [AlertsInfo](./Alert#alertsinfo) |
| [**stat**](./Alert#stat) | [AlertStatQuery](Alert#alertstatquery) | [Struct](./Alert#struct) |



    
<br>

### create

desc: Creates a new Alert. Alerts generated with `create` method are made in a manual way. Manually made Alerts can be used for Notifications.
request_example: >-
{
"title": "sample test",
"description": "This is a description of sample.",
"urgency": "HIGH",
"project_id": "project-123456789012",
"domain_id": "domain-123456789012"
}
response_example: >-
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



> **POST** /monitoring/v1/alert/create
>






    
<br>

### update

desc: Updates a specific Alert. You can make changes in Alert settings, including the `title`, `description`, `responder`, `state`, and `urgency`. The `responder` of the Alert is a User who is assigned to respond to the Alert.
request_example: >-
{
"alert_id": "alert-123456789012",
"state": "ACKNOWLEDGED",
"urgency": "LOW",
"description": "[updating]This is a description of sample.",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"alert_number": 104053,
"alert_id": "alert-123456789012",
"title": "sample test",
"state": "ACKNOWLEDGED",
"description": "[updating]This is a description of sample. ",
"urgency": "LOW",
"severity": "NONE",
"escalation_step": 1,
"additional_info": {},
"triggered_by": "user1@email.com",
"escalation_policy_id": "ep-123456789012",
"project_id": "project-123456789012",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T01:43:08.566Z",
"updated_at": "2022-01-01T01:43:08.566Z",
"acknowledged_at": "2022-01-01T01:48:52.799Z",
"escalated_at": "2022-01-01T01:43:54.464Z"
}



> **POST** /monitoring/v1/alert/update
>






    
<br>

### update_state

desc: Updates the state of an Alert via callback URL by creating a temporary `access_key` while generating a Notification about the Alert.
request_example: >-
{
"alert_id": "alert-123456789012",
"access_key": "1q2w3e4r5t6y7u8i9o0p",
"domain_id": "domain-123456789012"
}



> **POST** /monitoring/v1/alert/update-state
>






    
<br>

### merge





> **POST** /monitoring/v1/alert/merge
>






    
<br>

### snooze





> **POST** /monitoring/v1/alert/snooze
>






    
<br>

### add_responder

desc: Adds a responder who receives a Notification about an Alert.
request_example: >-
{
"alert_id": "alert-123456789012",
"resource_type": "identity.User",
"resource_id": "user2@email.com",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"alert_number": 104053,
"alert_id": "alert-123456789012",
"title": "sample test",
"state": "ACKNOWLEDGED",
"description": "[updating]This is a description of sample. ",
"urgency": "LOW",
"severity": "NONE",
"escalation_step": 1,
"responders": [
{
"resource_type": "identity.User",
"resource_id": "user2@email.com"
}
],
"additional_info": {},
"triggered_by": "user1@email.com",
"escalation_policy_id": "ep-123456789012",
"project_id": "project-123456789012",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T01:43:08.566Z",
"updated_at": "2022-01-01T01:43:08.566Z",
"acknowledged_at": "2022-01-01T02:24:12.051Z",
"escalated_at": "2022-01-01T01:43:54.464Z"
}



> **POST** /monitoring/v1/alert/add-responder
>






    
<br>

### remove_responder

desc: Deletes a responder who receives a Notification about an Alert.
request_example: >-
{
"alert_id": "alert-123456789012",
"resource_type": "identity.User",
"resource_id": "user2@email.com",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"alert_number": 104053,
"alert_id": "alert-123456789012",
"title": "sample test",
"state": "ACKNOWLEDGED",
"description": "[updating]This is a description of sample. ",
"urgency": "LOW",
"severity": "NONE",
"escalation_step": 1,
"additional_info": {},
"triggered_by": "user1@email.com",
"escalation_policy_id": "ep-123456789012",
"project_id": "project-123456789012",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T01:43:08.566Z",
"updated_at": "2022-01-01T01:43:08.566Z",
"acknowledged_at": "2022-01-01T01:48:52.799Z",
"escalated_at": "2022-01-01T01:43:54.464Z"
}



> **POST** /monitoring/v1/alert/remove-responder
>






    
<br>

### add_project_dependency





> **POST** /monitoring/v1/alert/add-project-dependency
>






    
<br>

### remove_project_dependency





> **POST** /monitoring/v1/alert/remove-project-dependency
>






    
<br>

### delete

desc: Deletes a specific Alert and remove it from the list of Alerts. You must specify the `alert_id` of the Alert to delete.
request_example: >-
{
"alert_id": "alert-123456789012",
"domain_id": "domain-123456789012"
}



> **POST** /monitoring/v1/alert/delete
>






    
<br>

### get

desc: Gets a specific Alert. Prints detailed information about the Alert.
request_example: >-
{
"alert_id": "alert-123456789012",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"alert_number": 104053,
"alert_id": "alert-123456789012",
"title": "sample test",
"state": "ACKNOWLEDGED",
"description": "[updating]This is a description of sample. ",
"urgency": "LOW",
"severity": "NONE",
"escalation_step": 1,
"additional_info": {},
"triggered_by": "user1@email.com",
"escalation_policy_id": "ep-123456789012",
"project_id": "project-123456789012",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T01:43:08.566Z",
"updated_at": "2022-01-01T01:43:08.566Z",
"acknowledged_at": "2022-01-01T01:48:52.799Z",
"escalated_at": "2022-01-01T01:43:54.464Z"
}



> **POST** /monitoring/v1/alert/get
>






    
<br>

### list

desc: Gets a list of all Alerts. You can use a query to get a filtered list of Alerts.
request_example: >-
{
"query": {},
"domain_id": "domain-123456789012"
}
response_example: >-
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



> **POST** /monitoring/v1/alert/list
>






    
<br>

### stat





> **POST** /monitoring/v1/alert/stat
>






    


<br>
<br>

## Message



### AlertInfo
* **alert_number** (int32)  `Required` 

    
* **alert_id** (string)  `Required` 

    
* **title** (string)  `Required` 

    
* **state** (AlertState)  `Required` 

    
* **status_message** (string)  `Required` 

    
* **description** (string)  `Required` 

    
* **assignee** (string)  `Required` 

    
* **urgency** (AlertUrgency)  `Required` 

    
* **severity** (string)  `Required` 

    
* **rule** (string)  `Required` 

    
* **resource** (AlertResource)  `Required` 

    
* **provider** (string)  `Required` 

    
* **account** (string)  `Required` 

    
* **is_snoozed** (bool)  `Required` 

    
* **snoozed_end_time** (string)  `Required` 

    
* **escalation_step** (int32)  `Required` 

    
* **escalation_ttl** (int32)  `Required` 

    
* **responders** (AlertResponder)  `Required` 

    
* **project_dependencies** (string)  `Required` 

    
* **image_url** (string)  `Required` 

    
* **additional_info** (Struct)  `Required` 

    
* **triggered_by** (string)  `Required` 

    
* **webhook_id** (string)  `Required` 

    
* **escalation_policy_id** (string)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    
* **acknowledged_at** (string)  `Required` 

    
* **resolved_at** (string)  `Required` 

    
* **escalated_at** (string)  `Required` 

    <br>

### AlertProjectDependencyRequest
* **alert_id** (string)  `Required` 

  *is_required: true*

    
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### AlertQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **alert_number** (int32)  `Required` 

  *is_required: false*

    
* **alert_id** (string)  `Required` 

  *is_required: false*

    
* **title** (string)  `Required` 

  *is_required: false*

    
* **state** (AlertState)  `Required` 

  *is_required: false*

    
* **assignee** (string)  `Required` 

  *is_required: false*

    
* **urgency** (AlertUrgency)  `Required` 

  *is_required: false*

    
* **severity** (string)  `Required` 

  *is_required: false*

    
* **is_snoozed** (string)  `Required` 

  *is_required: false*

    
* **resource_id** (string)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **account** (string)  `Required` 

  *is_required: false*

    
* **triggered_by** (string)  `Required` 

  *is_required: false*

    
* **webhook_id** (string)  `Required` 

  *is_required: false*

    
* **escalation_policy_id** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### AlertRequest
* **alert_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### AlertResource
* **resource_id** (string)  `Required` 

    
* **resource_type** (string)  `Required` 

    
* **name** (string)  `Required` 

    <br>

### AlertResponder
* **resource_type** (string)  `Required` 

    
* **resource_id** (string)  `Required` 

    <br>

### AlertResponderRequest
* **alert_id** (string)  `Required` 

  *is_required: true*

    
* **resource_type** (string)  `Required` 

  *is_required: true*

    
* **resource_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### AlertStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### AlertsInfo
* **results** (AlertInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### CreateAlertRequest
* **title** (string)  `Required` 

  *is_required: true*

    
* **description** (string)  `Required` 

  *is_required: false*

    
* **assignee** (string)  `Required` 

  *is_required: false*

    
* **urgency** (AlertUrgency)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetAlertRequest
* **alert_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### MergeAlertRequest
* **alerts** (string)  `Required` 

  *is_required: true*

    
* **merge_to** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SnoozeAlertRequest
* **alert_id** (string)  `Required` 

  *is_required: true*

    
* **end_time** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateAlertRequest
* **alert_id** (string)  `Required` 

  *is_required: true*

    
* **title** (string)  `Required` 

  *is_required: false*

    
* **state** (string)  `Required` 

  *is_required: false*

    
* **status_message** (string)  `Required` 

  *is_required: false*

    
* **description** (string)  `Required` 

  *is_required: false*

    
* **assignee** (string)  `Required` 

  *is_required: false*

    
* **urgency** (AlertUrgency)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **reset_status_message** (bool)  `Required` 

  *is_required: false*

    
* **reset_description** (bool)  `Required` 

  *is_required: false*

    
* **reset_assignee** (bool)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateAlertStateRequest
* **alert_id** (string)  `Required` 

  *is_required: true*

    
* **access_key** (string)  `Required` 

  *is_required: true*

    
* **state** (string)  `Required` 

  *is_required: false*

    <br>
