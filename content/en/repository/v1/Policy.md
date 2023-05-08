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

> **POST** /repository/v1/policy/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /repository/v1/policy/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /repository/v1/policy/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /repository/v1/policy/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /repository/v1/policy/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /repository/v1/policy/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


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
