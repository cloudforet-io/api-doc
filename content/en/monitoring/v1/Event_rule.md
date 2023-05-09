---
title: "Event_rule"
linkTitle: "Event_rule"
weight: 3
bookFlatSection: true
---
# [Event_rule](#Event_rule)
desc: An EventRule is a rule to transform the request data when an Event is generated.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## Event_rule





**EventRule Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./EventRule#create) | [CreateEventRuleRequest](EventRule#createeventrulerequest) | [EventRuleInfo](./EventRule#eventruleinfo) |
| [**update**](./EventRule#update) | [UpdateEventRuleRequest](EventRule#updateeventrulerequest) | [EventRuleInfo](./EventRule#eventruleinfo) |
| [**change_order**](./EventRule#change_order) | [ChangeEventRuleOrderRequest](EventRule#changeeventruleorderrequest) | [EventRuleInfo](./EventRule#eventruleinfo) |
| [**delete**](./EventRule#delete) | [EventRuleRequest](EventRule#eventrulerequest) | [Empty](./EventRule#empty) |
| [**get**](./EventRule#get) | [GetEventRuleRequest](EventRule#geteventrulerequest) | [EventRuleInfo](./EventRule#eventruleinfo) |
| [**list**](./EventRule#list) | [EventRuleQuery](EventRule#eventrulequery) | [EventRulesInfo](./EventRule#eventrulesinfo) |
| [**stat**](./EventRule#stat) | [EventRuleStatQuery](EventRule#eventrulestatquery) | [Struct](./EventRule#struct) |



    
<br>

### create

desc: Creates a new EventRule. You can filter the Events to apply the EventRule by setting the input parameter `Conditions`. The method can change the Events' assignee or Project.
request_example: >-
{
"conditions": [{"key": "description", "value": "API", "operator": "contain"}],
"conditions_policy": "ALL",
"actions": {"change_assignee": "user1@email.com",
"change_urgency": "LOW",
"change_project": "project-123456789012",
"add_additional_info": {"type": "personal rule"},
"no_notification": true},
"options": {},
"project_id": "project-123456789012",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"event_rule_id": "er-123456789012",
"order": 1,
"conditions": [
{
"key": "description",
"value": "API",
"operator": "contain"
}
],
"conditions_policy": "ALL",
"actions": {
"change_assignee": "user1@email.com",
"change_urgency": "LOW",
"change_project": "project-123456789012",
"add_additional_info": {
"type": "personal rule"
},
"no_notification": true
},
"options": {},
"scope": "PROJECT",
"project_id": "project-123456789012",
"tags": {},
"domain_id": "domain-123456789012",
"created_at": "2022-01-02T06:02:31.517Z"
}



> **POST** /monitoring/v1/event-rule/create
>






    
<br>

### update

desc: Changes a priority order between EventRules to apply. EventRules are filtered by the order configured.
request_example: >-
{
"event_rule_id": "er-123456789012",
"conditions": [{"key": "description", "value": "ELB", "operator": "contain"}],
"conditions_policy": "ALL",
"actions": {"change_assignee": "user2@email.com",
"change_urgency": "HIGH",
"change_project": "project-123456789012",
"add_additional_info": {"type": "personal rule"},
"no_notification": true},
"options": {},
"domain_id": "domain-123456789012"
}
response_example: >-
{
"event_rule_id": "er-123456789012",
"order": 2,
"conditions": [
{
"key": "description",
"value": "ELB",
"operator": "contain"
}
],
"conditions_policy": "ALL",
"actions": {
"change_assignee": "user2@email.com",
"change_urgency": "HIGH",
"change_project": "project-123456789012",
"add_additional_info": {
"type": "personal rule"
},
"no_notification": true
},
"options": {},
"scope": "PROJECT",
"project_id": "project-123456789012",
"tags": {},
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T06:02:31.517Z"
}



> **POST** /monitoring/v1/event-rule/update
>






    
<br>

### change_order

desc: Updates a specific EventRule. You can make changes in EventRule settings.
request_example: >-
{
"event_rule_id": "er-123456789012",
"order": 2,
"domain_id": "domain-123456789012"
}
response_example: >-
{
"event_rule_id": "er-123456789012",
"order": 2,
"conditions": [
{
"key": "description",
"value": "API",
"operator": "contain"
}
],
"conditions_policy": "ALL",
"actions": {
"change_assignee": "user1@email.com",
"change_urgency": "LOW",
"change_project": "project-123456789012",
"add_additional_info": {
"type": "personal rule"
},
"no_notification": true
},
"options": {},
"scope": "PROJECT",
"project_id": "project-123456789012",
"tags": {},
"domain_id": "domain-123456789012",
"created_at": "2022-01-02T06:02:31.517Z"
}



> **POST** /monitoring/v1/event-rule/change-order
>






    
<br>

### delete

desc: Deletes a specific EventRule. You must assign an EventRule resource to delete by specifying `event_rule_id`.
request_example: >-
{
"event_rule_id": "er-123456789012",
"domain_id": "domain-123456789012"
}



> **POST** /monitoring/v1/event-rule/delete
>






    
<br>

### get

desc: Gets a specific EventRule. Prints detailed information about the EventRule.
request_example: >-
{
"event_rule_id": "er-123456789012",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"event_rule_id": "er-123456789012",
"order": 2,
"conditions": [
{
"key": "title",
"value": "ELB",
"operator": "contain"
}
],
"conditions_policy": "ALL",
"actions": {
"change_assignee": "user1@email.com",
"change_urgency": "LOW",
"change_project": "project-123456789012",
"add_additional_info": {},
"no_notification": true
},
"options": {},
"scope": "PROJECT",
"project_id": "project-123456789012",
"tags": {},
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T06:12:30.226Z"
}



> **POST** /monitoring/v1/event-rule/get
>






    
<br>

### list

desc: Gets a list of all EventRules. You can use a query to get a filtered list of EventRules. For example, you can adjust the scope of the list to a certain Project or Domain.
request_example: >-
{
"project_id": "project-123456789012",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"results": [
{
"event_rule_id": "er-123456789012",
"order": 1,
"conditions": [
{
"key": "title",
"value": "AWS",
"operator": "contain"
}
],
"conditions_policy": "ALL",
"actions": {
"change_assignee": "user2@email.com",
"change_urgency": "HIGH",
"add_additional_info": {},
"no_notification": true
},
"options": {},
"scope": "PROJECT",
"project_id": "project-123456789012",
"tags": {},
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T06:33:58.388Z"
},
{
"event_rule_id": "er-123456789012",
"order": 2,
"conditions": [
{
"key": "title",
"value": "ELB",
"operator": "contain"
}
],
"conditions_policy": "ALL",
"actions": {
"change_assignee": "user1@email.com",
"change_urgency": "LOW",
"change_project": "project-123456789012",
"add_additional_info": {},
"no_notification": true
},
"options": {},
"scope": "PROJECT",
"project_id": "project-123456789012",
"tags": {},
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T06:12:30.226Z"
}
],
"total_count": 2
}



> **POST** /monitoring/v1/event-rule/list
>






    
<br>

### stat





> **POST** /monitoring/v1/event-rule/stat
>






    


<br>
<br>

## Message



### ChangeEventRuleOrderRequest
* **event_rule_id** (string)  `Required` 

  *is_required: true*

    
* **order** (int32)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CreateEventRuleRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **conditions** (EventRuleCondition)  `Required` 

  *is_required: true*

    
* **conditions_policy** (ConditionsPolicy)  `Required` 

  *is_required: true*

    
* **actions** (EventRuleActions)  `Required` 

  *is_required: true*

    
* **options** (EventRuleOptions)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### EventRuleActionResponder
* **resource_type** (string)  `Required` 

    
* **resource_id** (string)  `Required` 

    <br>

### EventRuleActions
* **change_assignee** (string)  `Required` 

    
* **change_urgency** (string)  `Required` 

    
* **change_project** (string)  `Required` 

    
* **add_project_dependency** (string)  `Required` 

    
* **add_responder** (EventRuleActionResponder)  `Required` 

    
* **match_service_account** (MatchRule)  `Required` 

    
* **add_additional_info** (Struct)  `Required` 

    
* **no_notification** (bool)  `Required` 

    <br>

### EventRuleCondition
* **key** (string)  `Required` 

    
* **value** (string)  `Required` 

    
* **operator** (string)  `Required` 

    <br>

### EventRuleInfo
* **event_rule_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **order** (int32)  `Required` 

    
* **conditions** (EventRuleCondition)  `Required` 

    
* **conditions_policy** (ConditionsPolicy)  `Required` 

    
* **actions** (EventRuleActions)  `Required` 

    
* **options** (EventRuleOptions)  `Required` 

    
* **scope** (EventRuleScope)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### EventRuleOptions
* **stop_processing** (bool)  `Required` 

    <br>

### EventRuleQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **event_rule_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **scope** (EventRuleScope)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### EventRuleRequest
* **event_rule_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### EventRuleStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### EventRulesInfo
* **results** (EventRuleInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### GetEventRuleRequest
* **event_rule_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### MatchRule
* **source** (string)  `Required` 

    
* **target** (string)  `Required` 

    <br>

### UpdateEventRuleRequest
* **event_rule_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **conditions** (EventRuleCondition)  `Required` 

  *is_required: false*

    
* **conditions_policy** (ConditionsPolicy)  `Required` 

  *is_required: false*

    
* **actions** (EventRuleActions)  `Required` 

  *is_required: false*

    
* **options** (EventRuleOptions)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
