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

> **POST** /monitoring/v1/event-rule/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /monitoring/v1/event-rule/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### change_order

> **POST** /monitoring/v1/event-rule/change-order
>




 {{< tabs " change_order " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /monitoring/v1/event-rule/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /monitoring/v1/event-rule/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /monitoring/v1/event-rule/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /monitoring/v1/event-rule/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


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
