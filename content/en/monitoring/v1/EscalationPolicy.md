---
title: "EscalationPolicy"
linkTitle: "EscalationPolicy"
weight: 3
bookFlatSection: true
---
# [EscalationPolicy](#EscalationPolicy)
An EscalationPolicy is a set of rules to deliver an alert to assigned members.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## EscalationPolicy





**EscalationPolicy Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./EscalationPolicy#create) | [CreateEscalationPolicyRequest](EscalationPolicy#createescalationpolicyrequest) | [EscalationPolicyInfo](EscalationPolicy#escalationpolicyinfo) |
| [**update**](./EscalationPolicy#update) | [UpdateEscalationPolicyRequest](EscalationPolicy#updateescalationpolicyrequest) | [EscalationPolicyInfo](EscalationPolicy#escalationpolicyinfo) |
| [**set_default**](./EscalationPolicy#set_default) | [EscalationPolicyRequest](EscalationPolicy#escalationpolicyrequest) | [EscalationPolicyInfo](EscalationPolicy#escalationpolicyinfo) |
| [**delete**](./EscalationPolicy#delete) | [EscalationPolicyRequest](EscalationPolicy#escalationpolicyrequest) | [Empty](EscalationPolicy#empty) |
| [**get**](./EscalationPolicy#get) | [EscalationPolicyRequest](EscalationPolicy#escalationpolicyrequest) | [EscalationPolicyInfo](EscalationPolicy#escalationpolicyinfo) |
| [**list**](./EscalationPolicy#list) | [EscalationPolicyQuery](EscalationPolicy#escalationpolicyquery) | [EscalationPoliciesInfo](EscalationPolicy#escalationpoliciesinfo) |
| [**stat**](./EscalationPolicy#stat) | [EscalationPolicyStatQuery](EscalationPolicy#escalationpolicystatquery) | [Struct](EscalationPolicy#struct) |



    
<br>

### create

Creates a new EscalationPolicy. When creating an EscalationPolicy, if the project_id is assigned, the EscalationPolicy is applied to the Project with the same project_id. If an EscalationPolicy is set as a global policy, all Projects in the same domain can apply the policy.



> **POST** /monitoring/v1/escalation-policy/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateEscalationPolicyRequest](./EscalationPolicy#createescalationpolicyrequest)

* **name** (string)   `Required` 


* **rules** (EscalationPolicyRule)  `Repeated`    `Required` 


* **resource_group** (ResourceGroup)   `Required` 


* **repeat_count** (int32)  


* **finish_condition** (EscalationFinishCondition)  


* **project_id** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "name": "es-test",
   "rules": [{"notification_level": "LV1", "escalate_minutes": 30},
             {"notification_level": "LV2", "escalate_minutes": 30}],
   "repeat_count": 2,
   "finish_condition": "ACKNOWLEDGED",
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[EscalationPolicyInfo](#ESCALATIONPOLICYINFO)
* **escalation_policy_id** (string)   `Required` 

* **name** (string)   `Required` 

* **is_default** (bool)   `Required` 

* **rules** (EscalationPolicyRule)  `Repeated`   `Required` 

* **repeat_count** (int32)   `Required` 

* **finish_condition** (EscalationFinishCondition)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **project_id** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **workspace_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific EscalationPolicy. You can make changes in EscalationPolicy settings, including the name, the escalation process, and the number of iterations.



> **POST** /monitoring/v1/escalation-policy/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateEscalationPolicyRequest](./EscalationPolicy#updateescalationpolicyrequest)

* **escalation_policy_id** (string)   `Required` 


* **name** (string)  


* **rules** (EscalationPolicyRule)  `Repeated`   


* **repeat_count** (int32)  


* **finish_condition** (EscalationFinishCondition)  


* **tags** (Struct)  





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[EscalationPolicyInfo](#ESCALATIONPOLICYINFO)
* **escalation_policy_id** (string)   `Required` 

* **name** (string)   `Required` 

* **is_default** (bool)   `Required` 

* **rules** (EscalationPolicyRule)  `Repeated`   `Required` 

* **repeat_count** (int32)   `Required` 

* **finish_condition** (EscalationFinishCondition)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **project_id** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **workspace_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### set_default

Sets a specific EscalationPolicy as default. Only policies configured as global can be set as default. When a Project is created, even if you did not configure any policy to the Project, the default policy set by this api method is applied.



> **POST** /monitoring/v1/escalation-policy/set-default
>





 {{< tabs " set_default " >}}

 {{< tab "Request Example" >}}



[EscalationPolicyRequest](./EscalationPolicy#escalationpolicyrequest)

* **escalation_policy_id** (string)   `Required` 





{{< highlight json >}}
{
   "escalation_policy_id": "ep-526e536fdca9",
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[EscalationPolicyInfo](#ESCALATIONPOLICYINFO)
* **escalation_policy_id** (string)   `Required` 

* **name** (string)   `Required` 

* **is_default** (bool)   `Required` 

* **rules** (EscalationPolicyRule)  `Repeated`   `Required` 

* **repeat_count** (int32)   `Required` 

* **finish_condition** (EscalationFinishCondition)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **project_id** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **workspace_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific EscalationPolicy. Deletes the EscalationPolicy with the escalation_policy_id from the deletion request.



> **POST** /monitoring/v1/escalation-policy/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[EscalationPolicyRequest](./EscalationPolicy#escalationpolicyrequest)

* **escalation_policy_id** (string)   `Required` 





{{< highlight json >}}
{
   "escalation_policy_id": "ep-526e536fdca9",
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific EscalationPolicy. Prints detailed information about the EscalationPolicy, including the name, rules, and termination conditions.



> **POST** /monitoring/v1/escalation-policy/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[EscalationPolicyRequest](./EscalationPolicy#escalationpolicyrequest)

* **escalation_policy_id** (string)   `Required` 





{{< highlight json >}}
{
   "escalation_policy_id": "ep-526e536fdca9",
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[EscalationPolicyInfo](#ESCALATIONPOLICYINFO)
* **escalation_policy_id** (string)   `Required` 

* **name** (string)   `Required` 

* **is_default** (bool)   `Required` 

* **rules** (EscalationPolicyRule)  `Repeated`   `Required` 

* **repeat_count** (int32)   `Required` 

* **finish_condition** (EscalationFinishCondition)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **project_id** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **workspace_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all EscalationPolicies. You can use a query to get a filtered list of EscalationPolicies.



> **POST** /monitoring/v1/escalation-policy/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[EscalationPolicyQuery](./EscalationPolicy#escalationpolicyquery)

* **resource_group** (ResourceGroup)   `Required` 


* **query** (Query)  


* **escalation_policy_id** (string)  


* **name** (string)  


* **is_default** (bool)  


* **finish_condition** (EscalationFinishCondition)  


* **project_id** (string)  





{{< highlight json >}}
{
   "query": {},
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[EscalationPoliciesInfo](#ESCALATIONPOLICIESINFO)
* **results** (EscalationPolicyInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /monitoring/v1/escalation-policy/stat
>






    


<br>
<br>

## Message



### CreateEscalationPolicyRequest
* **name** (string)   `Required` 

    
* **rules** (EscalationPolicyRule)  `Repeated`    `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **repeat_count** (int32)  

    
* **finish_condition** (EscalationFinishCondition)  

    
* **project_id** (string)  

    
* **tags** (Struct)  

    <br>

### EscalationPoliciesInfo
* **results** (EscalationPolicyInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### EscalationPolicyInfo
* **escalation_policy_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **is_default** (bool)   `Required` 

    
* **rules** (EscalationPolicyRule)  `Repeated`    `Required` 

    
* **repeat_count** (int32)   `Required` 

    
* **finish_condition** (EscalationFinishCondition)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### EscalationPolicyQuery
* **resource_group** (ResourceGroup)   `Required` 

    
* **query** (Query)  

    
* **escalation_policy_id** (string)  

    
* **name** (string)  

    
* **is_default** (bool)  

    
* **finish_condition** (EscalationFinishCondition)  

    
* **project_id** (string)  

    <br>

### EscalationPolicyRequest
* **escalation_policy_id** (string)   `Required` 

    <br>

### EscalationPolicyRule
* **notification_level** (NotificationLevel)   `Required` 

    
* **escalate_minutes** (int32)   `Required` 

    <br>

### EscalationPolicyStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### UpdateEscalationPolicyRequest
* **escalation_policy_id** (string)   `Required` 

    
* **name** (string)  

    
* **rules** (EscalationPolicyRule)  `Repeated`   

    
* **repeat_count** (int32)  

    
* **finish_condition** (EscalationFinishCondition)  

    
* **tags** (Struct)  

    <br>
