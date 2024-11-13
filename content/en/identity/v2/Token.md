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





 {{< tabs " issue " >}}

 {{< tab "Request Example" >}}



[IssueTokenRequest](./Token#issuetokenrequest)

* **credentials** (Struct)   `Required` 


* **domain_id** (string)   `Required` 


* **auth_type** (AuthType)  

  *LOCAL, EXTERNAL*


* **timeout** (int32)  


* **verify_code** (string)  

  *if MFA is enabled, verify_code is required*





{{< highlight json >}}
{
 "credentials": {
     "user_id": "wonny@cloudforet.io",
     "password": "Password0*"
 },
 "auth_type": "LOCAL",
 "domain_id": "domain-123123a"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### grant

+noauth



> **POST** /identity/v2/token/grant
>





 {{< tabs " grant " >}}

 {{< tab "Request Example" >}}



[GrantTokenRequest](./Token#granttokenrequest)

* **grant_type** (GrantType)   `Required` 


* **token** (string)   `Required` 


* **scope** (Scope)   `Required` 


* **timeout** (int32)  


* **permissions** (string)  `Repeated`   


* **domain_id** (string)  


* **workspace_id** (string)  





{{< highlight json >}}
{
 "grant_type": "REFRESH_TOKEN",
 "token": "your_refresh_token_from_issue",
 "scope": "DOMAIN",
 "domain_id": "domain-123123a"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    


<br>
<br>

## Message



### GrantTokenInfo
* **access_token** (string)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    <br>

### GrantTokenRequest
* **grant_type** (GrantType)   `Required` 

    
* **token** (string)   `Required` 

    
* **scope** (Scope)   `Required` 

    
* **timeout** (int32)  

    
* **permissions** (string)  `Repeated`   

    
* **domain_id** (string)  

    
* **workspace_id** (string)  

    <br>

### IssueTokenRequest
* **credentials** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **auth_type** (AuthType)  

  *LOCAL, EXTERNAL*

    
* **timeout** (int32)  

    
* **verify_code** (string)  

  *if MFA is enabled, verify_code is required*

    <br>

### TokenInfo
* **access_token** (string)   `Required` 

    
* **refresh_token** (string)   `Required` 

    <br>
