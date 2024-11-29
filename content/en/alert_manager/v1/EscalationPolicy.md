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
| [**delete**](./EscalationPolicy#delete) | [EscalationPolicyRequest](EscalationPolicy#escalationpolicyrequest) | [Empty](EscalationPolicy#empty) |
| [**get**](./EscalationPolicy#get) | [EscalationPolicyRequest](EscalationPolicy#escalationpolicyrequest) | [EscalationPolicyInfo](EscalationPolicy#escalationpolicyinfo) |
| [**list**](./EscalationPolicy#list) | [EscalationPolicySearchQuery](EscalationPolicy#escalationpolicysearchquery) | [EscalationPoliciesInfo](EscalationPolicy#escalationpoliciesinfo) |
| [**stat**](./EscalationPolicy#stat) | [EscalationPolicyStatQuery](EscalationPolicy#escalationpolicystatquery) | [Struct](EscalationPolicy#struct) |



    
<br>

### create





> **POST** /alert-manager/v1/escalation-policy/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[EscalationPolicyCreateRequest](./EscalationPolicy#escalationpolicycreaterequest)

* **name** (string)   `Required` 


* **rules** (Struct)  `Repeated`    `Required` 


* **service_id** (string)   `Required` 


* **repeat_count** (int32)  


* **finish_condition** (FinishCondition)  


* **tags** (Struct)  





{{< highlight json >}}
Receive
////////
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
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





> **POST** /alert_manager/v1/escalation-policy/stat
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

    
* **rules** (Struct)  `Repeated`    `Required` 

    
* **service_id** (string)   `Required` 

    
* **repeat_count** (int32)  

    
* **finish_condition** (FinishCondition)  

    
* **tags** (Struct)  

    <br>

### EscalationPolicyInfo
* **escalation_policy_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **rules** (Struct)  `Repeated`    `Required` 

    
* **repeat_count** (int32)   `Required` 

    
* **finish_condition** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### EscalationPolicyRequest
* **escalation_policy_id** (string)   `Required` 

    <br>

### EscalationPolicySearchQuery
* **query** (Query)  

    
* **escalation_policy_id** (string)  

    
* **name** (string)  

    
* **finish_condition** (string)  

    
* **service_id** (string)  

    <br>

### EscalationPolicyStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>
