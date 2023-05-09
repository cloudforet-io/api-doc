---
title: "Policy"
linkTitle: "Policy"
weight: 3
bookFlatSection: true
---
# [Policy](#Policy)
desc: A Policy is a resource managing page access permissions. This resource can be used in all domains if it is defined in the `repository` microservice.


>  **Package : spaceone.api.repository.v1**

<br>
<br>

## Policy





**Policy Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Policy#create) | [CreatePolicyRequest](Policy#createpolicyrequest) | [PolicyInfo](./Policy#policyinfo) |
| [**update**](./Policy#update) | [UpdatePolicyRequest](Policy#updatepolicyrequest) | [PolicyInfo](./Policy#policyinfo) |
| [**delete**](./Policy#delete) | [PolicyRequest](Policy#policyrequest) | [Empty](./Policy#empty) |
| [**get**](./Policy#get) | [GetRepositoryPolicyRequest](Policy#getrepositorypolicyrequest) | [PolicyInfo](./Policy#policyinfo) |
| [**list**](./Policy#list) | [PolicyQuery](Policy#policyquery) | [PoliciesInfo](./Policy#policiesinfo) |
| [**stat**](./Policy#stat) | [PolicyStatQuery](Policy#policystatquery) | [Struct](./Policy#struct) |



    
<br>

### create

desc: Creates a new Policy. The parameter `policy_id`, an identifier of Policy resources, can only include lowercase alphabets, numbers, and hyphens(-). The parameter `permissions` is a list type data describing page access permissions.
request_example: >-
{
"policy_id": "policy-custom-full-acess",
"name": "Full Access",
"permissions": ["*"],
"labels": [],
"tags": {},
"domain_id": "domain-123456789012"
}
response_example: >-
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



> **POST** /repository/v1/policy/create
>






    
<br>

### update

desc: Updates a specific Policy. You can make changes in Policy settings, including `name`, `labels`, `tags`, and `permissions`. The parameter `policy_id` cannot be updated.
request_example: >-
{
"policy_id": "policy-custom-full-acess",
"name": "Full Access",
"permissions": ["*"],
"labels": [],
"tags": {},
"domain_id": "domain-123456789012"
}
response_example: >-
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



> **POST** /repository/v1/policy/update
>






    
<br>

### delete

desc: Deletes a specific Policy. You must specify the `policy_id` of the Policy to delete, as the `policy_id` is an identifier of Policy resources.
request_example: >-
{
"policy_id": "policy-123456789012"
}



> **POST** /repository/v1/policy/delete
>






    
<br>

### get

desc: Gets a specific Policy. You must specify the `policy_id` of the Policy to get, as the `policy_id` is an identifier of Policy resources. You can use the parameter `repository_id` to limit the scope of the method to a specific Repository.
request_example: >-
{
"policy_id": "policy-123456789012",
"repository_id": "repo-123456789012"
}
response_example: >-
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
}



> **POST** /repository/v1/policy/get
>






    
<br>

### list

desc: Gets a list of all Policies in a specific Repository. The parameter `repository_id` is used as an identifier of a Repository to get its list of Policies. You can use a query to get a filtered list of Policies.
request_example: >-
{
"query": {},
"repository_id": "repo-123456789012"
}
response_example: >-
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



> **POST** /repository/v1/policy/list
>






    
<br>

### stat





> **POST** /repository/v1/policy/stat
>






    


<br>
<br>

## Message



### CreatePolicyRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **permissions** (string)  `Required` 

  *is_required: true*

    
* **policy_id** (string)  `Required` 

  *is_required: true*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetRepositoryPolicyRequest
* **policy_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **repository_id** (string)  `Required` 

  *is_required: false*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### PoliciesInfo
* **results** (PolicyInfo)  `Required` 

  *desc: list of PolicyInfo*

    
* **total_count** (int32)  `Required` 

    <br>

### PolicyInfo
* **policy_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **state** (State)  `Required` 

    
* **permissions** (string)  `Required` 

  *desc: list of permissions*

    
* **labels** (ListValue)  `Required` 

  *desc: list of labels*

    
* **tags** (Struct)  `Required` 

    
* **repository_info** (RepositoryInfo)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### PolicyQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **policy_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **repository_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **state** (State)  `Required` 

  *is_required: false*

    <br>

### PolicyRequest
* **policy_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### PolicyStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **repository_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdatePolicyRequest
* **policy_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **permissions** (string)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
