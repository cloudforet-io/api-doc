---
title: "Handler"
linkTitle: "Handler"
weight: 3
bookFlatSection: true
---
# [Handler](#Handler)



>  **Package : spaceone.api.core.v2**

<br>
<br>

## Handler







<br>
<br>

## Message



### AuthenticationRequest
* **domain_id** (string)   `Required` 

    <br>

### AuthenticationResponse
* **domain_id** (string)   `Required` 

    
* **public_key** (string)   `Required` 

    <br>

### AuthorizationRequest
* **scope** (string)   `Required` 

    
* **owner_type** (OwnerType)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **app_id** (string)   `Required` 

    
* **api_key_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### AuthorizationResponse
* **role_type** (RoleType)   `Required` 

    
* **user_projects** (string)  `Repeated`    `Required` 

    <br>

### EventRequest
* **service** (string)   `Required` 

    
* **resource** (string)   `Required` 

    
* **verb** (string)   `Required` 

    
* **status** (string)   `Required` 

    
* **message** (Struct)   `Required` 

    <br>
