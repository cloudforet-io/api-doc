---
title: "ExternalAuth"
linkTitle: "ExternalAuth"
weight: 3
bookFlatSection: true
---
# [ExternalAuth](#ExternalAuth)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## ExternalAuth





**ExternalAuth Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**set**](./ExternalAuth#set) | [SetExternalAuthRequest](ExternalAuth#setexternalauthrequest) | [ExternalAuthInfo](ExternalAuth#externalauthinfo) |
| [**unset**](./ExternalAuth#unset) | [ExternalAuthRequest](ExternalAuth#externalauthrequest) | [ExternalAuthInfo](ExternalAuth#externalauthinfo) |
| [**get**](./ExternalAuth#get) | [ExternalAuthRequest](ExternalAuth#externalauthrequest) | [ExternalAuthInfo](ExternalAuth#externalauthinfo) |



    
<br>

### set





> **POST** /identity/v2/external-auth/set
>






    
<br>

### unset





> **POST** /identity/v2/external-auth/unset
>






    
<br>

### get





> **POST** /identity/v2/external-auth/get
>






    


<br>
<br>

## Message



### ExternalAuthInfo
* **domain_id** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **plugin_info** (PluginInfo)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### ExternalAuthRequest<br>

### SetExternalAuthRequest
* **plugin_info** (PluginRequest)   `Required` 

    <br>
