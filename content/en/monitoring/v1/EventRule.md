---
title: "EventRule"
linkTitle: "EventRule"
weight: 3
bookFlatSection: true
---
# [EventRule](#EventRule)
An EventRule is a rule to transform the request data when an Event is generated.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## EventRule





**EventRule Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./EventRule#create) | [CreateEventRuleRequest](EventRule#createeventrulerequest) | [EventRuleInfo](EventRule#eventruleinfo) |
| [**update**](./EventRule#update) | [UpdateEventRuleRequest](EventRule#updateeventrulerequest) | [EventRuleInfo](EventRule#eventruleinfo) |
| [**change_order**](./EventRule#change_order) | [ChangeEventRuleOrderRequest](EventRule#changeeventruleorderrequest) | [EventRuleInfo](EventRule#eventruleinfo) |
| [**delete**](./EventRule#delete) | [EventRuleRequest](EventRule#eventrulerequest) | [Empty](EventRule#empty) |
| [**get**](./EventRule#get) | [EventRuleRequest](EventRule#eventrulerequest) | [EventRuleInfo](EventRule#eventruleinfo) |
| [**list**](./EventRule#list) | [EventRuleQuery](EventRule#eventrulequery) | [EventRulesInfo](EventRule#eventrulesinfo) |
| [**stat**](./EventRule#stat) | [EventRuleStatQuery](EventRule#eventrulestatquery) | [Struct](EventRule#struct) |



    
<br>

### create

Creates a new EventRule. You can filter the Events to apply the EventRule by setting the input parameter `Conditions`. The method can change the Events' assignee or Project.



> **POST** /monitoring/v1/event-rule/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateEventRuleRequest](./EventRule#createeventrulerequest)

* **name** (string)   `Required` 


* **conditions** (EventRuleCondition)  `Repeated`    `Required` 


* **conditions_policy** (ConditionsPolicy)   `Required` 


* **actions** (EventRuleActions)   `Required` 


* **resource_group** (ResourceGroup)   `Required` 


* **options** (EventRuleOptions)  


* **tags** (Struct)  


* **project_id** (string)  





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[EventRuleInfo](#EVENTRULEINFO)
* **event_rule_id** (string)   `Required` 

* **name** (string)   `Required` 

* **order** (int32)   `Required` 

* **conditions** (EventRuleCondition)  `Repeated`   `Required` 

* **conditions_policy** (ConditionsPolicy)   `Required` 

* **actions** (EventRuleActions)   `Required` 

* **options** (EventRuleOptions)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Changes a priority order between EventRules to apply. EventRules are filtered by the order configured.



> **POST** /monitoring/v1/event-rule/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateEventRuleRequest](./EventRule#updateeventrulerequest)

* **event_rule_id** (string)   `Required` 


* **name** (string)  


* **conditions** (EventRuleCondition)  `Repeated`   


* **conditions_policy** (ConditionsPolicy)  


* **actions** (EventRuleActions)  


* **options** (EventRuleOptions)  


* **tags** (Struct)  





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[EventRuleInfo](#EVENTRULEINFO)
* **event_rule_id** (string)   `Required` 

* **name** (string)   `Required` 

* **order** (int32)   `Required` 

* **conditions** (EventRuleCondition)  `Repeated`   `Required` 

* **conditions_policy** (ConditionsPolicy)   `Required` 

* **actions** (EventRuleActions)   `Required` 

* **options** (EventRuleOptions)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### change_order

Updates a specific EventRule. You can make changes in EventRule settings.



> **POST** /monitoring/v1/event-rule/change-order
>





 {{< tabs " change_order " >}}

 {{< tab "Request Example" >}}



[ChangeEventRuleOrderRequest](./EventRule#changeeventruleorderrequest)

* **event_rule_id** (string)   `Required` 


* **order** (int32)   `Required` 





{{< highlight json >}}
{
   "event_rule_id": "er-123456789012", 
   "order": 2,
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[EventRuleInfo](#EVENTRULEINFO)
* **event_rule_id** (string)   `Required` 

* **name** (string)   `Required` 

* **order** (int32)   `Required` 

* **conditions** (EventRuleCondition)  `Repeated`   `Required` 

* **conditions_policy** (ConditionsPolicy)   `Required` 

* **actions** (EventRuleActions)   `Required` 

* **options** (EventRuleOptions)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific EventRule. You must assign an EventRule resource to delete by specifying `event_rule_id`.



> **POST** /monitoring/v1/event-rule/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[EventRuleRequest](./EventRule#eventrulerequest)

* **event_rule_id** (string)   `Required` 





{{< highlight json >}}
{
   "event_rule_id": "er-123456789012",
   "order": 2,
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific EventRule. Prints detailed information about the EventRule.



> **POST** /monitoring/v1/event-rule/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[EventRuleRequest](./EventRule#eventrulerequest)

* **event_rule_id** (string)   `Required` 





{{< highlight json >}}
{
   "event_rule_id": "er-123456789012",
   "order": 2,
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[EventRuleInfo](#EVENTRULEINFO)
* **event_rule_id** (string)   `Required` 

* **name** (string)   `Required` 

* **order** (int32)   `Required` 

* **conditions** (EventRuleCondition)  `Repeated`   `Required` 

* **conditions_policy** (ConditionsPolicy)   `Required` 

* **actions** (EventRuleActions)   `Required` 

* **options** (EventRuleOptions)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all EventRules. You can use a query to get a filtered list of EventRules. For example, you can adjust the scope of the list to a certain Project or Domain.



> **POST** /monitoring/v1/event-rule/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[EventRuleQuery](./EventRule#eventrulequery)

* **query** (Query)  


* **event_rule_id** (string)  


* **name** (string)  


* **workspace_id** (string)  


* **project_id** (string)  





{{< highlight json >}}
{
   "project_id": "project-123456789012",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[EventRulesInfo](#EVENTRULESINFO)
* **results** (EventRuleInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /monitoring/v1/event-rule/stat
>






    


<br>
<br>

## Message



### ChangeEventRuleOrderRequest
* **event_rule_id** (string)   `Required` 

    
* **order** (int32)   `Required` 

    <br>

### CreateEventRuleRequest
* **name** (string)   `Required` 

    
* **conditions** (EventRuleCondition)  `Repeated`    `Required` 

    
* **conditions_policy** (ConditionsPolicy)   `Required` 

    
* **actions** (EventRuleActions)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **options** (EventRuleOptions)  

    
* **tags** (Struct)  

    
* **project_id** (string)  

    <br>

### EventRuleActionResponder
* **resource_type** (string)   `Required` 

    
* **resource_id** (string)   `Required` 

    <br>

### EventRuleActions
* **change_assignee** (string)   `Required` 

    
* **change_urgency** (string)   `Required` 

    
* **change_project** (string)   `Required` 

    
* **change_escalation_policy** (string)   `Required` 

    
* **match_service_account** (MatchRule)   `Required` 

    
* **add_additional_info** (Struct)   `Required` 

    
* **no_notification** (bool)   `Required` 

    <br>

### EventRuleCondition
* **key** (string)   `Required` 

    
* **value** (string)   `Required` 

    
* **operator** (string)   `Required` 

    <br>

### EventRuleInfo
* **event_rule_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **order** (int32)   `Required` 

    
* **conditions** (EventRuleCondition)  `Repeated`    `Required` 

    
* **conditions_policy** (ConditionsPolicy)   `Required` 

    
* **actions** (EventRuleActions)   `Required` 

    
* **options** (EventRuleOptions)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### EventRuleOptions
* **stop_processing** (bool)   `Required` 

    <br>

### EventRuleQuery
* **query** (Query)  

    
* **event_rule_id** (string)  

    
* **name** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### EventRuleRequest
* **event_rule_id** (string)   `Required` 

    <br>

### EventRuleStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### EventRulesInfo
* **results** (EventRuleInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### MatchRule
* **source** (string)   `Required` 

    
* **target** (string)   `Required` 

    <br>

### UpdateEventRuleRequest
* **event_rule_id** (string)   `Required` 

    
* **name** (string)  

    
* **conditions** (EventRuleCondition)  `Repeated`   

    
* **conditions_policy** (ConditionsPolicy)  

    
* **actions** (EventRuleActions)  

    
* **options** (EventRuleOptions)  

    
* **tags** (Struct)  

    <br>
