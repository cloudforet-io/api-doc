---
title: "Policy"
linkTitle: "Policy"
weight: 3
bookFlatSection: true
---
# [Policy](#Policy)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Policy





**Policy Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Policy#create) | [CreatePolicyRequest](Policy#createpolicyrequest) | [PolicyInfo](Policy#policyinfo) |
| [**update**](./Policy#update) | [UpdatePolicyRequest](Policy#updatepolicyrequest) | [PolicyInfo](Policy#policyinfo) |
| [**delete**](./Policy#delete) | [PolicyRequest](Policy#policyrequest) | [Empty](Policy#empty) |
| [**get**](./Policy#get) | [PolicyRequest](Policy#policyrequest) | [PolicyInfo](Policy#policyinfo) |
| [**list**](./Policy#list) | [PolicySearchQuery](Policy#policysearchquery) | [PoliciesInfo](Policy#policiesinfo) |
| [**stat**](./Policy#stat) | [PolicyStatQuery](Policy#policystatquery) | [Struct](Policy#struct) |



    
<br>

### create





> **POST** /identity/v2/policy/create
>






    
<br>

### update





> **POST** /identity/v2/policy/update
>






    
<br>

### delete





> **POST** /identity/v2/policy/delete
>






    
<br>

### get





> **POST** /identity/v2/policy/get
>






    
<br>

### list





> **POST** /identity/v2/policy/list
>






    
<br>

### stat





> **POST** /identity/v2/policy/stat
>






    


<br>
<br>

## Message



### CreatePolicyRequest
* **name** (string)   `Required` 

    
* **permissions** (string)  `Repeated`    `Required` 

    
* **domain_id** (string)   `Required` 

    
* **tags** (Struct)  

    <br>

### PoliciesInfo
* **results** (PolicyInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### PolicyInfo
* **policy_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **permissions** (string)  `Repeated`    `Required` 

    
* **tags** (Struct)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### PolicyRequest
* **policy_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### PolicySearchQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **policy_id** (string)  

    
* **name** (string)  

    <br>

### PolicyStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### UpdatePolicyRequest
* **policy_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **permissions** (string)  `Repeated`   

    
* **tags** (Struct)  

    <br>
