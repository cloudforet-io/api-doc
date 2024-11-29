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
| [**change_order**](./EventRule#change_order) | [EventRuleChangeMemberRequest](EventRule#eventrulechangememberrequest) | [EventRuleInfo](EventRule#eventruleinfo) |
| [**update**](./EventRule#update) | [EventRuleUpdateRequest](EventRule#eventruleupdaterequest) | [EventRuleInfo](EventRule#eventruleinfo) |
| [**delete**](./EventRule#delete) | [EventRuleRequest](EventRule#eventrulerequest) | [Empty](EventRule#empty) |
| [**get**](./EventRule#get) | [EventRuleRequest](EventRule#eventrulerequest) | [EventRuleInfo](EventRule#eventruleinfo) |
| [**list**](./EventRule#list) | [EventRuleSearchQuery](EventRule#eventrulesearchquery) | [EventRulesInfo](EventRule#eventrulesinfo) |
| [**stat**](./EventRule#stat) | [EventRuleStatQuery](EventRule#eventrulestatquery) | [Struct](EventRule#struct) |



    
<br>

### create





> **POST** /alert-manager/v1/comment/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[EventRuleCreateRequest](./EventRule#eventrulecreaterequest)

* **conditions** (Struct)  `Repeated`    `Required` 


* **conditions_policy** (ConditionsPolicy)   `Required` 


* **actions** (Struct)   `Required` 


* **service_id** (string)   `Required` 


* **name** (string)  


* **options** (Options)  


* **tags** (Struct)  





{{< highlight json >}}
Receive
////////
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### change_order





> **POST** /alert-manager/v1/comment/change-order
>






    
<br>

### update





> **POST** /alert-manager/v1/comment/update
>






    
<br>

### delete





> **POST** /alert-manager/v1/comment/delete
>






    
<br>

### get





> **POST** /alert-manager/v1/comment/get
>






    
<br>

### list





> **POST** /alert-manager/v1/comment/list
>






    
<br>

### stat





> **POST** /alert_manager/v1/comment/stat
>






    


<br>
<br>

## Message



### EventRuleChangeMemberRequest
* **event_rule_id** (string)   `Required` 

    
* **order** (int32)   `Required` 

    <br>

### EventRuleCreateRequest
* **conditions** (Struct)  `Repeated`    `Required` 

    
* **conditions_policy** (ConditionsPolicy)   `Required` 

    
* **actions** (Struct)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **name** (string)  

    
* **options** (Options)  

    
* **tags** (Struct)  

    <br>

### EventRuleInfo
* **event_rule_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **order** (int32)   `Required` 

    
* **conditions** (Struct)  `Repeated`    `Required` 

    
* **conditions_policy** (ConditionsPolicy)   `Required` 

    
* **actions** (Struct)   `Required` 

    
* **options** (Options)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### EventRuleRequest
* **event_rule_id** (string)   `Required` 

    <br>

### EventRuleSearchQuery
* **query** (Query)  

    
* **event_rule_id** (string)  

    
* **name** (string)  

    
* **resource_group** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### EventRuleStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### EventRuleUpdateRequest
* **event_rule_id** (string)   `Required` 

    
* **name** (string)  

    
* **conditions** (Struct)  `Repeated`   

    
* **conditions_policy** (ConditionsPolicy)  

    
* **actions** (Struct)  

    
* **options** (Options)  

    
* **tags** (Struct)  

    <br>

### EventRulesInfo
* **results** (EventRuleInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
