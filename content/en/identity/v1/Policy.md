---
title: "Policy"
linkTitle: "Policy"
weight: 3
bookFlatSection: true
---
# [Policy](#Policy)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## Policy





**Policy Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Policy#create) | [CreatePolicyRequest](Policy#createpolicyrequest) | [PolicyInfo](./Policy#policyinfo) |
| [**update**](./Policy#update) | [UpdatePolicyRequest](Policy#updatepolicyrequest) | [PolicyInfo](./Policy#policyinfo) |
| [**delete**](./Policy#delete) | [PolicyRequest](Policy#policyrequest) | [Empty](./Policy#empty) |
| [**get**](./Policy#get) | [GetPolicyRequest](Policy#getpolicyrequest) | [PolicyInfo](./Policy#policyinfo) |
| [**list**](./Policy#list) | [PolicyQuery](Policy#policyquery) | [PoliciesInfo](./Policy#policiesinfo) |
| [**stat**](./Policy#stat) | [PolicyStatQuery](Policy#policystatquery) | [Struct](./Policy#struct) |



    
<br>

### create





> **POST** /identity/v1/policy/create
>






    
<br>

### update





> **PUT** /identity/v1/policy/update
>






    
<br>

### delete





> **POST** /identity/v1/policy/delete
>






    
<br>

### get





> **POST** /identity/v1/policy/get
>






    
<br>

### list





> **POST** /identity/v1/policy/list
>






    
<br>

### stat





> **POST** /identity/v1/policies/stat
>






    


<br>
<br>

## Message



### CreatePolicyRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **permissions** (string)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetPolicyRequest
* **policy_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### PoliciesInfo
* **results** (PolicyInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### PolicyInfo
* **policy_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **permissions** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### PolicyQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **policy_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

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

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
