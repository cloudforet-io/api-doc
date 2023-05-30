---
title: "Policy"
linkTitle: "Policy"
weight: 3
bookFlatSection: true
---
# [Policy](#Policy)
A Policy is a resource managing page access permissions. This resource can be used in all domains if it is defined in the `repository` microservice.


>  **Package : spaceone.api.repository.v1**

<br>
<br>

## Policy





**Policy Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Policy#create) | [CreatePolicyRequest](Policy#createpolicyrequest) | [PolicyInfo](Policy#policyinfo) |
| [**update**](./Policy#update) | [UpdatePolicyRequest](Policy#updatepolicyrequest) | [PolicyInfo](Policy#policyinfo) |
| [**delete**](./Policy#delete) | [PolicyRequest](Policy#policyrequest) | [Empty](Policy#empty) |
| [**get**](./Policy#get) | [GetRepositoryPolicyRequest](Policy#getrepositorypolicyrequest) | [PolicyInfo](Policy#policyinfo) |
| [**list**](./Policy#list) | [PolicyQuery](Policy#policyquery) | [PoliciesInfo](Policy#policiesinfo) |
| [**stat**](./Policy#stat) | [PolicyStatQuery](Policy#policystatquery) | [Struct](Policy#struct) |



    
<br>

### create

Creates a new Policy. The parameter `policy_id`, an identifier of Policy resources, can only include lowercase alphabets, numbers, and hyphens(-). The parameter `permissions` is a list type data describing page access permissions.



> **POST** /repository/v1/policy/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreatePolicyRequest](./Policy#createpolicyrequest)

* **name** (string)   `Required` 


* **permissions** (string)  `Repeated`    `Required` 


* **policy_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **labels** (ListValue)  


* **tags** (Struct)  


* **project_id** (string)  





{{< highlight json >}}
{
   "policy_id": "policy-custom-full-acess",
   "name": "Full Access",
   "permissions": ["*"],
   "labels": [],
   "tags": {},
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PolicyInfo](#POLICYINFO)
* **policy_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **permissions** (string)  `Repeated`   `Required` 

  list of permissions

* **labels** (ListValue)   `Required` 

  list of labels

* **tags** (Struct)   `Required` 

* **repository_info** (RepositoryInfo)   `Required` 

* **project_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
   "policy_id": "policy-custom-full-acess",
   "name": "Full Access",
   "state": "ENABLED",
   "permissions": [
       "*"
   ],
   "labels": [],
   "tags": {},
   "repository_info": {
       "repository_id": "repo-123456789012",
       "name": "Local",
       "repository_type": "local"
   },
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:45:04.582Z",
   "updated_at": "2022-01-01T06:45:04.582Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Policy. You can make changes in Policy settings, including `name`, `labels`, `tags`, and `permissions`. The parameter `policy_id` cannot be updated.



> **POST** /repository/v1/policy/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdatePolicyRequest](./Policy#updatepolicyrequest)

* **policy_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **name** (string)  


* **permissions** (string)  `Repeated`   


* **labels** (ListValue)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "policy_id": "policy-custom-full-acess",
   "name": "Full Access",
   "permissions": ["*"],
   "labels": [],
   "tags": {},
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PolicyInfo](#POLICYINFO)
* **policy_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **permissions** (string)  `Repeated`   `Required` 

  list of permissions

* **labels** (ListValue)   `Required` 

  list of labels

* **tags** (Struct)   `Required` 

* **repository_info** (RepositoryInfo)   `Required` 

* **project_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
   "policy_id": "policy-custom-full-acess",
   "name": "Full Access",
   "state": "ENABLED",
   "permissions": [
       "*"
   ],
   "labels": [],
   "tags": {},
   "repository_info": {
       "repository_id": "repo-123456789012",
       "name": "Local",
       "repository_type": "local"
   },
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:45:04.582Z",
   "updated_at": "2022-01-01T06:45:04.582Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific Policy. You must specify the `policy_id` of the Policy to delete, as the `policy_id` is an identifier of Policy resources.



> **POST** /repository/v1/policy/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[PolicyRequest](./Policy#policyrequest)

* **policy_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "policy_id": "policy-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Policy. You must specify the `policy_id` of the Policy to get, as the `policy_id` is an identifier of Policy resources. You can use the parameter `repository_id` to limit the scope of the method to a specific Repository.



> **POST** /repository/v1/policy/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetRepositoryPolicyRequest](./Policy#getrepositorypolicyrequest)

* **policy_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **repository_id** (string)  


* **only** (string)  `Repeated`   





{{< highlight json >}}
{
   "policy_id": "policy-123456789012",
   "repository_id": "repo-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PolicyInfo](#POLICYINFO)
* **policy_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **permissions** (string)  `Repeated`   `Required` 

  list of permissions

* **labels** (ListValue)   `Required` 

  list of labels

* **tags** (Struct)   `Required` 

* **repository_info** (RepositoryInfo)   `Required` 

* **project_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
   "policy_id": "policy-custom-full-acess",
   "name": "Full Access",
   "state": "ENABLED",
   "permissions": [
       "*"
   ],
   "labels": [],
   "tags": {},
   "repository_info": {
       "repository_id": "repo-123456789012",
       "name": "Local",
       "repository_type": "local"
   },
   "domain_id": "domain-123456789012",
   "created_at": "2022-01-01T06:45:04.582Z",
   "updated_at": "2022-01-01T06:45:04.582Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Policies in a specific Repository. The parameter `repository_id` is used as an identifier of a Repository to get its list of Policies. You can use a query to get a filtered list of Policies.



> **POST** /repository/v1/policy/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[PolicyQuery](./Policy#policyquery)

* **repository_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **query** (Query)  


* **policy_id** (string)  


* **name** (string)  


* **project_id** (string)  


* **state** (State)  





{{< highlight json >}}
{
   "query": {},
   "repository_id": "repo-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PoliciesInfo](#POLICIESINFO)
* **results** (PolicyInfo)  `Repeated`   `Required` 

  list of PolicyInfo

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
   "results": [
       {
           "policy_id": "policy-123456789012",
           "name": "Full Access",
           "state": "ENABLED",
           "permissions": [
               "*"
           ],
           "labels": [],
           "tags": {},
           "repository_info": {
               "repository_id": "repo-123456789012",
               "name": "Local",
               "repository_type": "local"
           },
           "domain_id": "domain-123456789012",
           "created_at": "2022-01-01T15:42:50.943Z",
           "updated_at": "2022-01-01T15:42:50.943Z"
       },
       {
           "policy_id": "policy-987654321098",
           "name": "Identity Admin",
           "state": "ENABLED",
           "permissions": [
               "identity.*"
           ],
           "labels": [],
           "tags": {},
           "repository_info": {
               "repository_id": "repo-123456789012",
               "name": "Local",
               "repository_type": "local"
           },
           "domain_id": "domain-123456789012",
           "created_at": "2022-01-01T08:08:14.756Z",
           "updated_at": "2022-01-01T08:08:14.756Z"
       }
   ],
   "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /repository/v1/policy/stat
>






    


<br>
<br>

## Message



### CreatePolicyRequest
* **name** (string)   `Required` 

    
* **permissions** (string)  `Repeated`    `Required` 

    
* **policy_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    
* **project_id** (string)  

    <br>

### GetRepositoryPolicyRequest
* **policy_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **repository_id** (string)  

    
* **only** (string)  `Repeated`   

    <br>

### PoliciesInfo
* **results** (PolicyInfo)  `Repeated`    `Required` 

  *list of PolicyInfo*

    
* **total_count** (int32)   `Required` 

    <br>

### PolicyInfo
* **policy_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **permissions** (string)  `Repeated`    `Required` 

  *list of permissions*

    
* **labels** (ListValue)   `Required` 

  *list of labels*

    
* **tags** (Struct)   `Required` 

    
* **repository_info** (RepositoryInfo)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PolicyQuery
* **repository_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **policy_id** (string)  

    
* **name** (string)  

    
* **project_id** (string)  

    
* **state** (State)  

    <br>

### PolicyRequest
* **policy_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### PolicyStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **repository_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### UpdatePolicyRequest
* **policy_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **permissions** (string)  `Repeated`   

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>
