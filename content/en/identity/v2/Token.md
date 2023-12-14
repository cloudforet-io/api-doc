---
title: "Token"
linkTitle: "Token"
weight: 3
bookFlatSection: true
---
# [Token](#Token)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Token





**Token Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**issue**](./Token#issue) | [IssueTokenRequest](Token#issuetokenrequest) | [TokenInfo](Token#tokeninfo) |
| [**grant**](./Token#grant) | [GrantTokenRequest](Token#granttokenrequest) | [GrantTokenInfo](Token#granttokeninfo) |



    
<br>

### issue

+noauth



> **POST** /identity/v2/token/issue
>






    
<br>

### grant

+noauth



> **POST** /identity/v2/token/grant
>






    


<br>
<br>

## Message



### GrantTokenInfo
* **access_token** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### GrantTokenRequest
* **grant_type** (GrantType)   `Required` 

    
* **token** (string)   `Required` 

    
* **scope** (Scope)   `Required` 

    
* **workspace_id** (string)  

    <br>

### IssueTokenRequest
* **credentials** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **auth_type** (AuthType)  

  *LOCAL, EXTERNAL*

    
* **refresh_timeout** (int32)  

    
* **verify_code** (string)  

  *if MFA is enabled, verify_code is required*

    <br>

### TokenInfo
* **access_token** (string)   `Required` 

    
* **refresh_token** (string)   `Required` 

    <br>
