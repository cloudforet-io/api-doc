---
title: "Token"
linkTitle: "Token"
weight: 3
bookFlatSection: true
---
# [Token](#Token)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## Token





**Token Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**issue**](./Token#issue) | [IssueTokenRequest](Token#issuetokenrequest) | [TokenInfo](./Token#tokeninfo) |
| [**refresh**](./Token#refresh) | [Empty](Token#empty) | [TokenInfo](./Token#tokeninfo) |



    
<br>

### issue





> **POST** /identity/v1/token/issue
>






    
<br>

### refresh





> **POST** /identity/v1/token/refresh
>






    


<br>
<br>

## Message



### IssueTokenRequest
* **user_id** (string)  `Required` 

  *is_required: false*

    
* **credentials** (Struct)  `Required` 

  *is_required: true*

    
* **user_type** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **timeout** (int32)  `Required` 

  *is_required: false*

    
* **refresh_count** (int32)  `Required` 

  *is_required: false*

    <br>

### TokenInfo
* **access_token** (string)  `Required` 

    
* **refresh_token** (string)  `Required` 

    <br>
