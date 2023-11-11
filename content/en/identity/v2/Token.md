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
| [**refresh**](./Token#refresh) | [Empty](Token#empty) | [TokenInfo](Token#tokeninfo) |



    
<br>

### issue

+noauth



> **POST** /identity/v2/token/issue
>






    
<br>

### refresh

+noauth



> **POST** /identity/v2/token/refresh
>






    


<br>
<br>

## Message



### IssueTokenRequest
* **credentials** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **auth_type** (AuthType)  

  *LOCAL, EXTERNAL*

    
* **timeout** (int32)  

    
* **refresh_count** (int32)  

    
* **verify_code** (string)  

  *if MFA is enabled, verify_code is required*

    <br>

### TokenInfo
* **access_token** (string)   `Required` 

    
* **refresh_token** (string)   `Required` 

    <br>
