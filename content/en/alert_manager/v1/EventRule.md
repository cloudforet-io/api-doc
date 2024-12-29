---
title: "EventRule"
linkTitle: "EventRule"
weight: 3
bookFlatSection: true
---
# [EventRule](#EventRule)



>  **Package : spaceone.api.alert_manager.v1**

<br>
<br>

## EventRule





**EventRule Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./EventRule#create) | [EventRuleCreateRequest](EventRule#eventrulecreaterequest) | [EventRuleInfo](EventRule#eventruleinfo) |
| [**change_order**](./EventRule#change_order) | [EventRuleChangeOrderRequest](EventRule#eventrulechangeorderrequest) | [EventRuleInfo](EventRule#eventruleinfo) |
| [**update**](./EventRule#update) | [EventRuleUpdateRequest](EventRule#eventruleupdaterequest) | [EventRuleInfo](EventRule#eventruleinfo) |
| [**delete**](./EventRule#delete) | [EventRuleRequest](EventRule#eventrulerequest) | [Empty](EventRule#empty) |
| [**get**](./EventRule#get) | [EventRuleRequest](EventRule#eventrulerequest) | [EventRuleInfo](EventRule#eventruleinfo) |
| [**list**](./EventRule#list) | [EventRuleSearchQuery](EventRule#eventrulesearchquery) | [EventRulesInfo](EventRule#eventrulesinfo) |
| [**stat**](./EventRule#stat) | [EventRuleStatQuery](EventRule#eventrulestatquery) | [Struct](EventRule#struct) |



    
<br>

### create





> **POST** /alert-manager/v1/event-rule/create
>






    
<br>

### change_order





> **POST** /alert-manager/v1/event-rule/change-order
>






    
<br>

### update





> **POST** /alert-manager/v1/event-rule/update
>






    
<br>

### delete





> **POST** /alert-manager/v1/event-rule/delete
>






    
<br>

### get





> **POST** /alert-manager/v1/event-rule/get
>






    
<br>

### list





> **POST** /alert-manager/v1/event-rule/list
>






    
<br>

### stat





> **POST** /alert-manager/v1/event-rule/stat
>






    


<br>
<br>

## Message



### Condition
* **key** (string)   `Required` 

    
* **value** (string)   `Required` 

    
* **operator** (string)   `Required` 

    <br>

### EventRuleChangeOrderRequest
* **event_rule_id** (string)   `Required` 

    
* **order** (int32)   `Required` 

    <br>

### EventRuleCreateRequest
* **scope** (EventRuleScope)   `Required` 

    
* **conditions_policy** (ConditionsPolicy)   `Required` 

    
* **actions** (Struct)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **name** (string)  

    
* **conditions** (Condition)  `Repeated`   

    
* **options** (EventRuleOptions)  

    
* **tags** (Struct)  

    <br>

### EventRuleInfo
* **event_rule_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **scope** (EventRuleScope)   `Required` 

    
* **order** (int32)   `Required` 

    
* **conditions** (Condition)  `Repeated`    `Required` 

    
* **conditions_policy** (ConditionsPolicy)   `Required` 

    
* **actions** (Struct)   `Required` 

    
* **options** (EventRuleOptions)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **webhook_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### EventRuleOptions
* **stop_processing** (bool)   `Required` 

    <br>

### EventRuleRequest
* **event_rule_id** (string)   `Required` 

    <br>

### EventRuleSearchQuery
* **query** (Query)  

    
* **event_rule_id** (string)  

    
* **name** (string)  

    
* **scope** (EventRuleScope)  

    
* **workspace_id** (string)  

    
* **service_id** (string)  

    
* **webhook_id** (string)  

    <br>

### EventRuleStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### EventRuleUpdateRequest
* **event_rule_id** (string)   `Required` 

    
* **name** (string)  

    
* **conditions** (Condition)  `Repeated`   

    
* **conditions_policy** (ConditionsPolicy)  

    
* **actions** (Struct)  

    
* **options** (EventRuleOptions)  

    
* **tags** (Struct)  

    <br>

### EventRulesInfo
* **results** (EventRuleInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
