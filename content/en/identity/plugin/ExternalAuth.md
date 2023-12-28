---
title: "ExternalAuth"
linkTitle: "ExternalAuth"
weight: 3
bookFlatSection: true
---
# [ExternalAuth](#ExternalAuth)



>  **Package : spaceone.api.identity.plugin**

<br>
<br>

## ExternalAuth





**ExternalAuth Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](./ExternalAuth#init) | [InitRequest](ExternalAuth#initrequest) | [PluginInfo](ExternalAuth#plugininfo) |
| [**authorize**](./ExternalAuth#authorize) | [AuthorizeRequest](ExternalAuth#authorizerequest) | [UserInfo](ExternalAuth#userinfo) |



    
<br>

### init










    
<br>

### authorize










    


<br>
<br>

## Message



### AuthorizeRequest
* **options** (Struct)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **credentials** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **schema_id** (string)  

    <br>

### InitRequest
* **options** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### PluginInfo
* **metadata** (Struct)   `Required` 

    <br>

### UserInfo
* **user_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **email** (string)   `Required` 

    
* **mobile** (string)   `Required` 

    
* **group** (string)   `Required` 

    
* **state** (State)   `Required` 

    <br>
