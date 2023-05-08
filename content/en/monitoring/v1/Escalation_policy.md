---
title: "Escalation_policy"
linkTitle: "Escalation_policy"
weight: 3
bookFlatSection: true
---
# [Escalation_policy](#Escalation_policy)
desc: An EscalationPolicy is a set of rules to deliver an alert to assigned members.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## Escalation_policy


**EscalationPolicy Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./EscalationPolicy#create) | [CreateEscalationPolicyRequest](EscalationPolicy#createescalationpolicyrequest) | [EscalationPolicyInfo](./EscalationPolicy#escalationpolicyinfo) |
| [**update**](./EscalationPolicy#update) | [UpdateEscalationPolicyRequest](EscalationPolicy#updateescalationpolicyrequest) | [EscalationPolicyInfo](./EscalationPolicy#escalationpolicyinfo) |
| [**set_default**](./EscalationPolicy#set_default) | [EscalationPolicyRequest](EscalationPolicy#escalationpolicyrequest) | [EscalationPolicyInfo](./EscalationPolicy#escalationpolicyinfo) |
| [**delete**](./EscalationPolicy#delete) | [EscalationPolicyRequest](EscalationPolicy#escalationpolicyrequest) | [Empty](./EscalationPolicy#empty) |
| [**get**](./EscalationPolicy#get) | [GetEscalationPolicyRequest](EscalationPolicy#getescalationpolicyrequest) | [EscalationPolicyInfo](./EscalationPolicy#escalationpolicyinfo) |
| [**list**](./EscalationPolicy#list) | [EscalationPolicyQuery](EscalationPolicy#escalationpolicyquery) | [EscalationPoliciesInfo](./EscalationPolicy#escalationpoliciesinfo) |
| [**stat**](./EscalationPolicy#stat) | [EscalationPolicyStatQuery](EscalationPolicy#escalationpolicystatquery) | [Struct](./EscalationPolicy#struct) |



    
<br>

### create

> **POST** /monitoring/v1/escalation-policy/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /monitoring/v1/escalation-policy/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### set_default

> **POST** /monitoring/v1/escalation-policy/set-default
>




 {{< tabs " set_default " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /monitoring/v1/escalation-policy/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /monitoring/v1/escalation-policy/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /monitoring/v1/escalation-policy/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /monitoring/v1/escalation-policy/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateEscalationPolicyRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **rules** (EscalationPolicyRule)  `Required` 

  *is_required: true*

    
* **repeat_count** (int32)  `Required` 

  *is_required: false*

    
* **finish_condition** (EscalationFinishCondition)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### EscalationPoliciesInfo
* **results** (EscalationPolicyInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### EscalationPolicyInfo
* **escalation_policy_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **is_default** (bool)  `Required` 

    
* **rules** (EscalationPolicyRule)  `Required` 

    
* **repeat_count** (int32)  `Required` 

    
* **finish_condition** (EscalationFinishCondition)  `Required` 

    
* **scope** (EscalationPolicyScope)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### EscalationPolicyQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **escalation_policy_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **is_default** (bool)  `Required` 

  *is_required: false*

    
* **finish_condition** (EscalationFinishCondition)  `Required` 

  *is_required: false*

    
* **scope** (EscalationPolicyScope)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### EscalationPolicyRequest
* **escalation_policy_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### EscalationPolicyRule
* **notification_level** (NotificationLevel)  `Required` 

    
* **escalate_minutes** (int32)  `Required` 

    <br>

### EscalationPolicyStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetEscalationPolicyRequest
* **escalation_policy_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### UpdateEscalationPolicyRequest
* **escalation_policy_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **rules** (EscalationPolicyRule)  `Required` 

  *is_required: false*

    
* **repeat_count** (int32)  `Required` 

  *is_required: false*

    
* **finish_condition** (EscalationFinishCondition)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
