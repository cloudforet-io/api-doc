---
title: "EscalationPolicy"
linkTitle: "EscalationPolicy"
weight: 3
bookFlatSection: true
---
# [EscalationPolicy](#EscalationPolicy)



>  **Package : spaceone.api.alert_manager.v1**

<br>
<br>

## EscalationPolicy





**EscalationPolicy Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./EscalationPolicy#create) | [EscalationPolicyCreateRequest](EscalationPolicy#escalationpolicycreaterequest) | [EscalationPolicyInfo](EscalationPolicy#escalationpolicyinfo) |
| [**update**](./EscalationPolicy#update) | [EscalationPolicyUpdateRequest](EscalationPolicy#escalationpolicyupdaterequest) | [EscalationPolicyInfo](EscalationPolicy#escalationpolicyinfo) |
| [**delete**](./EscalationPolicy#delete) | [EscalationPolicyRequest](EscalationPolicy#escalationpolicyrequest) | [Empty](EscalationPolicy#empty) |
| [**get**](./EscalationPolicy#get) | [EscalationPolicyRequest](EscalationPolicy#escalationpolicyrequest) | [EscalationPolicyInfo](EscalationPolicy#escalationpolicyinfo) |
| [**list**](./EscalationPolicy#list) | [EscalationPolicySearchQuery](EscalationPolicy#escalationpolicysearchquery) | [EscalationPoliciesInfo](EscalationPolicy#escalationpoliciesinfo) |
| [**stat**](./EscalationPolicy#stat) | [EscalationPolicyStatQuery](EscalationPolicy#escalationpolicystatquery) | [Struct](EscalationPolicy#struct) |



    
<br>

### create





> **POST** /alert-manager/v1/escalation-policy/create
>






    
<br>

### update





> **POST** /alert-manager/v1/escalation-policy/update
>






    
<br>

### delete





> **POST** /alert-manager/v1/escalation-policy/delete
>






    
<br>

### get





> **POST** /alert-manager/v1/escalation-policy/get
>






    
<br>

### list





> **POST** /alert-manager/v1/escalation-policy/list
>






    
<br>

### stat





> **POST** /alert-manager/v1/escalation-policy/stat
>






    


<br>
<br>

## Message



### EscalationPoliciesInfo
* **results** (EscalationPolicyInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### EscalationPolicyCreateRequest
* **name** (string)   `Required` 

    
* **rules** (EscalationRule)  `Repeated`    `Required` 

    
* **service_id** (string)   `Required` 

    
* **repeat** (Repeat)  

    
* **finish_condition** (FinishCondition)  

    
* **tags** (Struct)  

    <br>

### EscalationPolicyInfo
* **escalation_policy_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **rules** (EscalationRule)  `Repeated`    `Required` 

    
* **repeat** (Repeat)   `Required` 

    
* **finish_condition** (FinishCondition)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### EscalationPolicyRequest
* **escalation_policy_id** (string)   `Required` 

    <br>

### EscalationPolicySearchQuery
* **query** (Query)  

    
* **escalation_policy_id** (string)  

    
* **name** (string)  

    
* **finish_condition** (FinishCondition)  

    
* **service_id** (string)  

    <br>

### EscalationPolicyStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### EscalationPolicyUpdateRequest
* **escalation_policy_id** (string)   `Required` 

    
* **name** (string)  

    
* **rules** (EscalationRule)  `Repeated`   

    
* **finish_condition** (FinishCondition)  

    
* **repeat** (Repeat)  

    
* **tags** (Struct)  

    <br>

### EscalationRule
* **channels** (string)  `Repeated`    `Required` 

    
* **escalate_minutes** (int32)   `Required` 

    <br>

### Repeat
* **state** (RepeatState)   `Required` 

    
* **count** (int32)   `Required` 

    <br>
