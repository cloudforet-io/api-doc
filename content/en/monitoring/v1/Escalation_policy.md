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

desc: Creates a new EscalationPolicy. When creating an EscalationPolicy, if the project_id is assigned, the EscalationPolicy is applied to the Project with the same project_id. If an EscalationPolicy is set as a global policy, all Projects in the same domain can apply the policy.
request_example: >-
{
"name": "es-test",
"rules": [{"notification_level": "LV1", "escalate_minutes": 30},
{"notification_level": "LV2", "escalate_minutes": 30}],
"repeat_count": 2,
"finish_condition": "ACKNOWLEDGED",
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"escalation_policy_id": "ep-526e536fdca9",
"name": "es-test",
"rules": [
{
"notification_level": "LV1",
"escalate_minutes": 30
},
{
"notification_level": "LV2",
"escalate_minutes": 30
}
],
"repeat_count": 2,
"finish_condition": "ACKNOWLEDGED",
"scope": "DOMAIN",
"tags": {},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-21T09:22:45.340Z"
}



> **POST** /monitoring/v1/escalation-policy/create
>






    
<br>

### update

desc: Updates a specific EscalationPolicy. You can make changes in EscalationPolicy settings, including the name, the escalation process, and the number of iterations.
request_example: >-
{
"escalation_policy_id": "ep-526e536fdca9",
"name": "es-test2",
"rules": [{"notification_level": "LV1", "escalate_minutes": 15},
{"notification_level": "LV2", "escalate_minutes": 15},
{"notification_level": "LV3", "escalate_minutes": 15}],
"repeat_count": 1,
"finish_condition": "RESOLVED",
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"escalation_policy_id": "ep-526e536fdca9",
"name": "es-test2",
"rules": [
{
"notification_level": "LV1",
"escalate_minutes": 15
},
{
"notification_level": "LV2",
"escalate_minutes": 15
},
{
"notification_level": "LV3",
"escalate_minutes": 15
}
],
"repeat_count": 1,
"finish_condition": "RESOLVED",
"scope": "DOMAIN",
"tags": {},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-21T09:22:45.340Z"
}



> **POST** /monitoring/v1/escalation-policy/update
>






    
<br>

### set_default

desc: Sets a specific EscalationPolicy as default. Only policies configured as global can be set as default. When a Project is created, even if you did not configure any policy to the Project, the default policy set by this api method is applied.
request_example: >-
{
"escalation_policy_id": "ep-526e536fdca9",
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"escalation_policy_id": "ep-526e536fdca9",
"name": "es-test2",
"is_default": true,
"rules": [
{
"notification_level": "LV1",
"escalate_minutes": 15
},
{
"notification_level": "LV2",
"escalate_minutes": 15
},
{
"notification_level": "LV3",
"escalate_minutes": 15
}
],
"repeat_count": 1,
"finish_condition": "RESOLVED",
"scope": "DOMAIN",
"tags": {},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-21T09:22:45.340Z"
}



> **POST** /monitoring/v1/escalation-policy/set-default
>






    
<br>

### delete

desc: Deletes a specific EscalationPolicy. Deletes the EscalationPolicy with the escalation_policy_id from the deletion request.
request_example: >-
{
"escalation_policy_id": "ep-d75670166af4",
"domain_id": "domain-58010aa2e451"
}



> **POST** /monitoring/v1/escalation-policy/delete
>






    
<br>

### get

desc: Gets a specific EscalationPolicy. Prints detailed information about the EscalationPolicy, including the name, rules, and termination conditions.
request_example: >-
{
"escalation_policy_id": "ep-d75670166af4",
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"escalation_policy_id": "ep-d75670166af4",
"name": "0525-ms-test-2",
"rules": [
{
"notification_level": "LV2",
"escalate_minutes": 30
},
{
"notification_level": "LV2"
}
],
"finish_condition": "ACKNOWLEDGED",
"scope": "DOMAIN",
"tags": {},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-05-25T09:31:38.573Z"
}



> **POST** /monitoring/v1/escalation-policy/get
>






    
<br>

### list

desc: Gets a list of all EscalationPolicies. You can use a query to get a filtered list of EscalationPolicies.
request_example: >-
{
"query": {},
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"results": [
{
"escalation_policy_id": "ep-7c9745003372",
"name": "0525-ms-test-1",
"rules": [
{
"notification_level": "LV1"
}
],
"finish_condition": "ACKNOWLEDGED",
"scope": "DOMAIN",
"tags": {},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-05-25T09:31:15.150Z"
},
{
"escalation_policy_id": "ep-d75670166af4",
"name": "0525-ms-test-2",
"rules": [
{
"notification_level": "LV2",
"escalate_minutes": 30
},
{
"notification_level": "LV2"
}
],
"finish_condition": "ACKNOWLEDGED",
"scope": "DOMAIN",
"tags": {},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-05-25T09:31:38.573Z"
}
],
"total_count": 2
}



> **POST** /monitoring/v1/escalation-policy/list
>






    
<br>

### stat





> **POST** /monitoring/v1/escalation-policy/stat
>






    


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
